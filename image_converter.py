#!/local/cluster/bin/python3
######################################################################################
#   ==  image_converter.py  ==
#   Mason Collett
# 
#   Function: Script that converts a directory of photos into the desired size
# 
#   See README for usage
#
#####################################################################################

import sys
import io
import os
import glob
from PIL import Image

# Visual start to program for users
print("\n======================================================================\n")
visual_code = 0

# Get Command line arguments
args = sys.argv
directory = args[1]

# Setup whether it's fixed or percentage resizing
if(len(args) == 4):
    
    # Get width and height from command line
    new_width = int(args[2])
    new_height = int(args[3])

    # Check for acceptable size
    while(new_height > 10000 or new_width > 10000):
        new_width, new_height = input("Error: Dimensions too high. Please enter new dimensions: ").split()
        new_height = int(new_height)
        new_width = int(new_width)
        visual_code = 1

    # Determines calculation for new width and height later
    setup = "fixed"

# Percentage resizing
elif(len(args) == 3):

    # Get percentage from command line
    scale = float(args[2])

    # Check for size within bounds 
    while (scale > 200):
        scale = float(input("Error: Percentage too high. Please enter a new percentage: "))
        visual_code = 1

    # Determines calculation for new width and height later
    og_width = 0
    og_height = 0
    setup = "percentage"  
if(visual_code == 1):
    print("")

# Create new directory
os.makedirs(directory+"_Resized\\", exist_ok = True)
new_directory = directory + "_Resized\\"

# Create stat counters
new_count = 0
original_filesize = 0
new_filesize = 0
total_files = str(len(os.listdir(directory)))

# Print statements for user readability and so user can double check
sys.stdout.write("Resize starting, using ")
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

# Summary information of new files
print("\n\nImage conversion complete!")
print(new_count, "new pictures created.\n")

# Summary information to again double check type used and parameters
sys.stdout.write("Images resized using: ")
if(setup == "percentage"): 
    sys.stdout.write("Percentage- ")
    sys.stdout.write(str(scale))
    sys.stdout.write(" %\n\n")
else:
    sys.stdout.write("Fixed- ")
    sys.stdout.write(str(new_width))
    sys.stdout.write(" x ")
    sys.stdout.write(str(new_height))
    sys.stdout.write("\n\n")


# Summary information of new space used
print("Original pictures storage space:",original_filesize, "bytes")
print("Resized pictures storage space:\t",new_filesize, "bytes\n")

# Summary information saved space
print("File size reduced by: ", str(round(100 - ((new_filesize/original_filesize)*100), 2)), "%")

# Visual end to program
print("\n======================================================================")










    

