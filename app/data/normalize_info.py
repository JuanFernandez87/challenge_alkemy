import pandas as pd
from datetime import date
from models.entidad import Entidad

def procces_museos(fname):
    # Leo el archivo fuente de la ruta 
    df = pd.read_csv(fname, encoding='latin-1')

    # Guardo la información solicitada
    for row_index, row in df.iterrows():
        entidad = Entidad()
        entidad.cod_localidad = int(df['localidad_id'][row_index])
        entidad.id_provincia = int(df['provincia_id'][row_index])
        entidad.id_departamento = int(df['espacio_cultural_id'][row_index])
        entidad.categoria = 'Museo'
        entidad.provincia = df['provincia'][row_index]
        entidad.localidad = df['localidad'][row_index]
        entidad.nombre = df['nombre'][row_index]
        entidad.domicilio = df['direccion'][row_index]
        entidad.codigo_postal = df['codigo_postal'][row_index]
        entidad.numero_de_telefono = df['telefono'][row_index]
        entidad.mail = df['mail'][row_index]
        entidad.web = df['web'][row_index]
        entidad.fecha_carga = date.today()
        Entidad.save(entidad)   

def procces_cines(fname):
    # Leo el archivo fuente de la ruta 
    df = pd.read_csv(fname, encoding='latin-1')

    # Guardo la información solicitada
    for row_index, row in df.iterrows():
        entidad = Entidad()
        entidad.cod_localidad = int(df['Cod_Loc'][row_index])
        entidad.id_provincia = int(df['IdProvincia'][row_index])
        entidad.id_departamento = int(df['IdDepartamento'][row_index])
        entidad.categoria = df['CategorÃ­a'][row_index]
        entidad.provincia = df['Provincia'][row_index]
        entidad.localidad = df['Localidad'][row_index]
        entidad.nombre = df['Nombre'][row_index]
        entidad.domicilio = df['DirecciÃ³n'][row_index]
        if df['CP'][row_index]:
            try:
                entidad.codigo_postal = str(df['CP'][row_index])
            except:
                print('Error CP')
        if df['TelÃ©fono'][row_index]:
            try:
                entidad.numero_de_telefono = df['TelÃ©fono'][row_index]
            except:
                print('Error telefono')
        entidad.mail = df['Mail'][row_index]
        entidad.web = df['Web'][row_index]
        entidad.fecha_carga = date.today()
        Entidad.save(entidad)         

def procces_bibliotecas(fname):
    # Leo el archivo fuente de la ruta 
    df = pd.read_csv(fname, encoding='latin-1')

    # Guardo la información solicitada
    for row_index, row in df.iterrows():
        entidad = Entidad()
        entidad.cod_localidad = int(df['Cod_Loc'][row_index])
        entidad.id_provincia = int(df['IdProvincia'][row_index])
        entidad.id_departamento = int(df['IdDepartamento'][row_index])
        entidad.categoria = df['CategorÃ­a'][row_index]
        entidad.provincia = df['Provincia'][row_index]
        entidad.localidad = df['Localidad'][row_index]
        entidad.nombre = df['Nombre'][row_index]
        entidad.domicilio = df['Domicilio'][row_index]
        if df['CP'][row_index]:
            try:
                entidad.codigo_postal = str(df['CP'][row_index])
            except:
                print('Error CP')
        if df['TelÃ©fono'][row_index]:
            try:
                entidad.numero_de_telefono = df['TelÃ©fono'][row_index]
            except:
                print('Error telefono')
        entidad.mail = df['Mail'][row_index]
        entidad.web = df['Web'][row_index]
        entidad.fecha_carga = date.today()
        Entidad.save(entidad)           