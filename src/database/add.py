# -*- coding: utf-8 -*-
import os
import sys
import psycopg2

CWD         = os.path.dirname(os.path.realpath(__file__))
ROOT_DIR    = os.path.dirname(CWD)
sys.path.append(ROOT_DIR)

try:
    conn            = psycopg2.connect(
        database    = "smarterp_okg_pro",
        host        = "192.168.123.116",
        user        = "okg_pro_01",
        password    = "okg_01@2024$kh",
        port        = "5432"
    )
    corsor = conn.cursor()
    corsor.execute("SELECT public.insert_hr_attendance( '58019', '98', 'sophat', 'Check-in', '0', '04-11-2023', '07:31:33', '2023-11-04 07:31:33' )")
    corsor.close()  # then close cursor
    conn.commit()   # commit query
    conn.close()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)