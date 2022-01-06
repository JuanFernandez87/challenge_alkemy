from config import db
from request import request
from data import process 
from logger.logger_base import log

if __name__ == '__main__':
    '''
        Si la conexión se realizo correctamente creo las tablas,
        descargo los archivos y guardo los datos en la base
    '''   
    
    try:        
        '''Instancio engine como lista para poder obtener la conexion por referencia'''
        engine = []
        
        '''
            Conecto con la base de datos, borro todas las tables si ya estan creadas 
            y por ultimo creo las tablas con las clases guardades en Base
        '''
        db.connect(engine)        
        db.Base.metadata.drop_all(engine[0])
        db.Base.metadata.create_all(engine[0], checkfirst=True)
                 
        '''Guardo las rutas en una lista para enviarselas al proceso encargado de almacenar en la base de datos'''
        list_routes = []
        request.request_files(list_routes)  

        '''Envio la lista de rutas de los archivos para almacenar en la base de datos'''
        process.process(list_routes)

        '''Envio la ruta de los cines para procesar la información'''
        process.process_cines(list_routes[1])

        '''Llamo a la funcion que procesa los datos conjuntos'''
        process.process_record()

        log.debug(f'El programa se ejecuto correctamente') 
        
    except Exception as e:
        log.debug(f'Ocurrio una excepcion {e}')  
        