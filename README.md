# Open Doors eFiction Converter
Script to convert eFiction for use in the Open Doors import process

## Pre-requisites

1. Python 3.7+
1. MySQL 5.7

## Before you start
Make sure you have the following:
1. The backup of the archive including the SQL backup file and `stories` folder (see [Where to find the original files](#Where-to-find-the-original-files) below). 
If they are compressed, for example in a zip file, they need to be decompressed into their own folder.
1. A short "code name" for the archive with no underscores, spaces or punctuation. This will be used throughout the code to prefix the MySQL databases and name intermediate files. Any short, distinctive name or acronym will do. Please use all lowercase characters for the codename, as Windows machines will automatically convert to lowercase when creating MySQL tables.
For example, if the archive is called "My Awesome Archive of Fandom Awesomeness", you might use a code name like `maafa` or `awesome` - archives often already have a nickname and if so, use that.


## Quickstart

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
    - `CODENAME` is the short name for the archive you're processing with no underscores, spaces or punctuation
    - `PATH-TO-WORKING-DIRECTORY` is the absolute path where you want the working files to go (eg: /Users/myusername/otw/thearchivename). Working files will include multiple backups of the various steps in this process.
1. Follow the instructions on screen.

Note that the process will create databases and tables in MySQL as well as files in the designated folder. All the databases will be prefixed with CODENAME.


## Process

1. Run 
   ```bash
   python start.py CODENAME PATH-TO-WORKING-DIRECTORY
   ``` 
    where:
    
    - `python` is the path to your Python 3.7+ interpreter 
    - `CODENAME` is the short name for the archive you're processing with no underscores, spaces or punctuation
    - `PATH-TO-WORKING-DIRECTORY` is the absolute path where you want the working files to go (eg: /Users/myusername/otw/thearchivename). Working files will include multiple backups of the various steps in this process.

2. Enter the full (original) name for the archive eg TER/MA, Land of Dreams
3. Enter your MySQL hostname
4. Enter your MySQL user name
5. Enter your MySQL password
6. Enter the full path to the database file, (eg /Users/myusername/myusername/otw/thearchivename/archivefile.sql)
7. Follow the prompts to run steps 1-4

### High-level overview of each step
- Start
- Step 01 Make a backup of original database
- Step 02 Create simplified database  
- Step 03 Convert metadata to Open Doors tables     
- Step 04 Convert chapters


### Step 01 - Make a backup of original database

This step creates a backup of the original database (in main directory), and then creates and tidies an edited version which is added to a new directory, 01, and loaded into mysql. 

### Step 02 -  Create simplified efiction database  

This step removes unused tables to create a simplified version of the edited database created in step 01, adds it to a new directory, 02, and loads it into MySQL

### Step 03 - Convert eFiction to Open Doors

This step converts the efiction tables into a new database using the Open Doors structure, and creates a backup of the new tables to a new directory 03.

### Step 04 - Convert chapters

This step copies the chapters from the specified location (eg /Users/myusername/Downloads/thearchivename/fiction/stories) into the chapters table of the Open Doors database created in step 03, and creates a backup in folder 04.


##  Next steps
Run https://github.com/otwcode/open-doors-code from step 03


## Where to find the original files
You will need to know the location of the following elements. They should be present in the zip file uploaded by the original archivist; decompress the zip and make sure you have the paths:
1. A **dump of the original database**: this will usually be a file with the .sql extension either in the zip file or in the 
root of the folder in the backup.
1. The **stories** folder: eFiction sites typically keep all the chapter contents in a `stories` folder, where the subfolders
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
