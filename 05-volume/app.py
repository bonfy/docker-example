# coding: utf-8

import time
import logging

logger = logging.getLogger(__name__)
logger.info("Start print log")
logging.basicConfig(filename='/log/log.log', level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


if __name__ == "__main__":
    i = 0
    while True:
        # print("Run func {} ...".format(i))
        logger.info("Run func {} ...".format(i))
        time.sleep(1)
        i += 1