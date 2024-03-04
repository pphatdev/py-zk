# -*- coding: utf-8 -*-
import os
import sys

CWD         = os.path.dirname(os.path.realpath(__file__))
ROOT_DIR    = os.path.dirname(CWD)
sys.path.append(ROOT_DIR)

from fingerprint import print_data_from_fingerprint
from src.database.helpers import get_fingerprint_config
fingerprint   = get_fingerprint_config()

conn    = None
for fpname in fingerprint :
    # get from json
    print_data_from_fingerprint(fpname)

# This file will push data to attendance.json