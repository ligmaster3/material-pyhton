import ee
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import geemap

ee.Authenticate()
ee.Initialize(project='geomateria')

chirps = ee.Image('image ID')
areaEstudio = ee.FeatureCollection('table ID')

# Cargar la colección de imágenes CHIRPS diaria
dataset = ee.ImageCollection('UCSB-CHG/CHIRPS/DAILY')

temperatura = dataset.select('temperature')

n_bandas = chirps.bandNames().size().getInfo()
fecha_inicio = '1994-01-01'

nombres_seq = []
for i in range(n_bandas):
    anio = fecha_inicio + (fecha_inicio.month + i) // 12
    mes = (fecha_inicio.month + i) % 12 + 1
    fecha_str = f"{anio}-{mes:02d}-01"
    nombres_seq.append('banda' + str(i))

chirps = chirps.rename(nombres_seq)
original_band_names = chirps.bandNames()

def image_from_band(band_name):
    # Seleccionar la banda individual y asignar propiedades con la fecha extraída
    img = chirps.select([band_name])
    # Extraer la parte de la fecha (se asume que band_name tiene el formato "rasterYYYY-MM")
    date_str = ee.String(band_name).slice(6)  # obtiene "YYYY-MM"
    return img.set({'label': band_name, 'date': date_str.cat('-01')})

# Convertir el ráster multibanda en una ImageCollection (para iterar en cada mes)
bands_ic = ee.ImageCollection(original_band_names.map(image_from_band))
res = 100

def resample_and_clip(image):
    # Resample bilineal y reproyecta a 100 m
    resampled = image.resample('bilinear').reproject(crs=image.projection(), scale=res)
    # Cortar (clip) al polígono del municipio
    return resampled.clip(departamento.geometry())

bands_ic = bands_ic.map(resample_and_clip)

# Definir la lista de meses como un ee.List
meses_nombres = ee.List(['ene', 'feb', 'mar', 'abr', 'may', 'jun',
                         'jul', 'ago', 'sep', 'oct', 'nov', 'dic'])

def imagen_media_mes(mes):
    # Convertir mes a número entero
    mes_int = ee.Number(mes).toInt()
    # Filtrar la colección para el mes correspondiente usando la propiedad 'system:time_start'
    imagenes_filtradas = bands_ic.filter(ee.Filter.eq('date', ee.Date.fromYMD(1994, mes, 1).format('YYYY-MM-dd')))
    
    # Calcular la media por píxel para el mes actual
    media = imagenes_filtradas.mean()
    # Calcular el índice (para acceder a la lista, se usa mes - 1)
    indice = mes_int.subtract(1).toInt()
    # Asignar la propiedad 'mes' usando el nombre correspondiente del ee.List
    media = media.set('mes', ee.String(meses_nombres.get(indice)))
    return media

# Crear una lista de números del 1 al 12 (cada uno representa un mes)
lista_meses = ee.List.sequence(1, 12)
# Mapear la función sobre la lista de meses para obtener la lista de imágenes medias mensuales
lista_imagenes = lista_meses.map(imagen_media_mes)

# Convertir la lista en una ImageCollection
coleccion_mensual = ee.ImageCollection(lista_imagenes)

# Convertir la colección a bandas
imagen_bandas = coleccion_mensual.toBands()

# Función para convertir de Kelvin a Celsius
def kelvin_celsius(imagen):
    return imagen.subtract(273.15)

# Aplicar la conversión de Kelvin a Celsius
imagen_bandas_mod = kelvin_celsius(imagen_bandas)

# Visualizar la imagen convertida en el mapa
m = geemap.Map()
parVis = {
    'min': 0,
    'max': 250,
    'palette': ['blue', 'purple', 'cyan', 'green', 'yellow', 'red']
}

m.addLayer(imagen_bandas_mod, parVis, 'Temperatura en Celsius')
m.centerObject(departamento, 8)

# Define la leyenda
legend_dict = {
    'Bajo': (0, 0, 255), 
    'Moderado': (128, 0, 128), 
    'Medio': (0, 255, 255),  
    'Alto': (0, 128, 0), 
    'Muy Alto': (255, 255, 0), 
    'Extremo': (255, 0, 0) 
}


m.add_legend(legend_title="Temperatura (°C)", legend_dict=legend_dict)

# Mostrar el mapa
m

# Configurar la exportación a Google Drive como GeoTIFF
export_task = ee.batch.Export.image.toDrive(
    image=imagen_bandas_mod,
    description='mediaMensual',
    folder='GEEExports_EACC',
    fileNamePrefix='mediaMensual',
    scale=1000, # Ajusta la escala según resolución deseada
    region=departamento.geometry(),
    fileFormat='GeoTIFF'
)
export_task.start()