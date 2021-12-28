from data import normalize_info 

def procces(list_routes):
     # Envio las rutas a los procesos que se encargan de almacenar la información en la base de datos
     normalize_info.procces_museos(list_routes[0])    
     normalize_info.procces_cines(list_routes[1])
     normalize_info.procces_bibliotecas(list_routes[2])
