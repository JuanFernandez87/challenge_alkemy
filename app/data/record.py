from models.registro_por_categoria import Registros_categoria 
from models.registro_por_provincia import Registros_provincia
from datetime import date
from config import db
import pandas as pd
from logger.logger_base import log

'''
    Procesar los datos conjuntos para poder generar una tabla con la siguiente información:
        Cantidad de registros totales por categoría
        Cantidad de registros totales por fuente
        Cantidad de registros por provincia y categoría
'''


def registros_por_categoria():
    try:
        engine = db.engine
        df = pd.read_sql_table('entidades', engine, columns=['id_provincia', 'categoria'])

        '''Agrupo por categoria y cuento cuantas filas tiene cada uno'''
        records = df.groupby(['categoria']).size().reset_index(name='cantidades')

        for row_index, row in records.iterrows():
            registro = Registros_categoria()
            registro.categoria = records['categoria'][row_index]
            registro.cantidad = int(records['cantidades'][row_index])
            registro.fecha_carga = date.today()
            Registros_categoria.save(registro)
    
    except Exception as e:
        log.debug(f'Ocurrio una excepcion {e}')              
    

def registros_por_provincia_y_categoria():
    try:
        engine = db.engine
        df = pd.read_sql_table('entidades', engine, columns=['id_provincia', 'provincia', 'categoria'])

        '''Obtengo un listado con las provincias de la base de datos y cuento las cantidades que tiene cada una por categorias'''
        df_filter = df.groupby("id_provincia").agg(provincia = ('provincia', 'first'),
                                                    cant_museos = ('categoria', lambda x: sum(x == 'Museo')),
                                                    cant_salas_de_cine = ('categoria', lambda x: sum(x == 'Sala de cine')),
                                                    cantidad_bibliotecas_publicas = ('categoria', lambda x: sum(x == 'Biblioteca popular'))
                                                    )
        '''Recorro el filtro y voy almacenando en la base de datos generando una fila por provincia y sus cantidades por categorias'''
        for row_index, row in df_filter.iterrows():
            registro = Registros_provincia()
            registro.provincia = df_filter['provincia'][row_index]
            registro.cantidad_museos = int(df_filter['cant_museos'][row_index])
            registro.cantidad_salas_de_cine = int(df_filter['cant_salas_de_cine'][row_index])
            registro.cantidad_bibliotecas_publicas = int(df_filter['cantidad_bibliotecas_publicas'][row_index])
            registro.fecha_carga = date.today()
            Registros_provincia.save(registro)
    
    except Exception as e:
        log.debug(f'Ocurrio una excepcion {e}')    
             