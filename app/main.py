from config import db
from models import cine, entidad, registro
from request import request
from data import process 
from logger.logger_base import log

if __name__ == '__main__':
    '''
        Si la conexión se realizo correctamente creo las tablas,
        descargo los archivos y guardo los datos en la base
    '''   
    
    try:        
        # Instancio engine como lista para poder obtener la conexion por referencia
        engine = []
        
        # Conexion con la base de datos
        db.connect(engine)

        # Borro todas las tables si ya estan creadas
        db.Base.metadata.drop_all(engine[0])

        # Creo las tablas con las clases guardades en Base
        db.Base.metadata.create_all(engine[0], checkfirst=True)
                 
        # Guardo las rutas en una lista para enviarselas al proceso encargado de almacenar en la base de datos
        list_routes = []
        request.request_files(list_routes)  

        # Envio la lista de rutas de los archivos para almacenar en la base de datos
        process.procces(list_routes)

        log.debug(f'El programa se ejecuto correctamente') 
        
    except Exception as e:
        log.debug(f'Ocurrio una excepcion {e}')  