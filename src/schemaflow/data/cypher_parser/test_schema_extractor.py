from __future__ import annotations

import sys
import traceback

from schemaflow.data.cypher_parser.schema_extractor import extract_schema


def sets(result: dict) -> dict:
    return {k: set(v) for k, v in result.items()}


def test_simple_node_with_label_and_return_prop():
    q = "MATCH (n:Person) RETURN n.name"
    r = sets(extract_schema(q))
    assert r["nodes"] == {"Person"}
    assert r["node_props"] == {("Person", "name")}
    assert r["relations"] == set()
    assert r["relation_props"] == set()


def test_inline_map_property_on_node():
    q = "MATCH (n:Person {name: 'Bob'}) RETURN n"
    r = sets(extract_schema(q))
    assert r["nodes"] == {"Person"}
    assert r["node_props"] == {("Person", "name")}


def test_property_in_where_clause():
    q = "MATCH (n:Person) WHERE n.age > 30 RETURN n"
    r = sets(extract_schema(q))
    assert ("Person", "age") in r["node_props"]


def test_property_in_with_clause():
    q = "MATCH (n:Person) WITH n.name AS name RETURN name"
    r = sets(extract_schema(q))
    assert ("Person", "name") in r["node_props"]


def test_chained_property_access_only_first_hop_captured():
    q = "MATCH (n:Person) RETURN n.address.city"
    r = sets(extract_schema(q))
    assert ("Person", "address") in r["node_props"]
    assert ("Person", "city") not in r["node_props"]


def test_directed_relationship_left_to_right():
    q = "MATCH (a:Person)-[r:KNOWS]->(b:Person) RETURN a"
    r = sets(extract_schema(q))
    assert r["relations"] == {("Person", "KNOWS", "Person")}


def test_directed_relationship_right_to_left():
    q = "MATCH (n:Person)<-[r0:createdBy]-(m0:Sculpture) RETURN n"
    r = sets(extract_schema(q))
    assert r["relations"] == {("Sculpture", "createdBy", "Person")}


def test_undirected_relationship_defaults_to_forward():
    q = "MATCH (a:Person)-[r:FRIENDS_WITH]-(b:Person) RETURN a"
    r = sets(extract_schema(q))
    assert ("Person", "FRIENDS_WITH", "Person") in r["relations"]


def test_multi_hop_chain_gold_example():
    q = (
        "MATCH (n:Person)<-[r0:createdBy]-(m0:Sculpture)"
        "-[r1:displayedAt]->(m1:Museum {name: 'Museum Boijmans Van Beuningen'}) "
        "WITH DISTINCT n RETURN n.name, n.date_of_death"
    )
    r = sets(extract_schema(q))
    assert r["nodes"] == {"Museum", "Sculpture", "Person"}
    assert r["node_props"] == {
        ("Museum", "name"),
        ("Person", "name"),
        ("Person", "date_of_death"),
    }
    assert r["relations"] == {
        ("Sculpture", "createdBy", "Person"),
        ("Sculpture", "displayedAt", "Museum"),
    }
    assert r["relation_props"] == set()


def test_untyped_relationship_yields_no_relation():
    q = "MATCH (a:Person)-->(b:Company) RETURN a"
    r = sets(extract_schema(q))
    assert r["relations"] == set()
    assert r["nodes"] == {"Person", "Company"}


def test_anonymous_nodes_and_relationship_no_crash():
    q = "MATCH ()-[:KNOWS]->() RETURN 1"
    r = sets(extract_schema(q))
    assert r["relations"] == set()


def test_or_relationship_types_both_captured():
    q = "MATCH (a:Person)-[r:KNOWS|FOLLOWS]->(b:Person) RETURN a"
    r = sets(extract_schema(q))
    assert r["relations"] == {
        ("Person", "KNOWS", "Person"),
        ("Person", "FOLLOWS", "Person"),
    }


def test_and_labels_both_captured_and_props_apply_to_both():
    q = "MATCH (a:Person&Employee {name: 'x'}) RETURN a"
    r = sets(extract_schema(q))
    assert r["nodes"] == {"Person", "Employee"}
    assert r["node_props"] == {("Person", "name"), ("Employee", "name")}


def test_negated_label_still_recorded():
    q = "MATCH (a:!Person) RETURN a"
    r = sets(extract_schema(q))
    assert "Person" in r["nodes"]


def test_wildcard_label_contributes_nothing():
    q = "MATCH (a:%) RETURN a"
    r = sets(extract_schema(q))
    assert r["nodes"] == set()


def test_dynamic_label_skipped_without_crash():
    q = "MATCH (a:$(someExpr)) RETURN a"
    r = sets(extract_schema(q))
    assert r["nodes"] == set()


def test_set_property():
    q = "MATCH (n:Person) SET n.age = 40"
    r = sets(extract_schema(q))
    assert ("Person", "age") in r["node_props"]


def test_remove_property():
    q = "MATCH (n:Person) REMOVE n.age"
    r = sets(extract_schema(q))
    assert ("Person", "age") in r["node_props"]


def test_set_labels_colon_syntax():
    q = "MATCH (n) WHERE n.id = 1 SET n:Person:Employee"
    r = sets(extract_schema(q))
    assert r["nodes"] == {"Person", "Employee"}


def test_set_labels_is_syntax():
    q = "MATCH (n) SET n IS Person"
    r = sets(extract_schema(q))
    assert "Person" in r["nodes"]


def test_set_relationship_property():
    q = "MATCH (a:Person)-[r:KNOWS]->(b:Person) SET r.since = 2020"
    r = sets(extract_schema(q))
    assert ("KNOWS", "since") in r["relation_props"]


def test_variable_reused_without_repeating_label():
    q = "MATCH (n:Person) MATCH (n)-[r:KNOWS]->(m:Person) RETURN n"
    r = sets(extract_schema(q))
    assert ("Person", "KNOWS", "Person") in r["relations"]


def test_relationship_variable_reused_for_prop_after_separate_match():
    q = (
        "MATCH (a:Person)-[r:KNOWS]->(b:Person) "
        "WITH r "
        "MATCH (x:Person) WHERE r.since > 2000 "
        "RETURN x"
    )
    r = sets(extract_schema(q))
    assert ("KNOWS", "since") in r["relation_props"]


def test_node_reused_without_label_props_still_attributed():
    q = "MATCH (n:Person) MATCH (n) SET n.nickname = 'Bo'"
    r = sets(extract_schema(q))
    assert ("Person", "nickname") in r["node_props"]


def test_optional_match():
    q = "OPTIONAL MATCH (n:Person)-[:WORKS_AT]->(c:Company) RETURN n"
    r = sets(extract_schema(q))
    assert ("Person", "WORKS_AT", "Company") in r["relations"]


def test_merge_clause():
    q = "MERGE (n:Person {name: 'Bob'})-[:KNOWS]->(m:Person {name: 'Alice'})"
    r = sets(extract_schema(q))
    assert r["nodes"] == {"Person"}
    assert r["node_props"] == {("Person", "name")}
    assert ("Person", "KNOWS", "Person") in r["relations"]


def test_create_clause():
    q = "CREATE (n:Person {name: 'Bob'})"
    r = sets(extract_schema(q))
    assert r["nodes"] == {"Person"}
    assert ("Person", "name") in r["node_props"]


def test_foreach_with_nested_create():
    q = (
        "MATCH (n:Person) "
        "FOREACH (x IN [1,2,3] | CREATE (m:Tag {name: 'x'})-[:TAGGED]->(n))"
    )
    r = sets(extract_schema(q))
    assert "Tag" in r["nodes"]
    assert ("Tag", "TAGGED", "Person") in r["relations"]


def test_call_subquery():
    q = "CALL { MATCH (n:Person) RETURN n } RETURN n"
    r = sets(extract_schema(q))
    assert "Person" in r["nodes"]


def test_backtick_quoted_names_are_unescaped():
    q = "MATCH (`my node`:`My Label` {`weird prop`: 1}) RETURN 1"
    r = sets(extract_schema(q))
    assert r["nodes"] == {"My Label"}
    assert r["node_props"] == {("My Label", "weird prop")}


def test_variable_length_relationship_no_crash():
    q = "MATCH (a:Person)-[r:KNOWS*1..3]->(b:Person) RETURN a"
    r = sets(extract_schema(q))
    assert ("Person", "KNOWS", "Person") in r["relations"]


def test_quantified_gpm_relationship_no_crash():
    q = "MATCH (a:Person)-[:KNOWS]->{1,3}(b:Person) RETURN a"
    r = sets(extract_schema(q))
    assert isinstance(r["relations"], set)


def test_parenthesized_quantified_path_no_crash():
    q = "MATCH ((a:Person)-[:KNOWS]->(b:Person))+ RETURN a"
    r = sets(extract_schema(q))
    assert isinstance(r["nodes"], set)


def test_property_in_order_by():
    q = "MATCH (n:Person) RETURN n ORDER BY n.name"
    r = sets(extract_schema(q))
    assert ("Person", "name") in r["node_props"]


def test_property_in_case_expression():
    q = "MATCH (n:Person) RETURN CASE n.status WHEN 'active' THEN 1 ELSE 0 END"
    r = sets(extract_schema(q))
    assert ("Person", "status") in r["node_props"]


def test_property_in_aggregation_function():
    q = "MATCH (n:Person) RETURN count(n.name), sum(n.score)"
    r = sets(extract_schema(q))
    assert ("Person", "name") in r["node_props"]
    assert ("Person", "score") in r["node_props"]


def test_property_in_list_comprehension():
    q = "MATCH (n:Person) RETURN [x IN n.friends | x.name]"
    r = sets(extract_schema(q))
    assert ("Person", "friends") in r["node_props"]


def test_property_in_pattern_comprehension():
    q = "MATCH (a:Person) RETURN [(a)-[r:KNOWS]->(b:Person) | b.name]"
    r = sets(extract_schema(q))
    assert ("Person", "KNOWS", "Person") in r["relations"]
    assert ("Person", "name") in r["node_props"]


def test_map_projection_with_dots():
    q = "MATCH (n:Person) RETURN n{.name, .age, .email}"
    r = sets(extract_schema(q))
    assert ("Person", "name") in r["node_props"]
    assert ("Person", "age") in r["node_props"]
    assert ("Person", "email") in r["node_props"]


def test_map_projection_with_key_value():
    q = "MATCH (n:Person) RETURN n{fullName: n.name, years: n.age}"
    r = sets(extract_schema(q))
    assert ("Person", "name") in r["node_props"]
    assert ("Person", "age") in r["node_props"]


def test_map_projection_nested():
    q = "MATCH (n:Person) RETURN n{address: n{.city, .zip}}"
    r = sets(extract_schema(q))
    assert ("Person", "address") in r["node_props"]


def test_multiple_patterns_comma_separated():
    q = "MATCH (a:Person), (b:Company) WHERE a.id = b.ceo RETURN a, b"
    r = sets(extract_schema(q))
    assert r["nodes"] == {"Person", "Company"}
    assert ("Person", "id") in r["node_props"]
    assert ("Company", "ceo") in r["node_props"]


def test_multiple_patterns_with_relationship():
    q = "MATCH (a:Person)-[:WORKS_AT]->(c:Company), (c)-[:LOCATED_IN]->(loc:City) RETURN a"
    r = sets(extract_schema(q))
    assert ("Person", "WORKS_AT", "Company") in r["relations"]
    assert ("Company", "LOCATED_IN", "City") in r["relations"]


def test_where_exists_pattern():
    q = "MATCH (n:Person) WHERE EXISTS((n)-[:KNOWS]->(m:Person)) RETURN n"
    r = sets(extract_schema(q))
    assert ("Person", "KNOWS", "Person") in r["relations"]


def test_where_not_exists_pattern():
    q = "MATCH (n:Person) WHERE NOT EXISTS((n)-[:BLOCKED]->(m:Person)) RETURN n"
    r = sets(extract_schema(q))
    assert ("Person", "BLOCKED", "Person") in r["relations"]


def test_where_any_predicate():
    q = "MATCH (n:Person) WHERE ANY(tag IN n.tags WHERE tag = 'admin') RETURN n"
    r = sets(extract_schema(q))
    assert ("Person", "tags") in r["node_props"]


def test_where_all_predicate():
    q = "MATCH (n:Order) WHERE ALL(item IN n.items WHERE item.price > 0) RETURN n"
    r = sets(extract_schema(q))
    assert ("Order", "items") in r["node_props"]


def test_where_none_predicate():
    q = "MATCH (n:Order) WHERE NONE(item IN n.items WHERE item.cancelled = true) RETURN n"
    r = sets(extract_schema(q))
    assert ("Order", "items") in r["node_props"]


def test_where_single_predicate():
    q = "MATCH (n:Person) WHERE SINGLE(friend IN n.friends WHERE friend.age > 30) RETURN n"
    r = sets(extract_schema(q))
    assert ("Person", "friends") in r["node_props"]


def test_exists_subquery():
    q = "MATCH (n:Person) WHERE EXISTS { MATCH (n)-[r:KNOWS]->(m:Person {active: true}) } RETURN n"
    r = sets(extract_schema(q))
    assert ("Person", "KNOWS", "Person") in r["relations"]
    assert ("Person", "active") in r["node_props"]


def test_count_subquery():
    q = "MATCH (n:Person) RETURN n, COUNT { (n)-[:KNOWS]->(:Person) } AS friendCount"
    r = sets(extract_schema(q))
    assert ("Person", "KNOWS", "Person") in r["relations"]


def test_call_procedure_with_yield():
    q = "CALL db.indexes() YIELD name, state RETURN name"
    r = sets(extract_schema(q))
    assert isinstance(r["nodes"], set)


def test_call_procedure_no_yield():
    q = "CALL apoc.help('graph')"
    r = sets(extract_schema(q))
    assert isinstance(r["nodes"], set)


def test_delete_node():
    q = "MATCH (n:Person) DELETE n"
    r = sets(extract_schema(q))
    assert "Person" in r["nodes"]


def test_detach_delete_node():
    q = "MATCH (n:Person)-[r:KNOWS]->(m:Person) DETACH DELETE n"
    r = sets(extract_schema(q))
    assert "Person" in r["nodes"]
    assert ("Person", "KNOWS", "Person") in r["relations"]


def test_merge_with_on_create():
    q = "MERGE (n:Person {name: 'Bob'}) ON CREATE SET n.createdAt = datetime()"
    r = sets(extract_schema(q))
    assert ("Person", "name") in r["node_props"]
    assert ("Person", "createdAt") in r["node_props"]


def test_merge_with_on_match():
    q = "MERGE (n:Person {name: 'Bob'}) ON MATCH SET n.lastSeen = datetime()"
    r = sets(extract_schema(q))
    assert ("Person", "name") in r["node_props"]
    assert ("Person", "lastSeen") in r["node_props"]


def test_shortest_path_function():
    q = "MATCH (a:Person {name: 'A'}), (b:Person {name: 'B'}) RETURN shortestPath((a)-[:KNOWS*]-(b))"
    r = sets(extract_schema(q))
    assert ("Person", "KNOWS", "Person") in r["relations"]


def test_all_shortest_paths_function():
    q = "MATCH (a:Person), (b:Person) RETURN allShortestPaths((a)-[:CONNECTED*]-(b))"
    r = sets(extract_schema(q))
    assert ("Person", "CONNECTED", "Person") in r["relations"]


def test_union_queries():
    q = "MATCH (n:Person) RETURN n.name UNION MATCH (c:Company) RETURN c.name"
    r = sets(extract_schema(q))
    assert "Person" in r["nodes"]
    assert "Company" in r["nodes"]
    assert ("Person", "name") in r["node_props"]
    assert ("Company", "name") in r["node_props"]


def test_union_all_queries():
    q = "MATCH (n:Person)-[:KNOWS]->(m:Person) RETURN m UNION ALL MATCH (n:Person)-[:FOLLOWS]->(m:Person) RETURN m"
    r = sets(extract_schema(q))
    assert ("Person", "KNOWS", "Person") in r["relations"]
    assert ("Person", "FOLLOWS", "Person") in r["relations"]


def test_return_star():
    q = "MATCH (n:Person {id: 1}) RETURN *"
    r = sets(extract_schema(q))
    assert "Person" in r["nodes"]
    assert ("Person", "id") in r["node_props"]


def test_comments_single_line():
    q = "MATCH (n:Person) // This is a comment\nRETURN n.name"
    r = sets(extract_schema(q))
    assert ("Person", "name") in r["node_props"]


def test_comments_multi_line():
    q = "/* comment \n spanning lines */ MATCH (n:Person) RETURN n.name"
    r = sets(extract_schema(q))
    assert ("Person", "name") in r["node_props"]


def test_semicolon_separated_statements():
    q = "MATCH (n:Person) RETURN n; MATCH (c:Company) RETURN c"
    r = sets(extract_schema(q))
    assert "Person" in r["nodes"]
    assert "Company" in r["nodes"]


def test_parameter_not_interpreted_as_property():
    q = "MATCH (n:Person) WHERE n.id = $id RETURN n"
    r = sets(extract_schema(q))
    assert ("Person", "id") in r["node_props"]


def test_string_literal_not_property():
    q = "MATCH (n:Person) WHERE n.name = 'Alice' RETURN n"
    r = sets(extract_schema(q))
    assert ("Person", "name") in r["node_props"]
    assert ("Person", "Alice") not in r["node_props"]


def test_numeric_literal_not_property():
    q = "MATCH (n:Person) WHERE n.age = 30 RETURN n"
    r = sets(extract_schema(q))
    assert ("Person", "age") in r["node_props"]


def test_relationship_property_in_where():
    q = "MATCH (a:Person)-[r:KNOWS]->(b:Person) WHERE r.since > 2020 RETURN a"
    r = sets(extract_schema(q))
    assert ("KNOWS", "since") in r["relation_props"]


def test_relationship_property_in_return():
    q = "MATCH (a:Person)-[r:KNOWS]->(b:Person) RETURN r.since, r.weight"
    r = sets(extract_schema(q))
    assert ("KNOWS", "since") in r["relation_props"]
    assert ("KNOWS", "weight") in r["relation_props"]


def test_relationship_property_in_inline_map():
    q = "MATCH (a:Person)-[r:KNOWS {since: 2020}]->(b:Person) RETURN a"
    r = sets(extract_schema(q))
    assert ("KNOWS", "since") in r["relation_props"]


def test_relationship_property_in_with():
    q = "MATCH (a:Person)-[r:KNOWS]->(b:Person) WITH r.since AS since RETURN since"
    r = sets(extract_schema(q))
    assert ("KNOWS", "since") in r["relation_props"]


def test_nested_foreach():
    q = (
        "MATCH (n:Person) "
        "FOREACH (x IN n.friends | "
        "  FOREACH (y IN x.tags | "
        "    CREATE (t:Tag {name: y})-[:APPLIED_TO]->(n)"
        "  )"
        ")"
    )
    r = sets(extract_schema(q))
    assert "Tag" in r["nodes"]
    assert ("Person", "friends") in r["node_props"]
    assert ("Tag", "APPLIED_TO", "Person") in r["relations"]


def test_call_subquery_with_return_variables():
    q = "CALL { MATCH (n:Person)-[r:KNOWS]->(m:Person) RETURN n, r, m } RETURN n.name, r.since, m.name"
    r = sets(extract_schema(q))
    assert ("Person", "KNOWS", "Person") in r["relations"]
    assert ("Person", "name") in r["node_props"]
    assert ("KNOWS", "since") in r["relation_props"]


def test_multiple_call_subqueries():
    q = (
        "CALL { MATCH (n:Person) RETURN n } "
        "CALL { MATCH (c:Company) RETURN c } "
        "RETURN n, c"
    )
    r = sets(extract_schema(q))
    assert "Person" in r["nodes"]
    assert "Company" in r["nodes"]


def test_using_index_hint():
    q = "MATCH (n:Person) USING INDEX n:Person(name) WHERE n.name = 'Bob' RETURN n"
    r = sets(extract_schema(q))
    assert ("Person", "name") in r["node_props"]


def test_using_join_hint():
    q = "MATCH (n:Person)-->(m:Person) USING JOIN ON n WHERE n.id = m.id RETURN n"
    r = sets(extract_schema(q))
    assert ("Person", "id") in r["node_props"]


def test_property_with_underscore():
    q = "MATCH (n:Person) RETURN n.first_name, n.last_name"
    r = sets(extract_schema(q))
    assert ("Person", "first_name") in r["node_props"]
    assert ("Person", "last_name") in r["node_props"]


def test_property_with_numbers():
    q = "MATCH (n:Person) RETURN n.addr1, n.addr2"
    r = sets(extract_schema(q))
    assert ("Person", "addr1") in r["node_props"]
    assert ("Person", "addr2") in r["node_props"]


def test_property_with_unicode():
    q = "MATCH (n:Person) RETURN n.`名前`, n.`メール`"
    r = sets(extract_schema(q))
    assert ("Person", "名前") in r["node_props"]
    assert ("Person", "メール") in r["node_props"]


def test_remove_label():
    q = "MATCH (n:Person:Employee) REMOVE n:Employee"
    r = sets(extract_schema(q))
    assert "Person" in r["nodes"]
    assert "Employee" in r["nodes"]


def test_set_remove_label_combined():
    q = "MATCH (n:Person:Employee) REMOVE n:Employee SET n:Manager"
    r = sets(extract_schema(q))
    assert r["nodes"] == {"Person", "Employee", "Manager"}


def test_distinct_does_not_affect_schema():
    q = "MATCH (n:Person) RETURN DISTINCT n.name"
    r = sets(extract_schema(q))
    assert ("Person", "name") in r["node_props"]


def test_skip_does_not_affect_schema():
    q = "MATCH (n:Person) RETURN n.name SKIP 10"
    r = sets(extract_schema(q))
    assert ("Person", "name") in r["node_props"]


def test_limit_does_not_affect_schema():
    q = "MATCH (n:Person) RETURN n.name LIMIT 10"
    r = sets(extract_schema(q))
    assert ("Person", "name") in r["node_props"]


def test_aliased_return_property():
    q = "MATCH (n:Person) RETURN n.name AS personName"
    r = sets(extract_schema(q))
    assert ("Person", "name") in r["node_props"]
    assert ("Person", "personName") not in r["node_props"]


def test_multiple_labels_on_node_in_pattern():
    q = "MATCH (a:Person)-[:KNOWS]->(b:Employee:Manager) RETURN a"
    r = sets(extract_schema(q))
    assert r["nodes"] == {"Person", "Employee", "Manager"}
    assert ("Person", "KNOWS", "Employee") in r["relations"]
    assert ("Person", "KNOWS", "Manager") in r["relations"]


def test_property_compared_to_null():
    q = "MATCH (n:Person) WHERE n.middleName IS NULL RETURN n"
    r = sets(extract_schema(q))
    assert ("Person", "middleName") in r["node_props"]


def test_property_compared_to_not_null():
    q = "MATCH (n:Person) WHERE n.email IS NOT NULL RETURN n"
    r = sets(extract_schema(q))
    assert ("Person", "email") in r["node_props"]


def test_property_in_string_function():
    q = "MATCH (n:Person) RETURN size(n.name), toUpper(n.email)"
    r = sets(extract_schema(q))
    assert ("Person", "name") in r["node_props"]
    assert ("Person", "email") in r["node_props"]


def test_property_in_math_expression():
    q = "MATCH (n:Order) RETURN n.total + n.tax AS grandTotal"
    r = sets(extract_schema(q))
    assert ("Order", "total") in r["node_props"]
    assert ("Order", "tax") in r["node_props"]


def test_property_in_starts_with():
    q = "MATCH (n:Person) WHERE n.name STARTS WITH 'A' RETURN n"
    r = sets(extract_schema(q))
    assert ("Person", "name") in r["node_props"]


def test_property_in_ends_with():
    q = "MATCH (n:Person) WHERE n.email ENDS WITH '.com' RETURN n"
    r = sets(extract_schema(q))
    assert ("Person", "email") in r["node_props"]


def test_property_in_contains():
    q = "MATCH (n:Person) WHERE n.name CONTAINS 'Bob' RETURN n"
    r = sets(extract_schema(q))
    assert ("Person", "name") in r["node_props"]


def test_property_in_in_operator():
    q = "MATCH (n:Person) WHERE n.status IN ['active', 'pending'] RETURN n"
    r = sets(extract_schema(q))
    assert ("Person", "status") in r["node_props"]


def test_variable_in_in_operator():
    q = "MATCH (n:Person) WHERE 'admin' IN n.roles RETURN n"
    r = sets(extract_schema(q))
    assert ("Person", "roles") in r["node_props"]


def test_property_in_range_comparison():
    q = "MATCH (n:Person) WHERE 18 <= n.age <= 65 RETURN n"
    r = sets(extract_schema(q))
    assert ("Person", "age") in r["node_props"]


def test_properties_on_both_nodes_in_relationship():
    q = "MATCH (a:Person {name: 'Alice'})-[:KNOWS]->(b:Person {name: 'Bob'}) RETURN a"
    r = sets(extract_schema(q))
    assert ("Person", "name") in r["node_props"]


def test_relationship_with_three_types():
    q = "MATCH (a:Person)-[r:KNOWS|FOLLOWS|BLOCKED]->(b:Person) RETURN a"
    r = sets(extract_schema(q))
    assert r["relations"] == {
        ("Person", "KNOWS", "Person"),
        ("Person", "FOLLOWS", "Person"),
        ("Person", "BLOCKED", "Person"),
    }


def test_where_with_and():
    q = "MATCH (n:Person) WHERE n.name = 'Bob' AND n.age > 30 RETURN n"
    r = sets(extract_schema(q))
    assert ("Person", "name") in r["node_props"]
    assert ("Person", "age") in r["node_props"]


def test_where_with_or():
    q = "MATCH (n:Person) WHERE n.name = 'Bob' OR n.email = 'bob@test.com' RETURN n"
    r = sets(extract_schema(q))
    assert ("Person", "name") in r["node_props"]
    assert ("Person", "email") in r["node_props"]


def test_where_with_xor():
    q = "MATCH (n:Person) WHERE n.isActive XOR n.isDeleted RETURN n"
    r = sets(extract_schema(q))
    assert ("Person", "isActive") in r["node_props"]
    assert ("Person", "isDeleted") in r["node_props"]


def test_nested_property_in_where():
    q = "MATCH (n:Person) WHERE n.address.city = 'NYC' RETURN n"
    r = sets(extract_schema(q))
    assert ("Person", "address") in r["node_props"]
    assert ("Person", "city") not in r["node_props"]


def test_nested_property_in_return():
    q = "MATCH (n:Person) RETURN n.address.zip"
    r = sets(extract_schema(q))
    assert ("Person", "address") in r["node_props"]
    assert ("Person", "zip") not in r["node_props"]


def test_variable_length_relationship_with_props():
    q = "MATCH path = (a:Person)-[r:KNOWS*2..5]->(b:Person) WHERE ALL(x IN relationships(path) WHERE x.since > 2020) RETURN a"
    r = sets(extract_schema(q))
    assert ("Person", "KNOWS", "Person") in r["relations"]
    assert ("KNOWS", "since") in r["relation_props"]
    

def test_inline_path_in_relationships_function():
    q = "MATCH (a:Person)-[r:KNOWS]->(b:Person) WHERE ALL(x IN relationships((a)-[r:KNOWS]->(b)) WHERE x.since > 2020) RETURN a"
    r = sets(extract_schema(q))
    assert ("KNOWS", "since") in r["relation_props"]


def test_unwind_with_create():
    q = "UNWIND [{name: 'Bob'}, {name: 'Alice'}] AS props CREATE (n:Person) SET n = props"
    r = sets(extract_schema(q))
    assert "Person" in r["nodes"]


def test_call_subquery_with_import():
    q = "CALL { MATCH (n:Person) RETURN n } IN TRANSACTIONS OF 100 ROWS RETURN n"
    r = sets(extract_schema(q))
    assert "Person" in r["nodes"]


def _all_tests():
    g = dict(globals())
    return [
        (name, fn)
        for name, fn in g.items()
        if name.startswith("test_") and callable(fn)
    ]


def main() -> int:
    failures = []
    tests = _all_tests()
    for name, fn in tests:
        try:
            fn()
            print(f"PASS  {name}")
        except AssertionError as e:
            print(f"FAIL  {name}: {e}")
            failures.append(name)
        except Exception:
            print(f"ERROR {name}")
            traceback.print_exc()
            failures.append(name)

    print(f"\n{len(tests) - len(failures)}/{len(tests)} passed")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
