#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Nome do script: image_mask_split.py
Autor: Tasso Moraes
Data de criação: 13/01/2023

Descrição:
     

Uso:
python mult_extract_tiles.py -w wsi_path (input) -s patch_size -p patch_path (output)

Exemplo:
python mult_extract_tiles.py -w r"C:\Users\IA\Pictures\Datasets\TCGA\WSI\Carcinoma diffuse" -s 8192 -p r"C:\Users\IA\Pictures\Datasets\TCGA\Patches\Carcinoma diffuse"
"""

# Nesccery libraries

# image ROI split
import glob
from functions.image_utils import split

# pront arguments
import argparse


# cmd armuments 
parser = argparse.ArgumentParser(description='Split image into patches acording to the corresponding mask')
parser.add_argument('-i', '--image', help="Images folder path. E.g. C/WSI/imges", default='./images', type=str)
parser.add_argument('-m', '--mask', help="Masks folder path. E.g. C/WSI/masks", default='./masks', type=str)
parser.add_argument('-p', '--patch', help="Folder path where the patches are going to be saved. This folder must to have a folder named 'images' and another one named 'masks' inside it. E.g. C/WSI/patch", default="./patches", type=str)

args = parser.parse_args()
print(f"args: {args}")
print(f"USER: Starting make patches for {args.patch}", flush=True)
        

inp_img_dir = args.image
inp_msk_dir = args.mask 
out_dir = args.patch
height = 256
width = 256
start_num = 1


input_images_list = glob.glob(inp_img_dir + '/*.png')
input_masks_list = glob.glob(inp_msk_dir + '/*.png')
split(inp_img_dir, inp_msk_dir, out_dir, height, width, start_num)



