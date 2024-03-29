# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 21:04:18 2021

@author: Fenrir

Description :

Variable:
    
Algorithm/Calculation:
"""
import csv
"""
filename = "shiny colors data.csv"
with open(filename, encoding="utf-8") as csvFile:    # 開啟檔案
    csvReader = csv.reader(csvFile)    # 讀檔案建立Reader物件
    for row in csvReader:  # csvReader 只能在 with 裡使用
        #print("Row {} = {}".format(csvReader.line_num, row))

"""
filename = "shiny colors data.csv"
with open(filename, encoding="utf-8") as csvFile:    # 開啟檔案
    csvReader = csv.reader(csvFile)    # 讀檔案建立Reader物件
    listReport = list(csvReader)    # 將資料變成 LIST(可在 with 外使用 )
#print(listReport)

title = listReport.pop(0) # 取出屬性欄位
# print("pop = {}".format(title))

# 寫死直接帶入
# INSERT INTO idol VALUES ( "idol01", "櫻木 真乃", "illumination STARS", "関根瞳", 16, 155, "2005-04-25", "東京", "A");
for row in listReport:
    sql_insert = " INSERT INTO idol VALUES ( \"{}\", \"{}\", \"{}\", \"{}\", {}, {}, \"{}\", \"{}\", \"{}\"); ".format(
        row[0], row[1], row[2], row[3], int(row[4]), int(row[5]), row[6], row[7], row[8])
    #print(sql_insert)

# 判斷屬性欄位來產生語法
title_len = len(title)
for row in listReport:
    sql_insert = "INSERT INTO idol VALUES ("
    for i in range(title_len):
        if i == title_len-1:
            sql_insert += " \"{}\"); ".format(row[i])
        else:
            sql_insert += " \"{}\", ".format(row[i])
    #print(sql_insert)

# 判斷屬性欄位來產生語法，並將結果寫到 insert.sql 裡
output_fn = "insert.sql"
with open(output_fn, 'w', encoding = "utf-8") as file_output:
    title_len = len(title)
    for row in listReport:
        sql_insert = "INSERT INTO idol VALUES ("
        for i in range(title_len):
            if i == title_len-1:
                sql_insert += "\"{}\");".format(row[i])
            else:
                sql_insert += "\"{}\", ".format(row[i])
        print(sql_insert)
        file_output.write(sql_insert+"\n")