import logging

logger=logging.getLogger('gurgaon_prop')
logger.setLevel('ERROR')

console_handler=logging.StreamHandler()
console_handler.setLevel('ERROR')

file_handler=logging.FileHandler('error.log')
file_handler.setLevel('ERROR')

formatter=logging.Formatter(f'%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)
                         

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)