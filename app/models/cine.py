from config import db
from sqlalchemy import Column, Integer, String, Date

class Cines(db.Base):
    __tablename__ = "cines"
    id = Column(Integer, primary_key=True , autoincrement=True)
    provincia = Column(String(50))
    cantidad_pantallas = Column(Integer)
    cantidad_butacas = Column(Integer)
    cantidad_espacios_incaa = Column(Integer)
    fecha_carga = Column(Date)


    def __init__(self,
                provincia=None, 
                cantidad_pantallas=None, 
                cantidad_butacas=None, 
                cantidad_espacios_incaa=None,
                fecha_carga=None): 
            self.provincia = provincia
            self.cantidad_pantallas = 0
            self.cantidad_butacas = 0
            self.cantidad_espacios_incaa = 0
            self.fecha_carga = fecha_carga


    def save(self):
        db.session.add(self)
        db.session.commit()   
                 