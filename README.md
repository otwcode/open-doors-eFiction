# open-doors-eFiction
Script to convert eFiction for use in the Open Doors import process

# Pre-requisites

1. Python 3.7+

# Quickstart

1. Ensure you are using Python 3
1. (Optional) Create or load a [virtualenv wrapper](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#installing-virtualenv) for this project.
1. Install the requirements
    ```bash
    pip install -r requirements.txt
    ```
1. Run 
   ```bash
   python start.py CODENAME PATH-TO-WORKING-DIRECTORY
   ``` 
    where:
    
    - `python` is the path to your Python 3.7+ interpreter 
    - `CODENAME` is the short name for the archive you're processing
    - `PATH-TO-WORKING-DIRECTORY` is the root directory where you want the working files to go (a subdirectory named after the CODENAME above will be created in this directory).
1. Follow the instructions on screen.
