from config import db
from sqlalchemy import Column, Integer, Date, String

class Registros_provincia(db.Base):
    __tablename__ = "registro_por_provincia"
    id = Column(Integer, primary_key=True , autoincrement=True)
    provincia = Column(String(70))
    cantidad_museos = Column(Integer)    
    cantidad_salas_de_cine = Column(Integer)
    cantidad_bibliotecas_publicas = Column(Integer)            
    fecha_carga = Column(Date)

    def __init__(self, 
                provincia=None,
                categoria=None, 
                cantidad=None, 
                fecha_carga=None):
        self.provincia = provincia                
        self.categoria = categoria
        self.cantidad = cantidad
        self.fecha_carga = fecha_carga

    def save(self):
        db.session.add(self)
        db.session.commit()   
        