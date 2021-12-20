from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from config.base import Base
from request import request

# Conexion con la base de datos
engine = create_engine('postgresql://postgres:1234@localhost:5432/Alkemy')

Session = sessionmaker(bind=engine)
session = Session()

if __name__ == '__main__':
    # Borro todas las tables si ya estan creadas
    Base.metadata.drop_all(engine)
    # Creo las tablas con las clases guardades en Base
    Base.metadata.create_all(engine, checkfirst=True)
    '''
        Guardo en variables los links de los archivos fuente para enviarlo al script encargado 
        de crear los directorios y descargar los archivos fuente que luego almacena de forma local
    '''    
    url_museos = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museos.csv'
    url_salas_cine = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/392ce1a8-ef11-4776-b280-6f1c7fae16ae/download/cine.csv'
    url_bibliotecas = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/biblioteca_popular.csv'
    request('museos', url_museos)
    request('salas-cine', url_salas_cine)
    request('bibliotecas-populares', url_bibliotecas)