from PIL import Image
from IPython.display import display
import random
import json
import os

import traitclass


TOTAL_IMAGES = 100 # Number of random unique images we want to generate

all_images = [] 

# A recursive function to generate unique image combinations
def create_new_image():
    
    new_image = {} #

    # For each trait category, select a random trait based on the weightings 
    new_image ["Face"] = random.choices(traitclass.face, traitclass.face_weights)[0]
    new_image ["Ears"] = random.choices(traitclass.ears, traitclass.ears_weights)[0]
    new_image ["Eyes"] = random.choices(traitclass.eyes, traitclass.eyes_weights)[0]
    new_image ["Hair"] = random.choices(traitclass.hair, traitclass.hair_weights)[0]
    new_image ["Mouth"] = random.choices(traitclass.mouth, traitclass.mouth_weights)[0]
    new_image ["Nose"] = random.choices(traitclass.nose, traitclass.nose_weights)[0]
    
    if new_image in all_images:
        return create_new_image()
    else:
        return new_image


for i in range(TOTAL_IMAGES): 
    
    new_trait_image = create_new_image()
    
    all_images.append(new_trait_image)        



#Check Uniqueness of each image NFT#   
    
def all_images_unique(all_images):
    seen = list()
    return not any(i in seen or seen.append(i) for i in all_images)

print("Are all images unique?", all_images_unique(all_images))
# Add token Id to each image
i = 0
for item in all_images:
    item["tokenId"] = i
    i = i + 1
   
print(all_images)




for item in all_images:

    im1 = Image.open(f'./face_parts/face/{traitclass.face_files[item["Face"]]}.png').convert('RGBA')
    im2 = Image.open(f'./trait-layers/eyes/{traitclass.eyes_files[item["Eyes"]]}.png').convert('RGBA')
    im3 = Image.open(f'./trait-layers/ears/{traitclass.ears_files[item["Ears"]]}.png').convert('RGBA')
    im4 = Image.open(f'./trait-layers/hair/{traitclass.hair_files[item["Hair"]]}.png').convert('RGBA')
    im5 = Image.open(f'./trait-layers/mouth/{traitclass.mouth_files[item["Mouth"]]}.png').convert('RGBA')
    im6 = Image.open(f'./trait-layers/nose/{traitclass.nose_files[item["Nose"]]}.png').convert('RGBA')

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