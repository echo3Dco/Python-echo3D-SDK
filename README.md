# Echo3D Demo Using Python

## About this demo

This demo uses Python to interact with the Echo3D API. It access all 3d models in a user account given the api key and security key, and let the user to choose which 3d model to render. Once the user has made a choice, the Python demo will attempt to retrieve the 3d model and render it. If the render is successful, a new window will pop out displaying the rendered 3d model. User can also rotate the 3d model by mouse dragging.  

## Requirements

* `Python 3.8.16`
* `vedo`
* `pyrender`

## Instructions for package installation

1. Download and install Python 3.8.16 from https://www.python.org/downloads/release/python-3816/. By default, pip (a Python package installation tool) should also come with it.

2. Run the following commands:
   
   `pip install vedo`
   
   `pip install pyrender`
   
   Above commands should install `vedo` and `pyrender` to your Python environment. After that, you should be able to run the main demo. 

## Echo3D API Instructions

1. Register for a FREE account at echo3D.
2. Upload any 3D models to the console. Currently, this Python demo only supports `obj` and `glb` file format. 
3. Copy your API key from the top of the console.
4. Copy your security key by clicking the `Security` button from the left sidebar of the console.

## Running Instructions

1. Install all required packages and follow the Echo3D API instructions as described above.

2. Clone this repo.

3. Open a terminal and `cd` to this repo. Make sure that Python 3.8.16 is properly installed by running the command `python --version`. You can also check if `vedo` and `pyrender` are installed by running the command `pip list`.

2. Run the command as follows:
   
   `python main.py [API_KEY] [SECURITY_KEY]`
   
   where `[API_KEY]` is your Echo3D API key from the top of the console, and `[SECURITY_KEY]` is your security key by clicking the `Security` button from the left sidebar of the console. 
3. A prompt showing a list of available 3d models will appear. Enter an integer number to choose which 3d model to retrieve and render.
4. A new window will pop up displaying the rendered model. 


