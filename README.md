ImageResizer v1.5.1
------------------------------

Description
---------------
image_resizer.py is a Python script that will resize a picture to a given size, greatly reducing storage space.


Installation
---------------
All dependencies should be installed already.  


Usage 
--------------
There are two ways to run this program in Command Prompt, using either 4 or 5 arguments based on preference/need.

Using 5 arguments, i.e the "Fixed" Method:

	1. Path to python.exe file.
	2. Path to where image_resizer.py is stored.
	3. Path to directory where images to be resized are.
	4. New desired width of pictures.
		-Needs to be a whole number greater than zero.
		-Capped at 10000
	5. New desired height of pictures.
		-Needs to be a whole number greater than zero.
		-Capped at 10000

Using 4 arguments, i.e the "Percentage" Method:

	1. Path to python.exe file.
	2. Path to where image_resizer.py is stored.
	3. Path to directory where images to be resized are.
	4. Percentage size of the original pictures the new pictures should be.
		-Can be any number greater than zero.
		-Numbers greater than 100 will create larger files.  Size increased is capped at 200%.

Output: 

	- A new directory containing resized copies of all of the pictures from the pictures directory.
	- New directory will be in the same directory as the original pictures directory with "_Resized" added on.
	- New pictures will contain identical filenames with "_resized.jpg" added on.
	- Program status will be printed to console.
	- Additional statistical information will be printed to the console.

Special notes:

	- Only the pictures to be resized can be in the picture directory.  
	- If there is already a _Resized directory made from the pictures directory, it will be overwritten.
	- For best results, it is recommended to see what ratio the pictures are and to resize them in the same ratio.
	- If the photos to be resized contain different width to height ratios, it's recommended to use Percentage.


Example Calls
--------------	

Fixed Resize Call: 
														
"S:\Materials Laboratory\TESTS IN PROGRESS\MasonsScripts\Python\Python37\python.exe" "S:\Materials Laboratory\TESTS IN PROGRESS\MasonsScripts\ImageResizer\image_resizer.py" "S:\Materials Laboratory\TESTS IN PROGRESS\MasonsScripts\ImageResizer\LabPictures" 300 200

	Outline: [python path] [script path] [picture directory path] [width] [height]

	Variable Arguments: [picture directory path] - set to directory of your pictures to be resized.
		 	    [width] - set new picture width
		 	    [height] - set new picture height

Percentage Resize Call: 

"S:\Materials Laboratory\TESTS IN PROGRESS\MasonsScripts\Python\Python37\python.exe" "S:\Materials Laboratory\TESTS IN PROGRESS\MasonsScripts\ImageResizer\image_resizer.py" "S:\Materials Laboratory\TESTS IN PROGRESS\MasonsScripts\ImageResizer\LabPictures" 50

	Outline: [python path] [script path] [picture directory path] [percentage]
	
	Variable Arguments: [picture directory path] - set to directory of your pictures to be resized.
		 	    [percentage] - any number to set the width and height of the new pictures x% of the original width and heights.

