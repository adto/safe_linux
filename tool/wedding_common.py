from enum import Enum
import functools
import time
from subprocess import Popen, PIPE
import shlex #For string -> args conversion

#Execute command in subprocess
def execute(arg_string, synch_flag=False):
    print(arg_string)
    process_handler = Popen(shlex.split(arg_string),stdout=PIPE, stderr=PIPE)
    if synch_flag:
        process_handler.wait()
    return process_handler

def timeit(func):
    @functools.wraps(func)
    def new_func(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        elapsed_time = time.time() - start_time
        print('function [{}] finished in {} ms'.format(
            func.__name__, int(elapsed_time * 1_000)))
        return result
    return new_func


#define colors
class c:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# define possible actions
class Action(Enum):
    migrate = 'migrate'
    analyse = 'analyse'
    x = 'x'
    y = 'y'
    def __str__(self): 
        return self.value
