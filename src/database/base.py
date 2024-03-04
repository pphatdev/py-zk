# -*- coding: utf-8 -*-
import os
import sys
from datetime import datetime
import psycopg2

CWD         = os.path.dirname(os.path.realpath(__file__))
ROOT_DIR    = os.path.dirname(CWD)
sys.path.append(ROOT_DIR)

from helpers import get_attendance_from_json, get_backdate_config, get_database_config

def insert_data(servername = "sit") :
    servername      = servername.lower()
    data            = get_attendance_from_json()

    database_conf   = get_database_config()
    print("\033[93m⏳ Checking Server {} and database connections... \033[0m".format(servername.upper()))
    conn            = psycopg2.connect(
        database    = database_conf[servername]['name'],
        host        = database_conf[servername]['host'],
        user        = database_conf[servername]['user'],
        password    = database_conf[servername]['password'],
        port        = database_conf[servername]['port']
    )
    corsor = conn.cursor()
    if corsor :
        print("\033[92m✅ Host: {}\033[0m".format(database_conf[servername]['host']))
        print("\033[92m✅ Name: {}\033[0m".format(database_conf[servername]['name']))
        print("\033[92m✅ Connected to database !!\033[0m")
    else :
        print("\033[93m⛔ Host: {}\033[0m".format(database_conf[servername]['host']))
        print("\033[93m⛔ Name: {}\033[0m".format(database_conf[servername]['name']))
        print("\033[93m⛔ Connection Problem !!\033[0m")

    date    = datetime.now()
    print("\033[93m⏳ Inserting! Please wait afew seconds... \033[0m")
    total = 0

    for item in data :
        id                      = item['id']
        user_id                 = item['user_id']
        username                = user_id
        scanning_type           = item['scanning_type']
        scanning_type_id        = item['scanning_type_id']
        current_timing_str      = date.strftime(get_backdate_config())
        current_timing          = datetime.strptime( current_timing_str, "%Y-%m-%d %H:%M:%S" )
        attendance_timing_str   = str(item['scaning_timestamp'])
        attendance_timing_stamp = datetime.strptime( attendance_timing_str, "%Y-%m-%d%H:%M:%S" )
        attendance_date         = item['scaning_date']
        attendance_time         = item['scaning_time']

        if attendance_timing_stamp >= current_timing :

            # Check existing data
            corsor.execute("SELECT * FROM hr_attendance WHERE \"deviceID\" = '{}' AND \"deviceStamp\" = '{}'".format(
                user_id,
                attendance_timing_stamp
            ))
            old_data = corsor.fetchall()

            # insert id not exist
            if len(old_data)  <= 0:
                total += 1
                corsor.execute("SELECT public.insert_hr_attendance( '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}' )".format(
                    id, # 58019
                    user_id, # 98
                    username, # sophat
                    scanning_type, # Check-in
                    scanning_type_id, # 0
                    attendance_date, # 04-11-2023
                    attendance_time, # 07:31:33
                    attendance_timing_stamp # 2023-11-04 07:31:33
                ))
                print("\033[92m✅ Inserting User id: {} !! \033[0m".format(user_id))

    if total <= 0 :
        print("\033[93m♻️⚠️ Everything already up-to-date.\033[0m")
    else : 
        user = "users"
        print("\033[93m♻️  Total: {} new {}!! \033[0m".format(total,user))
        print("\033[92m✅ Inserting: Completed!! \033[0m".format(total))

    conn.commit() # commit query
    corsor.close() # then close cursor
    conn.close()