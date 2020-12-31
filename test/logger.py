import logging

# Create and configy logger

LOG_FORMAT = "[%(levelname)s] [%(asctime)s] - %(message)s,"
logging.basicConfig(filename='applog.log', level=logging.DEBUG, format =LOG_FORMAT, filemode='a')
logger = logging.getLogger()

logger.info('Info logger11')