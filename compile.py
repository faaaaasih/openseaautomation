import createimage
import traitclass
from PIL import Image
from IPython.display import display
import random
import json
import os

for item in createimage.all_images:

    im1 = Image.open(f'./face_parts/face/{traitclass.face_files[item["Face"]]}.png').convert('RGBA')
    im2 = Image.open(f'./face_parts/eyes/{traitclass.eyes_files[item["Eyes"]]}.png').convert('RGBA')
    im3 = Image.open(f'./face_parts/ears/{traitclass.ears_files[item["Ears"]]}.png').convert('RGBA')
    im4 = Image.open(f'./face_parts/hair/{traitclass.hair_files[item["Hair"]]}.png').convert('RGBA')
    im5 = Image.open(f'./face_parts/mouth/{traitclass.mouth_files[item["Mouth"]]}.png').convert('RGBA')
    im6 = Image.open(f'./face_parts/nose/{traitclass.nose_files[item["Nose"]]}.png').convert('RGBA')

    #Create each composite
    com1 = Image.alpha_composite(im1, im2)
    com2 = Image.alpha_composite(com1, im3)
    com3 = Image.alpha_composite(com2, im4)
    com4 = Image.alpha_composite(com3, im5)
    com5 = Image.alpha_composite(com4, im6)

                     

    #Convert to RGB
    rgb_im = com5.convert('RGB')
    file_name = str(item["tokenId"]) + ".png"
    rgb_im.save("./images/" + file_name)