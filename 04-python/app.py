# coding: utf-8

import time
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG) 

fh = logging.FileHandler(filename='log.log', mode='a')
fh.setLevel(logging.INFO)

ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)

formatter = logging.Formatter("%(asctime)s - %(levelname)s: %(message)s")
fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)

if __name__ == "__main__":
    i = 0
    while True:
        # print("Run func {} ...".format(i))
        logger.info("Run func {} ...".format(i))
        logger.debug("Debug func {} ...".format(i))
        logger.warning("Warn func {} ...".format(i))
        time.sleep(1)
        i += 1