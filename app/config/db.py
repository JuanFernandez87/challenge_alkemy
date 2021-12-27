from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Conexion con la base de datos
engine = create_engine('postgresql://postgres:1234@localhost:5432/Alkemy')

# Creo la session para trabajar con SQLAlchemy
Session = sessionmaker(bind=engine)
session = Session()

# Realizo el mapeo de una clase a una tabla
Base = declarative_base()