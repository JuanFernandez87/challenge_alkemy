import logging as log

log.basicConfig(level=log.DEBUG,
                # muestra fecha y hora, el nivel de error (en este caso esta seteado en debug), el archivo donde muestra el error y por ultimo la linea
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p')

if __name__ == '__main__':
    log.debug('ERROR')