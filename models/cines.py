from sqlalchemy import Column, Integer, String, Date
from config.base import Base

class Cines(Base):
    __tablename__ = "cines"
    id = Column(Integer, primary_key=True , autoincrement=True)
    provincia = Column(String(30))
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
            self.cantidad_pantallas = cantidad_pantallas
            self.cantidad_butacas = cantidad_butacas
            self.cantidad_espacios_incaa = cantidad_espacios_incaa
            self.fecha_carga = fecha_carga