from sqlalchemy import Column, Integer, String, Date
from config.base import Base

class Entidad(Base):
    __tablename__ = "entidades"
    id = Column(Integer, primary_key=True , autoincrement=True)
    cod_localidad = Column(Integer)
    id_provincia = Column(Integer)
    id_departamento = Column(Integer)
    # Consultar si es un id o un string (museo, cine o biblioteca)
    categoría = Column(String(30))
    provincia = Column(String(30))
    localidad = Column(String(30))
    nombre = Column(String(30))
    domicilio = Column(String(30))
    codigo_postal = Column(Integer)
    numero_de_telefono = Column(Integer)
    mail = Column(String(30))
    web = Column(String(30))
    fecha_carga = Column(Date)

    def __init__(self, 
                cod_localidad=None, 
                id_provincia=None, 
                id_departamento=None, 
                categoria=None, 
                provincia=None, 
                localidad=None, 
                nombre=None, 
                domicilio=None, 
                codigo_postal=None, 
                numero_de_telefono=None, 
                mail=None, 
                web=None,
                fecha_carga=None):
        self.cod_localidad = cod_localidad
        self.id_provincia = id_provincia
        self.id_departamento = id_departamento
        self.categoría = categoria
        self.provincia = provincia
        self.localidad = localidad
        self.nombre = nombre
        self.domicilio = domicilio
        self.codigo_postal = codigo_postal
        self.numero_de_telefono = numero_de_telefono
        self.mail = mail
        self.web = web
        self.fecha_carga = fecha_carga

