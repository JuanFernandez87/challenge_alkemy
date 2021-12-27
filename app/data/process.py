from data import normalize_info 

def procces(route_museos, route_cines, route_bibliotecas):
     # Envio las rutas a los procesos que se encargan de almacenar la información en la base de datos
     normalize_info.procces_museos(route_museos)    
     normalize_info.procces_cines(route_cines)
     normalize_info.procces_bibliotecas(route_bibliotecas)
