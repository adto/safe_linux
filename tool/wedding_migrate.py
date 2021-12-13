# main function
from argparse import ArgumentParser
from wedding_common import *
import os
import sys
from os import walk

# ok
def find_file(filter,path):
    
    print(path)
    
    ret = []
    for (dirpath, dirnames, filenames) in walk(path):
         for i in range(len(filenames)):         
            if filter in filenames[i]:
                ret.append(dirpath + "/" +filenames[i]) 
                
    return ret            

def do_migrate(args):
    
    print( c.OKBLUE +  "Execute action: Migate." + c.ENDC)     

    #args["linux_build"]
    #args["output"]

    linux_build_path = os.path.abspath(args["linux_build"])
    linux_source_path = linux_build_path + "/source"
 
 
    file_list = []
    
    for (dirpath, dirnames, filenames) in walk(linux_source_path):
        for i in range(len(dirnames)):         
            if dirnames[i] != "source" and \
            dirnames[i] != ".git" and \
            dirnames[i] != "Documentation" and \
            dirnames[i] != "LICENSES":        
                file_list = file_list + find_file(filter=".ko",path=linux_build_path + "/" + dirnames[i])          
        break
 
    print(file_list)
    
    
       
    # for root, dirs, files in os.walk("."):
    # path = root.split(os.sep)
    # print((len(path) - 1) * '---', os.path.basename(root))
    # for file in files:
    #     print(len(path) * '---', file)
    
    
    
    f = []
    for (dirpath, dirnames, filenames) in walk(linux_source_path):
        f.extend(filenames)
        break
    
    print(f)

    #for (dirpath, dirnames, filenames) in os.walk(self.sysroot_path):
    #         files.extend(filenames)
    #         break

    

    # def get_package_file(self, module_dir_name, package_name):
    #
    #     ret_value= []
    #     files = []
    #
    #     for (dirpath, dirnames, filenames) in os.walk(self.sysroot_path):
    #         files.extend(filenames)
    #         break
    #
    #     if "ara_LSP" in module_dir_name:
    #         for file in files:
    #             if module_dir_name in file:    
    #                 ret_value.append(self.sysroot_path + "/" + file)    
    #     else:                            
    #         for file in files:
    #             if module_dir_name in file and package_name in file:    
    #                 ret_value.append(self.sysroot_path + "/" + file)    
    #
    #     return ret_value 





    print( c.OKBLUE +  "Migrat action executed." + c.ENDC) 