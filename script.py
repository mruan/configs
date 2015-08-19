#!/usr/bin/python3

import os
from sys import exit

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
list_configs = ['.bashrc', 
                '.emacs']

src_dir  = os.getcwd() + '/'
home_dir = os.environ['HOME'] + '/Documents'

# cd to home dir
os.chdir(home_dir)

print("The following config files will be created in %s" % home_dir)
for config in list_configs:
    print_warn(config)
answer = input("Shall we begin [y/n]> ")
if answer[0] != 'Y' and answer[0] != 'y':
    print("Nothing is done.")
    exit(0)

for config in list_configs:
    # Check if it already exist
    if os.path.exists(config):
        print_warn("WARN: %s exists in %s" %(config, home_dir))
        # Create a backup copy just in case
        print_warn("Back up %s to %s" % (config, config+'.bk'))
        os.rename(config, config+'.bk')

    # Create symbolic link 
    print_info("Create symlink: %s -> %s\n" % (config, src_dir+config))
    os.symlink(src_dir+config, config)

os.chdir(src_dir)
