import os,sys

def get_directory():
    '''
    Gets the directory of the data folder, relative to position of this file
    '''
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_token():
    """
    Get token from file
    To Keep It Private
    """
    from CONSTANTS import TOKEN_PATH
    with open(TOKEN_PATH,"r") as f:
        return f.read().strip()
    
def set_token(file,token):
    """
    Write Token To File
    Will be JSON file when we have more than one token
    """
    with open(file,"w") as f:
        f.write(token)

