import os
from pip._vendor import requests
from datetime import datetime
from logger.logger_base import log
'''
    Este script crea la carpeta para cada archivo fuente que se descarga desde el sitio.
    Recibe la URL de donde descargar el archivo fuente y la categoria (museos, salas-cine, 'bibliotecas-populares').

'''

'''
    Guardo en variables los links de los archivos fuente para enviarlo al programa encargado 
    de crear los directorios y descargar los archivos fuente que luego almacena de forma local
'''    
url_museos = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museos.csv'
url_salas_cine = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/392ce1a8-ef11-4776-b280-6f1c7fae16ae/download/cine.csv'
url_bibliotecas = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/biblioteca_popular.csv'   


def request(categoria, url):
    '''
        Si la peticion se realizo correctamente guardo el archivo fuente para luego trabajar con pandas.
    '''
    request = requests.get(url)
    if request.status_code == 200:  
        # Obtengo la fecha para la creacion de la carpeta y el archivo
        date = datetime.today().strftime('%d-%m-%Y')
        year = datetime.today().strftime('%Y')
        month = datetime.today().strftime('%B')
          
        # Carpeta año-mes
        directory = year+'-'+month
          
        # Ruta de la carpeta
        parent_dir = 'files/'+categoria+'/'
        path = os.path.join(parent_dir, directory)
            
        try:
            # Crecion de la carpeta categoria-fecha
            os.makedirs(path, exist_ok = True)
            # Ruta donde almacenar el archivo
            route = parent_dir+directory+'/'
            content = request.content
            # Nombre del archivo csv descargado
            route_file = route+categoria+'-'+date+'.csv'
            file = open(route_file, 'wb')
            file.write(content)
            file.close()
            log.debug(f'La carpeta para ' + categoria + ' se creo correctamente' )
        except Exception as e:
            log.debug(f'Ocurrio una excepcion {e}') 

    # Retorno la ruta donde se almaceno el archivo fuente
    return (route_file)  

def request_files(list_routes):
    list_routes.append(request('museos', url_museos))
    list_routes.append(request('salas-cine', url_salas_cine))
    list_routes.append(request('bibliotecas-populares', url_bibliotecas))
    return list_routes

