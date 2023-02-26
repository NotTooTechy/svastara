import logging
from logging.handlers import SysLogHandler
import socket

rootLogger = logging.getLogger('')
rootLogger.setLevel(logging.DEBUG)

handler = SysLogHandler(address=("192.168.2.206", 514))#, socktype=socket.SOCK_DGRAM)
rootLogger.addHandler(handler)
rootLogger.debug("here")
rootLogger.warning("here")

