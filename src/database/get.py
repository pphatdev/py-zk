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
    corsor.execute("SELECT * from public.ma_user")
    old_data = corsor.fetchall()
    print(old_data)
    corsor.close()  # then close cursor
    conn.commit()   # commit query
    conn.close()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)