#I frequenty print out screenshots from SAP.
#I use this routine to reduce transparency
#on all snapshots to use less ink.

import os, sys
from PIL import Image

all_files = os.listdir()
image_files = []

for file in all_files:
    extension = file.split(".")[1]
    if extension == "png":	#only accept .png images in directory.
        image_files.append(file)

for image_file in image_files:
    with Image.open(image_file) as im:
        im.putalpha(150)	#increase transparency (full saturation is 255).
        raw_name = image_file.split(".")[0]
        im.save(raw_name+"_new"+".png")





