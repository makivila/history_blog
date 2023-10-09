from logging import Logger, FileHandler, Formatter, StreamHandler
import logging
import os

# from dotenv import load_dotenv


def create_logger() -> Logger:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    log_handler = StreamHandler()
    log_handler.setFormatter(Formatter(fmt="%(asctime)s: %(levelname)s %(message)s"))
    logger.addHandler(log_handler)

    return logger
