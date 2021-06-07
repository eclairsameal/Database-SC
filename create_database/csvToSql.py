import csv
filename = "shiny colors data.csv"
with open(filename, encoding="utf-8") as csvFile:    # 開啟檔案
    csvReader = csv.reader(csvFile)    # 讀檔案建立Reader物件
    listReport = list(csvReader)    # 將資料變成 LIST(可在 with 外使用 )
#print(listReport)

title = listReport.pop(0) # 取出屬性欄位
print("pop = {}".format(title))

# 寫死
# INSERT INTO idol VALUES ( "idol01", "櫻木 真乃", "illumination STARS", "関根瞳", 16, 155, "2005-04-25", "東京", "A");
for row in listReport:
    sql_insert = """ INSERT INTO idol VALUES ( "{}", "{}", "{}", "{}", {}, {}, "{}", "{}", "{}"); """.format(
        row[0], row[1], row[2], row[3], int(row[4]), int(row[5]), row[6], row[7], row[8],)
    print(sql_insert)

# 判斷屬性欄位來產生語法
title_len = len(title)
for row in listReport:
    sql_insert = "INSERT INTO idol VALUES ("
    for i in range(title_len):
        if i == title_len-1:
            sql_insert += """"{}");""".format(row[i])
        else:
            sql_insert += """ "{}", """.format(row[i])
    print(sql_insert)
