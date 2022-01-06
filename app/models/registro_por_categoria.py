from config import db
from sqlalchemy import Column, Integer, Date, String

class Registros_categoria(db.Base):
    __tablename__ = "registro_por_categoria"
    id = Column(Integer, primary_key=True , autoincrement=True)
    categoria = Column(String(30))
    cantidad = Column(Integer)    
    fecha_carga = Column(Date)

    def __init__(self, 
                categoria=None, 
                cantidad=None, 
                fecha_carga=None):
        self.categoria = categoria
        self.cantidad = cantidad
        self.fecha_carga = fecha_carga

    def save(self):
        db.session.add(self)
        db.session.commit()   
             