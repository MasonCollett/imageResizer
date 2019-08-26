## ImageConverter v1.0


## Description

image_converter.py is a Python script that will resize a picture to a given size, greatly reducing file size.


## Installation

These steps will only need to be performed if this is the first time a python script is being run on the computer:
	1. Go to: https://www.python.org/downloads/windows/
	2. Download "Windows x86-64 executable installer".
	3. Run the executable to download Python.  Make sure to check yes to "Add Python to PATH". Take note of the install location.

This step will only need to be performed the first time running image_converter.py:
	1. After installing Python, open Command Prompt on Windows
	2. Run the following line of code:
	   pip install pillow


## Usage 

Script requires 3 arguments to be run:
	1. Path to your python.exe file.
		This is usually found in C:\Python37\python.exe
	2. Path to where image_converter.py is stored.
	3. Path to directory where images to be converted are.
	4. New desired width of pictures.
		-Needs to be a whole number greater than zero.
	5. New desired height of pictures.
		-Needs to be a whole number greater than zero.

Output: 
	- Script will output copies of all of the pictures in the directory.
	- Names will be identical, copies will contain "_scaled.jpg" added on.

Special notes:
	- The only thing that can be in the pictures directory is the pictures to be resized.  
	  It is recommended to create a new, temporary directory with only the pictures of 
	  interest and using that directory in the call.
	- If there are pictures containing "_scaled.jpg" in the filenames, they will be removed/replaced. 
	  Hence, why it is also a good idea to create a new directory.
	- Run the script from Windows Command Prompt


## Example Call
														
C:\Python\Python37\python.exe C:\Users\mason.collett\Python\ImageConverter\image_converter.py C:\Users\mason.collett\LabPictures 150 100

^filepath to python.exe       ^filepath to image_converter.py			              ^filepath to directory of pictures to change	^ ^ new width, new height


## Support

Contact: Mason Collett
email: mason.collett@a-dec.com
