import os
import hashlib
from blob import Blob

# Class definition begins
class Tree(staticmethod):

    def create_tree(path: str, main_dir: str):
        '''
        Tree structure:
        Line1..........."tree"
        Line2 onwards...<object type>  <name>  <hash>....:(separated by tab)
        '''
        initial_dir = os.getcwd()
        os.chdir(main_dir)
        
        cont = "tree"

        os.chdir(os.path.join(".oak","objects"))
        for root,dirs,file in os.walk(path):
            for filename in file:          #iterating through only the files in the object folder and storing them as blob
                if filename.startswith("."):    #ignoring the hidden files
                    continue
                else:
                    name_blob = filename.name
                    hash_blob = Blob.create_blob(filename.path,main_dir)
                    cont = "\n" + "blob" + "\t" + name_blob + "\t" + hash_blob

            for dirname in dirs:          #iterating through directories and storing them as tree objects 
                name_tree = dirname.name
                hash_tree = Tree.create_tree(dirname.path , main_dir)
                cont = "\n" + "tree" + "\t" + name_tree + "\t" + hash_tree
        
        hash_str = hashlib.sha1(cont.encode('utf-8'))
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
            file.write("tree\n")
            file.write(cont)
                

        os.chdir(initial_dir)
        return hash_str
    
# Class definition ends