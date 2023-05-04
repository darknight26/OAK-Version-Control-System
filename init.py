import os

def init():
    cwd = os.getcwd()
    if os.path.exists(os.path.join(cwd,".oak")):
        print("Error:Repository already exists")
    else:
        os.mkdir(".oak")
        os.chdir(".oak")
        os.mkdir("objects")
        print("Empty Repository created succesfully")
    os.chdir(cwd)
    return
init()