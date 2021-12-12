import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
from papa_pg import *


class OtborHardDep():
    def __init__(self, deps_choise):
        if ' ' in deps_choise:
            self.deps = deps_choise.split(' ')
        else:
            self.deps = [deps_choise,]
        
    def main_otbor_hard_dep(self):     
        head = 'term;dep\n'
        out = head
       
        for dep in self.deps:
            term = dep + '1'
            out += term + ';' + dep + '\n'

        
        info = text_to_file(out, IN_DATA_PATH + 'otbor.csv')
        insert_all_otbor() + '\n\n'
        info += '\n' + out + '\n'
        self.info = info

