#!/usr/bin/env py
import os
import sys
from datetime import datetime

CWD         = os.path.dirname(os.path.realpath(__file__))
ROOT_DIR    = os.path.dirname(CWD)
sys.path.append(ROOT_DIR)

from exports import exports_attendance
from src.database.helpers import convert_bytes, defined_path, get_fingerprint_config

if __name__ == '__main__' :
    # print("Downloading users! Please wait amoment...", end='\n', flush=True)
    print("\033[93m⏳ Please wait amoment... \033[0m")
    print("\033[93m⏳ Checking fingerprint connections... \033[0m")

    fingerprints = get_fingerprint_config()
    for key in fingerprints :
        print("{} >: =============== {} =============".format(key.upper(), datetime.now()))

    exports_attendance("attendance", 'json')
    file_name   = defined_path() + "/data/attendance.json"
    size        = convert_bytes(file_name)
    print("\033[93m♻️  Download size: {} \033[0m".format(size))
    print("\033[92m✅ Downloading: Completed!! \033[0m")
