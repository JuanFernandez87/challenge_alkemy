from config import db
from sqlalchemy import Column, Integer, Date

class Registros(db.Base):
    __tablename__ = "registros"
    id = Column(Integer, primary_key=True , autoincrement=True)
    totales_categoria = Column(Integer)
    # Que es por fuente?
    totales_fuente = Column(Integer)
    provincia_categoria = Column(Integer)
    fecha_carga = Column(Date)

    def __init__(self, 
                totales_categoria=None, 
                totales_fuente=None, 
                provincia_categoria=None,
                fecha_carga=None):
        self.totales_categoria = totales_categoria
        self.totales_fuente = totales_fuente
        self.provincia_categoria = provincia_categoria
        self.fecha_carga = fecha_carga

    def save(self):
        db.session.add(self)
        db.session.commit()        