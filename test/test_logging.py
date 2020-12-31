import logging

logging.basicConfig(format='%(asctime)-24s %(levelname)-7s %(filename)-15s %(lineno)05d %(message)s', level=logging.DEBUG)
logger = logging.getLogger('tcpserver')
logger.error("Protocol problem: %s", "connecction reset", extra={"clientip": "192.168.0.1", "user": "fbloggs"})
logger.warning("Protocol problem: %s", "connecction reset", extra={"clientip": "192.168.0.1", "user": "fbloggs"})
logger.debug("Protocol problem: %s", "connecction reset", extra={"clientip": "192.168.0.1", "user": "fbloggs"})
logger.info("Protocol problem: %s", "connecction reset", extra={"clientip": "192.168.0.1", "user": "fbloggs"})
