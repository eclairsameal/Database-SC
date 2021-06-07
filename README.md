# はつき的資料庫教室
###### tags: `Database` `目錄`


[shiny colors data](https://docs.google.com/spreadsheets/d/17NubQX0O8iPIBVS0WRVaM3t5pIeMs3UEeFGO_T3WnWE/edit?usp=sharing)

以Shiny Colors的資料例來學習資料庫基本語法及知識。

## 關聯式資料庫
關聯式資料庫是目前最多軟體開發者使用的資料庫系統，常見如 MySQL、PostgreSQL、Microsoft SQL Server、SQLite。

關聯式資料庫的三個特質：
1. 資料是以一個或是多個資料表 (Table) 的方式存放
在關聯式資料庫裡，每一筆資料都是資料表(Table)中的一個紀錄(record)，然後再把不同的 Table 集合起來，就成為一個關聯式資料庫。
2. 資料之間有明確的關聯
3. 關聯式資料庫是以 SQL 語言操作

## SQL 語言
SQL (Structured Query Language 結構化查詢語言) 是一種專門用來管理與查詢關聯式資料庫的程式語言。
SQL 主要是以 keyword 關鍵字和資料表（table）名稱和屬性欄位（column）名稱當作一段完整的語句。
SQL 語法使用分號 ; 當作結尾，英文字母不區分大小寫，單字間使用空白分隔。單行註解寫法 --，多行註解使用 /**/ 包裹。

### DDL（Data Definition Language）
DDL 又稱為資料定義語言，主要用來定義資料庫的結構，能建立或刪除資料庫和資料表等用來儲存的單位。
[基本語法](https://hackmd.io/BbsOAfY9T5Sb1iVotEIefQ?edit)
[](https://)
###  DML（Data Manipulation Language）
DML 能查詢或修改資料表的紀錄。

[INSERT INTO](https://hackmd.io/FpqLSy04Q1qLGYNf1Mceqw?both)
[UPDATE](https://hackmd.io/iaxLtQ_pQT-v09Y3BPr3_Q?both)
[SELECT](https://hackmd.io/cN20hSX6Sf-nD5dbcq6ALQ)

###  DCL（Data Control Language）
DCL 為可用來取消操作和設定操作權限的指令。

