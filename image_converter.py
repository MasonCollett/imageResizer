#!/local/cluster/bin/python3
######################################################################################
#   ==  image_converter.py  ==
#   Mason Collett - mason.collett@a-dec.com 
# 
#   Function: Script that converts a directory of photos into the desired size
# 
#   When calling the script:
#       First argument needs to be a filepath to the directory of photos
#         > Nothing else can be in the directory but the photos to be modified 
#       Second argument needs to be the new width
#       Third argument needs to be the new height
#       Camera defaults to a 1.5 : 1 setting, so ideally leave images in that ratio
#
#####################################################################################

import sys
import io
import os
import glob
from PIL import Image

# Get Command line arguments
args = sys.argv
directory = args[1]
new_width = int(args[2])
new_height = int(args[3])

# Delete any previous _scaled.jpg files
for i in glob.glob(directory+'\\*_scaled.jpg'):
    os.remove(i)

# Open directory, get image filepaths, resize images
for filename in os.listdir(directory):
    
    # Get picture filepaths
    picture_filepath = (directory+ "\\" + filename)

    # Resize images
    picture = Image.open(picture_filepath)
    picture = picture.resize((new_width, new_height),Image.ANTIALIAS)
    picture.save((picture_filepath+"_scaled.jpg"), optimize = True, quality = 100)


