#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Nome do script: mult_extract_tiles.py
Autor: Tasso Moraes
Data de criação: 13/01/2023

Descrição:
    Este script aplica um outro script (o extract_tiles_from_wsi_openslide.py
que se encontra na pasta cli do repositório do QuickAnnotator) em multiplas 
imagens WSI dividindo-as em patches de dimensões especificadas. Também cria 
as pastas de destino caso essas não tenham sido criadas previamente. Para que 
ele funcione é ncessário que o arquivo esteja na pasta 'cli' que se encontra 
na pasta QuickAnnotator-main. 

Uso:
python mult_extract_tiles.py -w wsi_path (input) -s patch_size -p patch_path (output)

Exemplo:
python mult_extract_tiles.py -w r"C:\Users\IA\Pictures\Datasets\TCGA\WSI\Carcinoma diffuse" -s 8192 -p r"C:\Users\IA\Pictures\Datasets\TCGA\Patches\Carcinoma diffuse" -t "Gastric Antrum"
"""


# Nesccery libraries

# mask binarization
import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np

# image ROI split
import os
import argparse
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image, ImageOps


# Parameters passed on terminal
parser = argparse.ArgumentParser(description='Extrac tiles from multple WSI images')
parser.add_argument('-w', '--wsi_path', help="WSI's path Directories", default="./input", type=str)
parser.add_argument('-s', '--patch_size', help="openslide level to use", default=8192, type=int)
parser.add_argument('-p', '--patch_path', help="Patches's path directories", default="./output", type=str)
parser.add_argument('-t', '--type', help='Especific type of cancer (folder name)', default=None, type=str)
args = parser.parse_args()

wsi_path = args.wsi_path
patches_path = args.patches_path
patch_size = args.patch_size
especific_type_folder = args.type

# list the folders
for fold in os.listdir(wsi_path):
    especific_type_folder = 'Gastric Antrum'
    type_path = os.path.join(wsi_path,fold + '\\' + especific_type_folder)
    
    #list the files insde each folder
    for file in os.listdir(type_path):
        print(file)
        
        # create a folder with file name
        file_path = os.path.join(type_path, file)
        dst_folder_path = file_path.replace('WSI', 'Patches')[:-4]
        os.makedirs(dst_folder_path, exist_ok=True)
        
        # make patches
        outdir = dst_folder_path
        input_pattern = file_path
        cli_folder = r"C:\Users\IA\Documents\QuickAnnotator-main\cli"
        os.system("python " + cli_folder + "\extract_tiles_from_wsi_openslide.py -p " + str(patch_size) + " -o \"" + outdir + "\" \"" + input_pattern + "\"")