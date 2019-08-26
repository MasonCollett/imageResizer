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
delete_count = 0
for i in glob.glob(directory+'\\*_scaled.jpg'):
    os.remove(i)
    delete_count = delete_count + 1

# Open directory, get image filepaths, resize images
new_count = 0
original_filesize = 0
new_filesize = 0
for filename in os.listdir(directory):
    
    # Get picture filepaths
    picture_filepath = (directory+ "\\" + filename)
    original_filesize = original_filesize + os.path.getsize(picture_filepath)

    # Resize images
    picture = Image.open(picture_filepath)
    picture = picture.resize((new_width, new_height),Image.ANTIALIAS)
    picture.save((picture_filepath+"_scaled.jpg"), quality = 100)
    new_filepath = picture_filepath+"_scaled.jpg"
    new_filesize = new_filesize + os.path.getsize(new_filepath)
    new_count = new_count + 1

print("\nImage conversion complete.")
print(delete_count, "old copies deleted.")
print(new_count, "new pictures created.\n")

print("Original pictures storage space:",original_filesize, "bytes")
print("Resized pictures storage space:\t",new_filesize, "bytes\n")

print("File size reduced by: ", str(round(100 - ((new_filesize/original_filesize)*100), 2)), "%")



