import pandas as pd
from datetime import date
from models.cine import Cines
from logger.logger_base import log
'''
    Procesar la información de cines para poder crear una tabla que contenga:
        Provincia -> IdProvincia
        Cantidad de pantallas -> Pantallas
        Cantidad de butacas -> Butacas
        Cantidad de espacios INCAA -> espacio_INCAA
'''      


def process(fname):
    try:
        '''Leo el archivo fuente de la ruta''' 
        df = pd.read_csv(fname)

        '''Agrupo la información por provincia y guardo los datos solicitados'''
        df_filter = df.groupby("IdProvincia").agg(provincia = ('Provincia', 'first'),
                                            cant_pantallas = ('Pantallas', 'sum'),
                                            cant_butacas = ('Butacas', 'sum'),                                             
                                            cant_incaa = ('espacio_INCAA', lambda x: sum(x == 'si') + sum(x == 'SI'))
                                            )

        for row_index, row in df_filter.iterrows():
            cine = Cines()
            cine.provincia = df_filter['provincia'][row_index]
            cine.cantidad_pantallas = int(df_filter['cant_pantallas'][row_index])
            cine.cantidad_butacas = int(df_filter['cant_butacas'][row_index])
            cine.cantidad_espacios_incaa = int(df_filter['cant_incaa'][row_index])
            cine.fecha_carga = date.today()
            Cines.save(cine)

        log.debug(f'La informacion de los cines se almaceno correctamente en la tabla cines') 

    except Exception as e:
        log.debug(f'Ocurrio una excepcion {e}')   
                   