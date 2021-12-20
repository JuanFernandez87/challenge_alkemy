import os
from pip._vendor import requests
from datetime import datetime
'''
    Este script crea la carpeta para cada archivo fuente que se descarga desde el sitio.
    Recibe la URL de donde descargar el archivo fuente y la categoria (museos, salas-cine, 'bibliotecas-populares').

'''
def request(categoria, url_museos):
    '''
        Si la peticion se realizo correctamente guardo el archivo fuente para luego trabajar con pandas.
    '''
    request = requests.get(url_museos)
    if request.status_code == 200:  
        # Obtengo la fecha para la creacion de la carpeta y el archivo
        date = datetime.today().strftime('%d-%m-%Y')
        year = datetime.today().strftime('%Y')
        month = datetime.today().strftime('%B')
          
        # Carpeta año-mes
        directory = year+'-'+month
          
        # Ruta de la carpeta
        parent_dir = 'files/'+categoria+'/'
            
        # Ruta
        path = os.path.join(parent_dir, directory)
            
        try:
            # Crecion de la carpeta categoria-fecha
            os.makedirs(path, exist_ok = True)
            # Ruta donde almacenar el archivo
            route = parent_dir+directory+'/'
            content = request.content
            # Nombre del archivo csv descargado
            name_file = route+categoria+'-'+date+'.csv'
            file = open(name_file, 'wb')
            file.write(content)
            file.close()
        except OSError as error:
            print("La carpeta '%s' no se pudo crear")        
