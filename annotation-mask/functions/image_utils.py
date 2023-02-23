import os
from utils import dir_create, crop
from PIL import Image, ImageOps
import numpy as np
import cv2 as cv
import sys

# Extracting ROI using a mask
def split(inp_img_dir, inp_msk_dir, out_dir, height, width, start_num):
    
    image_dir = os.path.join(out_dir, 'images')
    mask_dir = os.path.join(out_dir, 'masks')
    
    # Create directories
    dir_create(out_dir)
    dir_create(image_dir)
    dir_create(mask_dir)
    
    # List of images in input directory
    img_list = [f for f in
                os.listdir(inp_img_dir)
                if os.path.isfile(os.path.join(inp_img_dir, f))]
    
    file_num = 0
    
    for infile in img_list:
        # a list to save the k indexes of masks that probably don't represent a tumor
        non_tumor_list = []
        
        infile_path = os.path.join(inp_msk_dir, infile[:-4] + '_QA-mask_bin.png')

        for k, piece in enumerate(crop(infile_path, height, width), start_num):
            # Create a white image
            msk = Image.new('RGB', (height, width), 255)
            # Paste the mask on the created white image
            msk.paste(piece)
            # Transform the 3 chanels imagem into a 1 chanel image
            msk = ImageOps.grayscale(msk)
            # Create the mask name with its path
            msk_path = os.path.join(mask_dir, infile.split('.')[0] + '_' + str(k).zfill(5) + '.png')
            
            # Check if the mask correspond to a tumor piece

            # take the number of white pixels
            white_pixels = cv.countNonZero(np.asarray(msk))
            # percentage of white pixels
            wpxl_percent = (white_pixels / (width*height))*100
            if wpxl_percent > 20:
                msk.save(msk_path) 
            else:
                non_tumor_list.append(k) # create a list of non tumor images
              
        infile_path = os.path.join(inp_img_dir, infile)
        for k, piece in enumerate(crop(infile_path, height, width), start_num):
            # only save tumors image
            if k not in non_tumor_list:
                img = Image.new('RGB', (height, width), 255)
                img.paste(piece)
                img_path = os.path.join(image_dir, infile.split('.')[0] + '_' + str(k).zfill(5) + '.png')
                img.save(img_path)
        
        file_num += 1
        sys.stdout.write("\rFile %s was processed." % file_num)
        sys.stdout.flush()