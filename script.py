#!/usr/bin/python3

import os

def clr_msg(msg, verbosity = 0):
    clr_code = ['\033[0m', '\033[94m', '\033[93m', '\033[91m']
    return "%s%s\033[0m" % (clr_code[verbosity], msg)

def print_info(msg):
    print(clr_msg(msg, 1))

def print_warn(msg):
    print(clr_msg(msg, 2))

def print_fatal(msg):
    print(clr_msg(msg, 3))

# List of .* files
list_configs = ['.bashrc', '.emacs']

verbosity = {'INFO':'\033[95m[Info]\033[0m',
             'WARN':'\033[93m[WARN]\033[0m',
             'FAIL':'\033[91m[FAIL]\033[0m'}

src_path  = os.getcwd() + '/'
home_path = os.environ['HOME']# + '/Documents'

# cd to home dir
os.chdir(home_path)
print("I'm in " + os.getcwd())

for config in list_configs:
    print(config)
    # Check if it already exist
    if os.path.exists(config):
        print_warn("WARN: %s exists in %s" %(config, home_path))
    
    print_info("Create symlink: %s -> %s" % (config, src_path+config))
    os.symlink(src_path+config, config)

os.chdir(src_path)
print("Back to %s" % os.getcwd())
