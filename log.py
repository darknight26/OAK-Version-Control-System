import os
from commit import Commit


class log(staticmethod):
    

    def log(main_dir:str):

        os.chdir(os.path.join(main_dir,".oak","objects"))
        
        cwd=os.getcwd()
        
        for root,dirs,files in os.walk(cwd):
            for file in files:
                with open(file,"r") as f:
                    if(f.read()[0] == 'c'):
                        print(Commit.get_date() +"\t" + Commit.get_curr_timestamp)
                        print("\n"+Commit.get_comment)

        os.chdir(main_dir)