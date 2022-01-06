from pip._vendor.requests.sessions import session
from sqlalchemy import create_engine
from sqlalchemy.orm.session import Session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from decouple import config
from logger.logger_base import log
import sys

DEBUG = config('DEBUG', default=False, cast=bool)
PSQL_HOST = config('PSQL_HOST', default='localhost')
PSQL_DB = config('PSQL_DB')
PSQL_USER = config('PSQL_USER')
PSQL_PASS = config('PSQL_PASS')
PSQL_PORT = config('PSQL_PORT', default=25, cast=int)

'''Realizo el mapeo de una clase a una tabla'''
Base = declarative_base()
engine = create_engine(f'postgresql://{PSQL_USER}:{PSQL_PASS}@{PSQL_HOST}:{PSQL_PORT}/{PSQL_DB}')
Session = sessionmaker(bind=engine)     
session = Session()
 

def connect(engine):
    try: 
        '''Conexion con la base de datos'''
        engine.append(create_engine(f'postgresql://{PSQL_USER}:{PSQL_PASS}@{PSQL_HOST}:{PSQL_PORT}/{PSQL_DB}'))
        engine[0].connect()  
        log.debug(f'La conexion se realizo correctamente') 
        return engine            
    except Exception as e:
        log.debug(f'Ocurrio una excepcion en la conexion a la base de datos {e}')  
        sys.exit()
  