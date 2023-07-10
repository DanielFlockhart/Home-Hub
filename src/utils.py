import os,sys

def get_directory():
    """
    Get directory of the file
    """
    return os.path.dirname(os.path.realpath(__file__))  

def get_token(file):
    """
    Get token from file
    To Keep It Private
    """
    with open(file,"r") as f:
        return f.read().strip()
    
def set_token(file,token):
    """
    Write Token To File
    Will be JSON file when we have more than one token
    """
    with open(file,"w") as f:
        f.write(token)

