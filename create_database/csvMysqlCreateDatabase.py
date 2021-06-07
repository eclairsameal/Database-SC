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
"""
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
"""

# 讀csv檔案並區分資料，方便建立資料表
filename = "SCdata(table).csv"
with open(filename, "r", encoding="utf-8") as f:
    csvreader = csv.reader(f)        # 讀檔案指標建立Reader物件
    headers = next(csvreader)        # 欄位名稱
    column_type = next(csvreader)    # 資料型態
    column_notnull = next(csvreader) # 是否能為空值
    primarykey = next(csvreader)     # 是否為主鍵)
    rowslist = list(csvreader)       # 資料

print(f'headers: {headers}')
print(f'column_type: {column_type}')
print(f'column_notnull: {column_notnull}')
print(f'primarykey: {primarykey}')
print(rowslist)