import logging as logger

logger.basicConfig(level=logger.DEBUG, datefmt='%I:%M:%S %p',
                   format='%(asctime)s: %(levelname)s [%(filename)s]: %(lineno)s %(message)s',
                   handlers=[logger.FileHandler(
                       'capa_datos.log'), logger.StreamHandler()]
                   )

if __name__ == '__main__':
    logger.debug('Hola!')
