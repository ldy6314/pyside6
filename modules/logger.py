import logging
from logging.handlers import RotatingFileHandler


def get_logger(filename,
               max_bytes=1024*1024,
               backup_count=3,
               header_fmt='%(filename)s-[%(asctime)s][%(levelname)s]%(message)s',
               time_fmt='%Y-%m-%d %H:%M:%S'):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    fh = RotatingFileHandler(
        filename=filename,
        maxBytes=max_bytes,
        backupCount=backup_count
    )
    fmt = logging.Formatter(header_fmt, time_fmt)
    fh.setFormatter(fmt)
    logger.addHandler(fh)
    return logger

