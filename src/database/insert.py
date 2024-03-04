# -*- coding: utf-8 -*-
from datetime import datetime
import os
import sys

CWD         = os.path.dirname(os.path.realpath(__file__))
ROOT_DIR    = os.path.dirname(CWD)
sys.path.append(ROOT_DIR)

from helpers import get_database_config
from base import insert_data

try :
    # Get All database config
    database   = get_database_config()

    # Foreach Database serve name (key)
    for key in database:
        # Execute insert_data()
        print("{} - {} >: ============================".format(key.upper(), datetime.now()))
        insert_data(key)

except Exception as e:
    print ("Process terminate : {}".format(e))

finally:
    exit()