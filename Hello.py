import logging
import os


# Logging information
logging.basicConfig(filename='gul.log', format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p', level=logging.INFO)

# validation
if "A_VARIABLE" in os.environ: 
    print: "Validated"
    logging.info("The environment variable has been imported")
else: 
    print: "Environment variable missing"
