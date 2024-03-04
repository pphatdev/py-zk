# -*- coding: utf-8 -*-
import os
import sys
from datetime import datetime
import json

CWD         = os.path.dirname(os.path.realpath(__file__))
ROOT_DIR    = os.path.dirname(CWD)
sys.path.append(ROOT_DIR)


from zk import ZK
from src.database.helpers import get_fingerprint_config, get_backdate_config
fingerprint   = get_fingerprint_config()

# so main branch get all data
def print_data_from_fingerprint(name = "fp_name") :
    try :
        conn    = None
        zk      = ZK(ip = fingerprint[name]['ip'] , port = int(fingerprint[name]['port']) )

        # Connect to fingerprint
        conn    = zk.connect()

        # Disable Device first
        conn.disable_device()
        date    = datetime.now()

        print ('[')
        attendances = conn.get_attendance()

        for attendance in attendances :
            status = "Check-in"
            if attendance.punch == 1:
                status = "Check-out"

            # get datetime attendance and convert to string
            # example: "2023-11-01 00:00:00"
            attendance_timing_str   = str(attendance.timestamp)

            # set current date to string
            # example: "2023-11-01 00:00:00"
            current_timing_str      = date.strftime(get_backdate_config())

            # convert string to full datetime for compare
            attendance_timing       = datetime.strptime( attendance_timing_str, "%Y-%m-%d %H:%M:%S" )
            current_timing          = datetime.strptime( current_timing_str, "%Y-%m-%d %H:%M:%S" )

            # Scanning timestamp
            scanning_timestamp      = attendance.timestamp
            scanning_date           = datetime.date(scanning_timestamp).strftime("%d-%m-%Y")
            scanning_time           = datetime.time(scanning_timestamp).strftime("%H:%M:%S")

            # If attendance bigger than current date and time 00:00:00
            # example:  "2023-11-01 00:00:00"
            if attendance_timing >= current_timing :
                print(
                    "{",
                        "{}:{},".format( json.dumps("id"), json.dumps(str(attendance.uid)) ),
                        "{}:{},".format( json.dumps("user_id"), json.dumps(str(attendance.user_id)) ),
                        "{}:{},".format( json.dumps("scaning_timestamp"), json.dumps(str(scanning_timestamp)) ),
                        "{}:{},".format( json.dumps("scaning_date"), json.dumps(str(scanning_date)) ),
                        "{}:{},".format( json.dumps("scaning_time"), json.dumps(str(scanning_time)) ),
                        "{}:{},".format( json.dumps("scanning_type"), json.dumps(str(status)) ),
                        "{}:{},".format( json.dumps("scanning_type_id"), json.dumps(str(attendance.punch)) ),
                        "{}:{}".format( json.dumps("status"), json.dumps(str(attendance.status)) ),
                    "},"
                )
        print ("]")
        conn.enable_device()
        conn.disconnect()
    except Exception as e:
        print ("Process terminate : {}".format(e))

    finally:
        exit()