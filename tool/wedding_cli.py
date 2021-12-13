#!/usr/bin/env python3 

import os
import subprocess # for executing a shell command
import shlex # for string -> args conversion
import json # why not
from argparse import ArgumentParser
from wedding_common import * 
import wedding_migrate
import wedding_analyse

# commandline or json parser
def parse():
    
    arg = list()
    
    # construct the argument parse and parse the arguments
    ap = ArgumentParser()
    #ap.add_argument("-l", "--linux_source", required=True, help="linux soruce directory path")
    ap.add_argument("-a", "--action",  type=Action, choices=list(Action), required=True, help="action to do")
    ap.add_argument("-l", "--linux_build",  required=True, help="linux build directory path")
    ap.add_argument("-o", "--output",  required=True, help="output directory")
    args = vars(ap.parse_args())

    #print(args)    
    #args["linux_build"]
    #args["output"]
    #args.["action"]
    
    return args


# main function
if __name__ == "__main__":
    
    print( c.OKBLUE +  "Hello! This is the great wedding project cli tool." + c.ENDC)    

    args = parse() 
 
    if args["action"] == Action.migrate:
        wedding_migrate.do_migrate(args)
    elif args["action"] == Action.analyse:
        wedding_analyse.do_analyse(args)        
    else:
        None    

    print( c.OKBLUE +  "All actions are executed, goodbye for now!" + c.ENDC)   
    
###############
#End of script#
###############    
    