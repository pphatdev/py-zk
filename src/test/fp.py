# -*- coding: utf-8 -*-
import json
import os
import sys

# Import ZK
from zk import ZK

# Set default connection
conn = None

# Get config file
def get_config() :
    with open(os.getcwd() + '/config.json') as config:
        conf = json.load(config)
    return conf

# get fingerprints configured from config.json file
def get_fingerprint_config() :
    conf = get_config()
    database = conf['fingerprint']
    return database

# fingerprints Configured
fingerprints = get_fingerprint_config()

# Question for Configured fingerprint's name
print( "Configured fingerprint name: \033[96m(check file config.json) \033[0m", end = ": ", flush = True )

# Answer value
fpname = input()


try:
    for name in fingerprints :
        if name == fpname :

            print("\033[93m⏳ Please wait afew seconds...  \033[0m")
            zk = ZK(fingerprints[name]['ip'], int(fingerprints[name]['port']))

            conn = zk.connect()
            conn.disable_device()
            print("\033[92m✅ Configured Name: {} \033[0m".format(name.upper()))
            print("\033[92m✅ IP Address: {} \033[0m".format(fingerprints[name]['ip']))
            print("\033[92m✅ IP Address: {} \033[0m".format(fingerprints[name]['port']))
            print("\033[92m✅ Connection: OK !! \033[0m")
            conn.enable_device()
    exit()
except Exception as e:
    print ("Process terminate : {}".format(e))
finally:
    if conn:
        conn.disconnect()
    exit()