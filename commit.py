import os
import hashlib
import datetime
from blob import Blob
from tree import Tree
commit_cont = "commit"
# Class definition begins
class Commit(staticmethod):
    

    def create_commit(comment: str):
        '''
        Tree structure:
        Line1..........."commmit"
        Line2...........<hash of main dir tree>
        Line3...........<hash of parent commit>
        Line4...........<timestamp>
        Line5...........<comment>
        '''

        '''
        In this version of the system, there isn't any add
        implementation. Commit includes all non dir files
        present in the main directory in a commit.
        '''
        
        main_dir = os.getcwd()

        
        commit_cont += "\n" + Commit.get_tree_hash(Tree.create_tree(main_dir,main_dir))
        commit_cont += "\n" + Commit.get_parent_hash(Tree.create_tree(main_dir,main_dir))
        commit_cont += "\n" + Commit.get_curr_timestamp() + Commit.get_date(main_dir,main_dir)
        commit_cont += "\n" + comment

        hash_str = hashlib.sha1(commit_cont.encode('utf-8'))
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
            file.write(commit_cont)

        os.chdir(main_dir)
        return hash_str


    def get_tree_hash(hash_str: str, main_dir: str):
        initial_dir = os.getcwd()
        os.chdir(main_dir)

        tree_hash = Tree.create_tree(main_dir,main_dir)

        os.chdir(initial_dir)
        return tree_hash
    

    def get_parent_hash(hash_str: str, main_dir: str):
        initial_dir = os.getcwd()
        os.chdir(main_dir)

        if os.path.exists(os.path.join(".oak","HEAD")):
            with open("HEAD","r") as file:
                parent_hash = file.read()
        else:
            print("NULL")

        os.chdir(initial_dir)
        return parent_hash
    

    def get_date(hash_str: str, main_dir: str):
        initial_dir = os.getcwd()
        os.chdir(main_dir)

        date = datetime.date()

        os.chdir(initial_dir)
        return date
    

    def get_comment(hash_str: str, main_dir: str):
        initial_dir = os.getcwd()
        os.chdir(main_dir)

        comment=commit_cont[4][0:]

        os.chdir(initial_dir)
        return comment
    

    def get_curr_timestamp():
        
        timestamp = datetime.time()

        return timestamp

# Class definition ends