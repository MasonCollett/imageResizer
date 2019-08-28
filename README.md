## ImageResizerv1.3


## Description

image_resizer.py is a Python script that will resize a picture to a given size, greatly reducing storage space.


## Installation

All dependencies should be installed already.  


## Usage 

Command Prompt requires 5 arguments to run the script:
	1. Path to python.exe file.
	2. Path to where image_resizer.py is stored.
	3. Path to directory where images to be resized are.
	4. New desired width of pictures.
		-Needs to be a whole number greater than zero.
	5. New desired height of pictures.
		-Needs to be a whole number greater than zero.

Output: 
	- A new directory containing copies of all of the pictures from the pictures directory.
	- New directory will be in the same directory as the original pictures directory.
	- New pictures will contain identical filenames with "_resized.jpg" added on.
	- Additional statistical information will be printed to the console.
	- Program progress will be printed to console as well.

Special notes:
	- Only the pictures can be in the picture directory.  
	- If there is already a _Resized directory made from the pictures directory, it will be overwritten.
	- Usually, the lab camera takes pictures in a 1.5 to 1 ratio.  For best results, it is recommended to keep this ratio.


## Example Call
															
"S:\Materials Laboratory\TESTS IN PROGRESS\MasonsScripts\Python\Python37\python.exe" "S:\Materials Laboratory\TESTS IN PROGRESS\MasonsScripts\ImageResizer\image_resizer.py" "S:\Materials Laboratory\TESTS IN PROGRESS\MasonsScripts\ImageResizer\LabPictures" 300 200

Outline: [python path] [script path] [picture directory path] [width] [height]

Variable Arguments: [picture directory path] - set to directory of your pictures to be resized.  The "LabPictures" directory was created to test the script, feel free to use it.
		    [width] - set new picture width
		    [height] - set new picture height


## Support

Contact: Mason Collett
Email: mason.collett@a-dec.com

