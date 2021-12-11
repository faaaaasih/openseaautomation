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
    
    
