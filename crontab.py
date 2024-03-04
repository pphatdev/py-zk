# Export User to Attendance 
import subprocess
import os
import sys

CWD         = os.path.dirname(os.path.realpath(__file__))
ROOT_DIR    = os.path.dirname(CWD)
sys.path.append(ROOT_DIR)

from src.database.helpers import defined_path, get_processor


def test_crontab() :
    with open(defined_path() + "/data/crontab.txt", "w+") as attendance :
        subprocess.call(
            [get_processor(), defined_path() + "/src/test/cron.py"], 
            stdout = attendance
        )
test_crontab()