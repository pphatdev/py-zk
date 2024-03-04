#!/usr/bin/env py
import subprocess
import os
import sys

CWD         = os.path.dirname(os.path.realpath(__file__))
ROOT_DIR    = os.path.dirname(CWD)
sys.path.append(ROOT_DIR)

from src.database.helpers import defined_path, get_processor

print("Download Processing...")
subprocess.call(
    [get_processor(), defined_path() + "/exports_attendance.py"],
    text = True
)

subprocess.call(
    [get_processor(), defined_path() + "/src/database/insert.py"],
    text = True
)