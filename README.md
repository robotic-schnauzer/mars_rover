# Mars Rover Photos API
A simple in browser app to download images from the Mars Rover Photos API by uploading a textfile.

## To Run
I used Python 3.5.2 and Ubuntu 16.04 LTS to build and run this repository.

To run this application first download the repository.

Then in the command line, cd into the top level directory of the repository to create a python virtual environment by running:
  'virtualenv -p python3.5 venv'
 
 To activate the virtual environment run:
  'source venv/bin/activate'
 
 Then use the requirements.txt provided in the repo to install the dependencies with pip:
  'pip install -r requirements.txt'
 
 To run the application cd to directory with manage.py and run:
  'python manage.py runserver'
  
 Finally open the browser to 127.0.0.1:8000/
 
 The downloading is not asynchronous nor does it take advantage of multithreading so calling multiple dates may take 30 seconds. Downloading 12 images on my machine takes about 15 seconds, but it does work!
