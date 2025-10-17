import logging

logging.basicConfig(
    filename='logs.log',
    encoding='utf-8',
    format='%(levelname)s:%(message)s',
    level=logging.DEBUG
    )

logging.info("Hola")