import os
import hashlib

# Class definition begins
class Blob(staticmethod):

    def create_blob(path: str, main_dir: str):
        '''
        Blob structure:
        Line1..........."blob"
        Line2 onwards...content
        '''
        initial_dir = os.getcwd()
        os.chdir(main_dir)

        #Filling content from path file to variable content
        with open(path,"r") as file:
            content = file.read()

        #hashing of data by sha1 encoding by converting data forst into binary by utf-8 coding then the sha1 to hexadecimal by hexdigest
        hash_str = hashlib.sha1(content.encode('utf-8'))
        hash_str = hash_str.hexdigest()
        prefix = hash_str[:2]
        suffix = hash_str[2:]


        #changing directory to /.oak/objects
        os.chdir(os.path.join(".oak","objects"))

        #making a folder with first two char of hash if it doesnt already exists or else just storing it in the avail folder as it helps in searching bringing it down to 256 searches 
        if not os.path.exists(prefix):
            os.mkdir(prefix)
        os.chdir(prefix)

        #storing content in a file with name 38 chars of hash 
        with open(suffix,"w") as file:
            file.write("blob\n")
            file.write(content)

        os.chdir(initial_dir)
        return hash_str


    def get_content(hash_str: str, main_dir: str):
        initial_dir = os.getcwd()
        os.chdir(main_dir)

        #opening the blob folder
        os.chdir(os.path.join(".oak","objects",hash_str[:2]))

        with open(hash_str[:2],"r") as file:
            content = file.read()[5:]    #content will be all the lines of data after first 5 character which are blob and new line
        

        os.chdir(initial_dir)
        return content
    
# Class definition ends