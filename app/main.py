from config import db
from models import cine, entidad, registro
from request import request
from data import process 

'''
    Guardo en variables los links de los archivos fuente para enviarlo al programa encargado 
    de crear los directorios y descargar los archivos fuente que luego almacena de forma local
'''    
url_museos = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museos.csv'
url_salas_cine = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/392ce1a8-ef11-4776-b280-6f1c7fae16ae/download/cine.csv'
url_bibliotecas = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/biblioteca_popular.csv'   

if __name__ == '__main__':
    # Borro todas las tables si ya estan creadas
    db.Base.metadata.drop_all(db.engine)

    # Creo las tablas con las clases guardades en Base
    db.Base.metadata.create_all(db.engine, checkfirst=True)

    '''
        Envio los nombres de la categoria para crear las carpetas y los links para descargar los archivos fuente. 
        Guardo las rutas en variables para enviarselas al proceso encargado de almacenar en la base de datos
    '''    
    route_museos = request.request('museos', url_museos)
    route_cines = request.request('salas-cine', url_salas_cine)
    route_bibliotecas = request.request('bibliotecas-populares', url_bibliotecas)

    # Envio las rutas de los archivos para almacenar en la base de datos
    process.procces(route_museos, route_cines, route_bibliotecas)