#!/usr/bin/env python3
"""
Script para extraer las visualizaciones originales del notebook de EDA
y guardarlas como imágenes para su uso en la presentación.
"""

import os
import nbformat
import base64
from nbconvert.preprocessors import ExecutePreprocessor
import re
from PIL import Image
import io
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def extract_images_from_notebook(notebook_path, output_dir):
    """
    Extrae todas las imágenes generadas en un notebook de Jupyter
    y las guarda en el directorio especificado.
    """
    # Crear directorio de salida si no existe
    os.makedirs(output_dir, exist_ok=True)
    
    # Leer el notebook
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    
    # Contador para nombrar las imágenes
    img_count = 0
    
    # Iterar sobre las celdas del notebook
    for cell in nb.cells:
        if cell.cell_type == 'code' and 'outputs' in cell:
            for output in cell.outputs:
                # Buscar datos de imagen en la salida
                if 'data' in output and 'image/png' in output.data:
                    img_count += 1
                    img_data = output.data['image/png']
                    img_bytes = base64.b64decode(img_data)
                    
                    # Guardar la imagen
                    img_path = os.path.join(output_dir, f'original_viz_{img_count:03d}.png')
                    with open(img_path, 'wb') as img_file:
                        img_file.write(img_bytes)
                    
                    print(f"Imagen guardada: {img_path}")
    
    return img_count

def main():
    # Ruta al notebook de EDA
    notebook_path = 'EDA_homicidios.ipynb'
    
    # Directorio donde se guardarán las imágenes
    output_dir = 'presentacion_ejecutiva/images/original_visualizations'
    
    # Extraer las imágenes
    num_images = extract_images_from_notebook(notebook_path, output_dir)
    
    print(f"\nSe extrajeron {num_images} visualizaciones originales del notebook de EDA.")
    print(f"Las imágenes se guardaron en: {output_dir}")
    
    # Crear un archivo HTML que muestre todas las imágenes extraídas
    create_visualization_gallery(output_dir)

def create_visualization_gallery(image_dir):
    """
    Crea una galería HTML con todas las visualizaciones originales.
    """
    html_path = os.path.join(os.path.dirname(image_dir), 'original_visualizations.html')
    
    # Obtener la lista de imágenes
    images = [f for f in os.listdir(image_dir) if f.endswith('.png')]
    images.sort()
    
    # Crear el contenido HTML
    html_content = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Visualizaciones Originales del Análisis de Datos</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        h1 {
            color: #333;
            text-align: center;
            margin-bottom: 30px;
        }
        .gallery {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(400px, 1fr));
            gap: 20px;
        }
        .viz-container {
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            padding: 15px;
        }
        .viz-container img {
            width: 100%;
            height: auto;
            border: 1px solid #eee;
        }
        .viz-title {
            margin-top: 10px;
            font-weight: bold;
        }
        .intro {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 30px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
    </style>
</head>
<body>
    <h1>Visualizaciones Originales del Análisis de Datos</h1>
    
    <div class="intro">
        <p>Esta galería muestra las visualizaciones originales generadas durante el análisis exploratorio de datos (EDA) 
        del proyecto de siniestros viales. Estas visualizaciones se basan en los datos reales analizados y representan 
        los hallazgos auténticos del proyecto.</p>
        
        <p>Estas visualizaciones complementan los videos animados de la presentación ejecutiva, proporcionando el 
        respaldo técnico y la evidencia empírica de los patrones y tendencias identificados.</p>
    </div>
    
    <div class="gallery">
"""
    
    # Agregar cada imagen a la galería
    for i, img_file in enumerate(images):
        img_path = f"original_visualizations/{img_file}"
        html_content += f"""
        <div class="viz-container">
            <img src="{img_path}" alt="Visualización {i+1}">
            <div class="viz-title">Visualización {i+1}: {img_file.replace('original_viz_', '').replace('.png', '')}</div>
        </div>
"""
    
    # Cerrar el HTML
    html_content += """
    </div>
</body>
</html>
"""
    
    # Guardar el archivo HTML
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"Galería de visualizaciones creada: {html_path}")

if __name__ == "__main__":
    main()
