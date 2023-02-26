# sending logs to server
import logging
from logging.handlers import SysLogHandler
import time

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(SysLogHandler(address=('192.168.2.206', 514)))

for i in range(20):
    logger.info("Hello World!!!")
    time.sleep(1)

