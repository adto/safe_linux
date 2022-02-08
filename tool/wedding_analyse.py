# main function
from argparse import ArgumentParser
from wedding_common import *
import os
import sys
from os import walk
import json


def remove_duplicate(input_list):

    return list(dict.fromkeys(input_list))

def find_def_sym(db,sym):
    
    #print(sym_undef)
    db_def = db["def"] 
    file_list = db["file"]
        
    for i in range(len(file_list)):   
        sym_defs = db_def[file_list[i]]
        
        for j in range(len(sym_defs)):
            sym_def = sym_defs[j]
  
            if sym_def == sym:
                
                #print(file_list[i])
                return file_list[i]
    
    return ("UNKNOWN_FILE")
    
                
# ok

def find_file(extension,path):
    
    #print(path)
    
    ret = []
    for (dirpath, dirnames, filenames) in walk(path):
         for i in range(len(filenames)):         
            if filenames[i].endswith(extension):
                ret.append(dirpath + "/" +filenames[i]) 
                
    #print(ret)            
    return ret

def extract_file(input, linux_build_path):
    
    ret = []
    for i in range(len(input)):
              
        if ".o" in input[i]:
            ret.append(linux_build_path + "/" + input[i])
        else:
            ret += (find_file(extension=".o", path=linux_build_path + "/" + input[i])) 
            
    ret = remove_duplicate(ret)
    ret.sort()

    return ret                  
         
def extract_syms(file_name, type="all") :
        
    ret = []
    
    if type is "undefined":
        type_flag="--undefined-only"
    elif type is "defined":
        type_flag="--defined-only"
    elif type is "all": 
        type_flag=""
    else:
        raise Exception("Invalid argument: type of function: extract_syms: {} ".format(type))
    
    ph = execute("nm " + type_flag + " " + file_name)
    raw = ph.communicate()[0].decode()
    lines = raw.split('\n')
        
    for i in range(len(lines)-1):
        if "w " in lines[i]:
            symval = lines[i].split("w ", 1)[1]
        elif "U " in lines[i]:
            symval = lines[i].split("U ", 1)[1]
        elif "t " in lines[i]:
            symval = lines[i].split("t ", 1)[1]
        elif "T " in lines[i]:
            symval = lines[i].split("T ", 1)[1]
        elif "r " in lines[i]:
            symval = lines[i].split("r ", 1)[1]
        elif "R " in lines[i]:
            symval = lines[i].split("R ", 1)[1]
        elif "d " in lines[i]:
            symval = lines[i].split("d ", 1)[1]
        elif "D " in lines[i]:
            symval = lines[i].split("D ", 1)[1]
        elif "b " in lines[i]:
            symval = lines[i].split("b ", 1)[1]             
        elif "B " in lines[i]:
            symval = lines[i].split("B ", 1)[1]            
        elif "W " in lines[i]:
            symval = lines[i].split("W ", 1)[1]            
        elif "V " in lines[i]:
            symval = lines[i].split("V ", 1)[1]            
        elif "C " in lines[i]:
            symval = lines[i].split("C ", 1)[1]            
        elif "a " in lines[i]:
            symval = lines[i].split("a ", 1)[1]                
        else:
            raise Exception("Undefined argument: {} in file {}".format(lines[i], file_name))    
        ret.append(symval)
    return ret    

@timeit
def do_analyse(args):
    
    print( c.OKBLUE +  "Execute action: Migate." + c.ENDC)     
    
    linux_build_path = os.path.abspath(args["linux_build"])
    linux_source_path = linux_build_path + "/source"
 
    file_list = []
    
    for (dirpath, dirnames, filenames) in walk(linux_build_path):
        for i in range(len(dirnames)):         
            if dirnames[i] != "source" and \
            dirnames[i] != ".git":        
                file_list = file_list + find_file(extension=".o", path=linux_build_path + "/" + dirnames[i])          
        break
    
    db = {}
    db_def = {}
    db_undef = {}
    db["def"] = db_def
    db["undef"] = db_undef
    db["file"] = file_list
    
    for i in range(len(file_list)):
        db_undef[file_list[i]] = extract_syms(file_list[i], type="undefined") 

    for i in range(len(file_list)): 
        db_def[file_list[i]] = extract_syms(file_list[i], type="defined") 

    db_out={}
    #db_out["file"]= []
    db_out["sym"] = {} 
    
    #do some analysis, inputs are: 
    #input = ["net", "fs", "block", "certs", "crypto", "security", "lib", "arch/arm64/crypto", "arch/arm64/lib"]
    #input = ["net"]
    #input = ["net/socket.o"]
    #input = ["kernel", "lib", "arch/arm64/lib", "mm", "init" ]
    input = ["kernel", "arch/arm64", "mm", "lib", "crypto", "security", "virt"]
             
    #create input file list
    input_files = extract_file(input, linux_build_path)


    print(input_files)
    
    #fill out db_out["sym"] dict     
    for j in range(len(input_files)):
        syms = db_undef[input_files[j]]
        for k in range(len(syms)):
            sym = syms[k]
            ret_flag = False
            for sym_key in db_out["sym"]:
                if sym_key == sym:
                    db_out["sym"][sym] += 1
                    ret_flag = True
                    break;
            if not ret_flag:
                 db_out["sym"][sym] = 1


    for sym_key in db_out["sym"]:
        file = find_def_sym(db,sym_key)
        
        if not file in input_files:
            
            #register the result
            if file not in db_out.keys():
                db_out[file] = {}
            
            db_out[file][sym_key] = db_out["sym"][sym_key]
            
          
    #do some printing    
    for file_key in sorted(db_out):
        if file_key is not "sym":
            print (file_key, db_out[file_key])
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    #Convert to json data
    db_j = json.dumps(db)
    
    #Write to file 
    with open('db.json', 'w', encoding='utf-8') as f:
        json.dump(db_j, f, ensure_ascii=False, indent=4)
    
    print( c.OKBLUE +  "Analysis action executed." + c.ENDC) 
    
    