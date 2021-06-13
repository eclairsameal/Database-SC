# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 16:10:00 2021

@author: Fenrir

Description :
    連接 mysql
"""
import pymysql
import csv

# 資料庫設定
db_settings = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "",
    "charset": "utf8"
}
database = 'shinycolor'
tablename = "idol"

# 連接 mysql 並創建 database
try:
    conn = pymysql.connect(**db_settings)    # 建立Connection物件
    # 建立Cursor物件
    with conn.cursor() as cursor:
        # 創建 database
        sql = "CREATE DATABASE " + database + " COLLATE utf8_general_ci;"
        cursor.execute(sql)    # 執行 sql 
except Exception as ex:
    print(ex)

# 讀csv檔案並區分資料，方便建立資料表
filename = "SCdata(table).csv"
with open(filename, "r", encoding="utf-8") as f:
    csvreader = csv.reader(f)        # 讀檔案指標建立Reader物件
    headers = next(csvreader)        # 欄位名稱
    column_type = next(csvreader)    # 資料型態
    column_notnull = next(csvreader) # 是否能為空值
    primarykey = next(csvreader)     # 是否為主鍵
    rowslist = list(csvreader)       # 資料
# print(f'headers: {headers}')
# print(f'column_type: {column_type}')
# print(f'column_notnull: {column_notnull}')
# print(f'primarykey: {primarykey}')
# print(rowslist)

# 連接資料庫並建立資料表(TABLE)
db_settings["database"] = database
# print(db_settings)
try:
    conn = pymysql.connect(**db_settings)    # 建立Connection物件
    # 建立Cursor物件
    with conn.cursor() as cursor:
        # 創建 database
        headers_len = len(headers)
        column_set_string = [headers[i] + " "+ column_type[i] + " NOT NULL,"if column_notnull[i] == "1" 
                             else headers[i] + " "+ column_type[i] + ","for i in range(headers_len)]
        sql = "CREATE TABLE " + tablename + "(" + ''.join(column_set_string)
        # 主鍵 SQL
        sql += ''.join(["PRIMARY KEY(" + headers[i] for i in range(headers_len)if primarykey[i] == "1"]) + "));"
        #print(sql)
        cursor.execute(sql)    # 執行 sql
        # 有修正空間
        sql_insert = "INSERT INTO idol \
        (idol_id,idol_name,idol_unit,idol_cv,idol_age,idol_height,idol_birthday,idol_birthplace,idol_bloodtype) \
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.executemany(sql_insert, rowslist)
        conn.commit()
except Exception as ex:
    print(ex)



