import logging.config

logging.config.fileConfig("./logging.conf")
logger = logging.getLogger("spider")

logger.exception("this is sha a ")
