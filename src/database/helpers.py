# -*- coding: utf-8 -*-
import os
import sys
import json
# import glob

CWD         = os.path.dirname(os.path.realpath(__file__))
ROOT_DIR    = os.path.dirname(CWD)
sys.path.append(ROOT_DIR)



# Get raw from file
def get_data(path='') : 
    with open(defined_path() + path, 'r') as config:
        return config.read()
    
# Get config file
def get_config() : 
    with open(defined_path()+'/config.json') as config:
        conf = json.load(config)
    return conf

# Get config file
def get_processor() :
    with open(defined_path()+'/config.json') as config:
        conf = json.load(config)
    return conf['processor']


# Get only database from config
def get_database_config() :
    conf = get_config()
    database = conf['database']
    return database

# Get only database from config
def get_fingerprint_config() :
    conf = get_config()
    database = conf['fingerprint']
    return database

# Get Backdate
def get_backdate_config() :
    conf        = get_config()
    database    = conf['backdate']
    return database

# minimize and format raw data
def min_raw_data(data) :
    remove_space = data.replace(' ','')
    data = remove_space.replace('\n', '')
    return data

# minimize and format json data
def get_json_data(data) :
    remove_space = data.replace(' ','')
    data = remove_space.replace('\n', '')
    return data.replace('},]','}]')

# get user data form json
def get_users() :
    file        = get_data('/data/users.json')
    strdata     = get_json_data(file)
    return json.loads(strdata)


# get attendance data form json
# Merging multi data form json files
# def get_from_json_files() : 
#     new_data    = []
#     files       = glob.glob(dir_fd="./data/", pathname="*.json")
#     for file in files:
#         data        = get_data('/data/' + file)
#         json_data   = get_json_data(data)
#         new_data    += json.loads(json_data)
#     return new_data

# get attendance data form json
def get_attendance_from_json() :
    file    = get_data('/data/attendance.json')
    data    = get_json_data(file).replace('][', ',').replace('[,', '[')
    return json.loads(data)


# calculate file size in KB, MB, GB
def convert_bytes(path):
    size = os.path.getsize(path)
    """ Convert bytes to KB, or MB or GB"""
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return "%3.1f %s" % (size, x)
        size /= 1024.0

def defined_path():
    cwd         = os.getcwd()
    cron_path   = "/home/developer"
    server_path = "/var/www/html/py-attendance"

    if cwd.replace("/","") != cron_path.replace("/","") :
        path = cwd
    else :
        path = server_path
    return path