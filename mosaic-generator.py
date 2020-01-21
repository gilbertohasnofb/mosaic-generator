#!/usr/bin/env python3
# Author: Gilberto Agostinho <gilbertohasnofb@gmail.com>
# https://github.com/gilbertohasnofb/mosaic-generator

from PIL import Image, ImageDraw, ImageFont
import os
import random


def get_images(input_folder):
    """Reads input images
    """
    source_images = []
    if not input_folder.endswith('/'):
        input_folder += '/'
    for filename in os.listdir(input_folder):
        if filename.endswith('.jpg'):
            source_images.append(input_folder + filename)
    return source_images
    

def generate_mosaic(source_images,
                    n_columns,
                    n_rows,
                    border=0,
                    border_colour=(255, 255, 255),
                    randomise=False,
                    output_folder='./'):
    """Creates a random mosaic from input images
    """
    
    width, heigth = Image.open(source_images[0]).size
    mosaic_width = width * n_columns + border * (n_columns + 1)
    mosaic_heigth = heigth * n_rows + border * (n_rows + 1)
    image = Image.new('RGB',
                      (mosaic_width, mosaic_heigth),
                      color=border_colour,  # white background
                      )

    if randomise:
        random.shuffle(source_images)
        
    for number, image_filename in enumerate(source_images):
        position_x = (number % n_columns) * width \
                   + border * (number % n_columns + 1)
        position_y = (number // n_columns) * heigth \
                   + border * (number // n_columns + 1)
        image.paste(
            Image.open(image_filename),
            (position_x, position_y),
            )

    if not output_folder.endswith('/'):
        output_folder += '/'
    image.save(output_folder + 'mosaic.jpg',
               format='JPEG',
               subsampling=0,
               quality=100,
               )


def main():
    n_columns = 6  # number of columns of images 
    n_rows = 7  # number of rows of images 
    border = 50  # in pixels; use 0 for no border
    border_colour = (255, 255, 255)  # rgb value
    input_folder = './input'
    output_folder = './'
    randomise = True  # randomises the order of the input images
    source_images = get_images(input_folder)
    generate_mosaic(source_images, 
                    n_columns,
                    n_rows,
                    border,
                    border_colour,
                    randomise,
                    output_folder,
                    )


if __name__ == '__main__':
    main()
