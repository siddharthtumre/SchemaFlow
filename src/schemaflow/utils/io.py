import os
import logging

hr_string = "-" * 50

def setup_logger(log_filepath):
    # Ensure directory exists
    os.makedirs(os.path.dirname(log_filepath), exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler(log_filepath, mode="a"),
            logging.StreamHandler()
        ]
    )

    logger = logging.getLogger("aiir")
    logger.info(hr_string)
    logger.info(f"Logger initialized. Log file: {log_filepath}")
    return logger