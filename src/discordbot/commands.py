import sys,os
sys.path.insert(0, os.path.abspath('..'))
from utils import *
from CONSTANTS import README_PATH
def get_readme():
    print("BRUHHHH" + README_PATH)
    info = ""
    with open(README_PATH,"r") as f:
        print(README_PATH)
        info = f.read()
        print(info)
    return "Test"

    

def process_msg(msg):
    """
    Process message
    """
    print(msg)
    if msg.startswith("info"):
        return get_readme()
    
    elif msg.startswith("help"):
        return "Naw bruh you aint getting no help"
    