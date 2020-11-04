# Open Doors eFiction Converter
Script to convert eFiction for use in the Open Doors import process

## Pre-requisites

1. Python 3.7+
1. MySQL 5.7

## Quickstart

1. Ensure you are using Python 3
1. (Optional) Create or load a [virtualenv wrapper](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#installing-virtualenv) for this project.
1. Install the requirements
    ```bash
    pip install -r requirements.txt
    ```
1. Download the archive backup and find the SQL backup file and `stories` folder (see [Where to find the original files](#Where-to-find-the-original-files) below)
1. Run 
   ```bash
   python start.py CODENAME PATH-TO-WORKING-DIRECTORY
   ``` 
    where:
    
    - `python` is the path to your Python 3.7+ interpreter 
    - `CODENAME` is the short name for the archive you're processing
    - `PATH-TO-WORKING-DIRECTORY` is the full path where you want the working files to go (eg: /Users/myusername/otw/thearchivename). Working files will include multiple backups of the various steps in this process.
1. Follow the instructions on screen.

Note that the process will create databases and tables in MySQL as well as files in the designated folder. All the databases will be prefixed with CODENAME.

## Where to find the original files
You will need to know the location of the following elements. They should be present in the zip file uploaded by the original archivist:
1. A dump of the original database: this will usually be a file with the .sql extension either in the zip file or in the 
root of the folder in the backup.
1. The stories folder: eFiction sites typically keep all the chapter contents in a `stories` folder, where the subfolders
are author ids, and the filenames the chapter ids. 

It isn't unusual for backups to include the entire hard drive of the original web server, including multiple 
installations of eFiction; so make sure the folder you find has the same author and chapter ids as the database dump 
you were given.

### Tests
Unit tests are situated in `tests` folders within each package. Fixtures are stored in `test_data`. Some tests output side-effect artefacts to a `test_output` folder.

To run the tests, use Pytest:

```
python -m pytest
```

or if you installed Pytest separately, simply:

```
pytest
```

Continuous Integration is provided by GitHub Actions, configured in the `.github/workflows` folder. There are separate workflows for Linux vs MacOS and Windows because as of September 2020, the latter don't support services.

## Known Issues
#### "Refusing to allow an OAuth App" when pushing to GitHub
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
