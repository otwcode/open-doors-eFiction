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

## Known Issues
# Refusing to allow an OAuth App
```
!	refs/heads/supporting-files:refs/heads/supporting-files	[remote rejected] (refusing to allow an OAuth App to create or update workflow `.github/workflows/python-app.yml` without `workflow` scope)
```
The Github repository uses Github Actions to automatically run tests when you raise a pull request or merge to the master branch. You may get this message if you are using an OAuth application like Github Desktop or the Github integration in a third-party application like VSCode or IntelliJ/Pycharm. The following may help:
1. In your Github account, go to Settings (click on your avatar in the top right-hand corner)
1. Go to Developer Settings > Personal Access Tokens
1. Click on your application's name to edit the settings associated with its OAuth token. Make sure `workflow` is ticked.
1. Click on Update Token to save the change.
1. On the same page, click on Generate Token. Read the information carefully, then click OK to continue.
1. Copy the new token that Github shows you.
1. You will need to recreate your application's integration with Github using the new token for the change to take effect.

If this doesn't work, use the command line Git command `git push` to push your code instead.