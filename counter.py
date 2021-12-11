import traitclass
import createimage


face_count = {}
for item in traitclass.face:
    face_count[item] = 0
    
ears_count = {}
for item in traitclass.ears:
    ears_count[item] = 0

eyes_count = {}
for item in traitclass.eyes:
    eyes_count[item] = 0
    
hair_count = {}
for item in traitclass.hair:
    hair_count[item] = 0
    
mouth_count = {}
for item in traitclass.mouth:
    mouth_count[item] = 0
    
nose_count = {}
for item in traitclass.nose:
    nose_count[item] = 0

for image in createimage.all_images:
    face_count[image["Face"]] += 1
    ears_count[image["Ears"]] += 1
    eyes_count[image["Eyes"]] += 1
    hair_count[image["Hair"]] += 1
    mouth_count[image["Mouth"]] += 1
    nose_count[image["Nose"]] += 1
    
print(face_count)
print(ears_count)
print(eyes_count)
print(hair_count)
print(mouth_count)
print(nose_count)