from config import db
from sqlalchemy import Column, Integer, String, Date, Float

class Entidad(db.Base):
    __tablename__ = "entidades"
    id = Column(Integer, primary_key=True , autoincrement=True)
    cod_localidad = Column(Integer)
    id_provincia = Column(Integer)
    id_departamento = Column(Integer)
    # Consultar si es un id o un string (museo, cine o biblioteca)
    categoria = Column(String(100))
    provincia = Column(String(100))
    localidad = Column(String(100))
    nombre = Column(String(200))
    domicilio = Column(String(100))
    codigo_postal = Column(String(50))
    numero_de_telefono = Column(String(20))
    mail = Column(String(100))
    web = Column(String(150))
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

    def save(self):
        db.session.add(self)
        db.session.commit()