import logging


logger = logging.getLogger('logger')
format = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
lf = logging.FileHandler('../file.log', mode='w')

lf.setFormatter(format)
logger.addHandler(lf)