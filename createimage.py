from PIL import Image
from IPython.display import display
import random
import json
import os
import time

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
   
print(all_images[0])

