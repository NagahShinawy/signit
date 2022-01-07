"""
logs
"""
import logging
from logging import handlers

# 1- setup logging config
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


# adding log format

format_ = logging.Formatter(
    "[%(asctime)s] [%(process)d] [%(levelname)s] [%(pathname)s:%(lineno)s] [%(message)s]",
    datefmt="%d/%b/%Y %H:%M:%S",
)


# for console logging [console handle ch]
ch = logging.StreamHandler()
ch.setFormatter(format_)
logger.addHandler(ch)

# for file logging [file handler fh]
fh = handlers.RotatingFileHandler("logs.log", maxBytes=(1048576 * 5), backupCount=7)
fh.setFormatter(format_)
logger.addHandler(fh)

