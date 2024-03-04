# -*- coding: utf-8 -*-
import json
import os
import psycopg2

# Get config file
def get_config() : 
    with open(os.getcwd() + '/config.json') as config:
        conf = json.load(config)
    return conf

# get database configured from config.json file
def get_database_config() : 
    conf = get_config()
    database = conf['database']
    return database

# databases configured
database_conf = get_database_config()

# Question for Configured database's name
print( "Configured database name: \033[96m(check file config.json) \033[0m", end = ": ", flush = True )

# Answer value
server_name = input()

try :
    for dbname in database_conf:
        if server_name.lower() == dbname.lower() :
            # connect to database
            conn = psycopg2.connect(
                database    = database_conf[dbname]['name'],
                host        = database_conf[dbname]['host'],
                user        = database_conf[dbname]['user'],
                password    = database_conf[dbname]['password'],
                port        = database_conf[dbname]['port']
            )

            if conn.cursor() :
                print("🗃️ \033[93mServer Name:\033[0m \033[92m{} \033[0m".format(dbname.upper()))
                print("🚀 \033[93mServer Host:\033[0m \033[92m{} \033[0m".format(database_conf[dbname]['host']))
                print("🚀 \033[93mDB Name:\033[0m \033[92m{} \033[0m".format(database_conf[dbname]['name']))
                print("🚀 \033[93mUser Name:\033[0m \033[92m{} \033[0m".format(database_conf[dbname]['user']))
                print("⛓️  \033[92mDatabase Connection: OK ✅ \033[0m")
                conn.cursor().close()

except Exception as e:
    print ("Process terminate : {}".format(e))
finally:
    if conn:
        conn.close()
    exit()