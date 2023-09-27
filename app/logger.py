from logging import Logger, FileHandler, Formatter
import logging


def create_logger() -> Logger:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    log_handler = FileHandler(filename="C:\python\history_blog\logs\history_blog.log")
    log_handler.setFormatter(Formatter(fmt="%(asctime)s: %(levelname)s %(message)s"))
    logger.addHandler(log_handler)

    return logger
