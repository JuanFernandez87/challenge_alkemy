from data import normalize_info 
from data import cines_info
from data import record

def process(list_routes):
     '''Envio las rutas a los procesos que se encargan de almacenar la información en la base de datos'''
     normalize_info.process_museos(list_routes[0])    
     normalize_info.process_cines(list_routes[1])
     normalize_info.process_bibliotecas(list_routes[2])

     
def process_cines(list_routes):
     cines_info.process(list_routes)


def process_record():
     record.registros_por_categoria()
     record.registros_por_provincia_y_categoria()
