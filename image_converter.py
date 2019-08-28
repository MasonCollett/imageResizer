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

print("\n======================================================================\n")

# Get Command line arguments
args = sys.argv
directory = args[1]

# Setup whether it's set or scaled resizing
if(len(args) == 4):
    new_width = int(args[2])
    new_height = int(args[3])
    setup = "fixed"

elif(len(args) == 3):
    scale = float(args[2])
    while (scale > 200):
        scale = float(input("Error: Percentage too high. Please enter a new percentage: "))

    og_width = 0
    og_height = 0
    setup = "percentage"  

# Create new directory
os.makedirs(directory+"_Resized\\", exist_ok = True)
new_directory = directory + "_Resized\\"

# Create stat counters
new_count = 0
original_filesize = 0
new_filesize = 0
total_files = str(len(os.listdir(directory)))

# Print statements for user readability
sys.stdout.write("\nResizing starting, using ")
sys.stdout.write("\"")
sys.stdout.write(setup)
sys.stdout.write("\" setup...\n\n")

# Open directory, get image filepaths, resize images
for filename in os.listdir(directory):
    
    # Get picture filepaths
    picture_filepath = (directory+ "\\" + filename)
    original_filesize = original_filesize + os.path.getsize(picture_filepath)

    # Open image
    picture = Image.open(picture_filepath)

    # If scaled resizing, set new lengths and heights
    if(setup == "percentage"):
        og_width, og_height = picture.size
        new_width = round(og_width * (scale/100))
        new_height = round(og_height * (scale/100))
    
    # Resize picture
    picture = picture.resize((new_width, new_height),Image.ANTIALIAS)

    # Convert to rgb then jpg and save
    picture = picture.convert('RGB')
    picture.save((new_directory+filename+"_resized.jpg"), quality = 100)

    # Get new picture storage space
    new_filepath = new_directory+filename+"_resized.jpg"
    new_filesize = new_filesize + os.path.getsize(new_filepath)
    new_count = new_count + 1
    sys.stdout.write("\rImages Resized: ")
    sys.stdout.write(str(new_count))
    sys.stdout.write("/")
    sys.stdout.write(total_files)


print("\nImage conversion complete!")
print(new_count, "new pictures created.\n")

print("Original pictures storage space:",original_filesize, "bytes")
print("Resized pictures storage space:\t",new_filesize, "bytes\n")

print("File size reduced by: ", str(round(100 - ((new_filesize/original_filesize)*100), 2)), "%")

print("\n======================================================================")









    

