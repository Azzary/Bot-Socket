import json
import os

class Get_account():

    def __init__(self,ndc):
        self.ndc = ndc
        


    def get_data(self):
        dir_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),f"compte\\{self.ndc}.json")
        with open(dir_path,"r") as f:
            data = f.read().split("|")
        return data

        
    
    
                        


