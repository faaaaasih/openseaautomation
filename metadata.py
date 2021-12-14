import createimage
import json

metadatafilepath = './metadata/all-traits.json'

with open(metadatafilepath, 'w') as outfile:
    json.dump(createimage.all_images, outfile, indent=4)


    ### Export Metadata for each image ###

IMAGES_BASE_URL = "https://gateway.pinata.cloud/ipfs/QmePSChjPphynzy44KXASX4iogMUCiGMUpHoCA6kNxm46Y"
PROJECT_NAME = "NFT TEST"

f = open('./metadata/all-traits.json',) 
data = json.load(f)


def getAttribute(key, value):
    return {
        "trait_type": key,
        "value": value
    }

for i in data:
    token_id = i['tokenId']
    token = {
        "image": IMAGES_BASE_URL + str(token_id) + '.png',
        "tokenId": token_id,
        "name": PROJECT_NAME + ' ' + str(token_id),
        "attributes": []
    }
    token["attributes"].append(getAttribute("Face", i["Face"]))
    token["attributes"].append(getAttribute("Ears", i["Ears"]))
    token["attributes"].append(getAttribute("Eyes", i["Eyes"]))
    token["attributes"].append(getAttribute("Hair", i["Hair"]))
    token["attributes"].append(getAttribute("Mouth", i["Mouth"]))
    token["attributes"].append(getAttribute("Nose", i["Nose"]))

    with open('./metadata/' + str(token_id) + ".json", 'w') as outfile:
        json.dump(token, outfile, indent=4)

f.close()