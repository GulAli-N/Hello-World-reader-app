import logging
import os
import pprint

logging.basicConfig(filename='gul.log', filemode='a', format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s', datefmt='%d-%m-%Y %H:%M:%S', level=logging.DEBUG)

gul = os.environ['GUL']

pprint("GUL:", gul)

logging.info('Hello World'
