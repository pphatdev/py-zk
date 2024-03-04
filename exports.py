#!/usr/bin/env py
import subprocess
from multiprocessing import Process
from src.database.helpers import defined_path, get_processor

# Export User to Attendance 
def exports_attendance( filename = "attendance", extension = "json" ) :
    to_path = "/data/{}.{}".format(filename, extension)
    with open(defined_path() + to_path, "w+") as attendance :
        return subprocess.call(
            [get_processor(), defined_path() + "/src/get_attendance.py"], 
            stdout= attendance
        )

if __name__ == '__main__' :
    print("Which data do you want to export ? [attendance]: ", flush=True)
    value = input()
    print("Downloading attendance! Please wait amoment...", end='\n', flush=True)
    attendance = Process(target = exports_attendance("attendance", 'json'))
    attendance.start()
    print("Downloading Completed ✅✅", end='\n')