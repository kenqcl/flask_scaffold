"""
    Create Flask application directory structure

    - Base on "Flask Web Development, 2nd - O'Reilly 2018" "Chapter 7"
    - Be aware: the files are dummy file, empty, wihout content

    Usage
    -----------------
    python flask_scaffold.py <proj_home>

    Argument
    -----------------
    sys.argv[1]: String
        project home dir
        - can be absolute path, i.e: "D:\temp\proj"
        - or relative path, "proj", or ".\proj"

    Errors
    ------------------
    if 2nd argument(sys.argv[1]) is not set:
        exit -1
"""

import os, sys

"""
    Directories to create
    - ["app", "templates"] means to create "app/templates" dir
"""
DIRS = [
    ["app", "templates"], # "app/templates" dir
    ["app", "static"],
    ["app", "main"],
    ["migrations"],
    ["tests"],
    ["venv"],
]

"""
    Files to create
    - ["app", "main", "__init__.py"] means to  create "app/main/__init__.py" file
"""
FILES = [
    ["app", "main", "__init__.py"], # "app/main/__init__.py" file
    ["app", "main", "errors.py"],
    ["app", "main", "forms.py"],
    ["app", "main", "views.py"],
    ["app", "__init__.py"],
    ["app", "models.py"],
    ["app", "email.py"],
    ["tests", "__init__.py"],
    ["requirements.txt"],
    ["config.py"],
    ["flask_app.py"]
]

def get_proj_home(home):
    if os.path.isabs(home):
        return home
    else:
        phome = os.path.abspath(os.path.dirname(__file__))
        phome = os.path.join(phome, home)
        return phome

def create_dirs_files(home):
    from pathlib import Path
    for fd in DIRS + FILES:
        target =os.path.join(home, *fd)
        print("Create: " + target)

        # Skip if target exists
        if os.path.exists(target):
            continue

        # for DIRS
        if fd in DIRS:
            os.makedirs(target)
        
        # for FILES
        if fd in FILES:
            Path(target).touch()

if __name__ == '__main__':

    # Check command line argument, 2nd argument is Proj HOME
    if len(sys.argv) < 2:
        msg = "Error!\n" + \
              "Please specify proj home as:\n" + \
              f"   python {__file__} abc \n"
        print(msg)
        exit(-1)
    
    # Get project home
    home = get_proj_home(sys.argv[1])
    print("Project home: " + home)

    # create dirs and files
    create_dirs_files(home)


