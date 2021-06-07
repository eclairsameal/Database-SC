# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 16:10:00 2021

@author: Fenrir

Description :
    連接 mysql
"""
import pymysql

# 資料庫設定
db_settings = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "",
    "charset": "utf8"
}
database = 'shinycolor'

try:
    conn = pymysql.connect(**db_settings)    # 建立Connection物件
    # 建立Cursor物件
    with conn.cursor() as cursor:
        # 資料表相關操作
        sql = "CREATE DATABASE " + database + " COLLATE utf8_general_ci;"
        cursor.execute(sql)
except Exception as ex:
    print(ex)