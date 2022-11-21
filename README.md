# 在python上使用sqlite3

## introduction
- sqlite3在python是內建的package，不需要額外import
```python=
import sqlite3
#與資料庫建立連結
conn = sqlite3.connect('<database_name>.db')
#建立cursor讓接下來能夠對資料庫進行操作
c = conn.cursor()

...

#commit our change
c.commit()
#close database
c.close()
```
## Create table
用`CREATE TABLE`建立table

```python=
#create a table 
#execute is case seneitive
c.execute("""CREATE TABLE <database_name>(
    dataname1 datatype1,
    dataname2 datatype2,
    ...
)""")

#commit our change
c.commit()
```

:::info
hint : execute被三個雙引號包圍可以打多行，若只有一個僅限單行
:::
- sqlite裡有五種datatype
    - NULL
    - INTEGER
    - TEXT
    - REAL(float)
    - BLOB(img)
## INSERT
### Insert single data
- 使用 `INSERT INTO <table_name> VALUES <DATA>`去新增單一值
```python=
c.execute("INSERT INTO <table_name> VALUES (?,?,...)",<data_col1>,<data_col2>,...)

conn.commit()

```
### Insert mutiple data
- 方法與新增單一值相同，但必須使用`c.executemany`
```python=
data_array = [
    (data1_col1,data1_col2,...)
    (data2_col1,data2_col2,...)
    ...
]
c.executemany("INSERT INTO customers VALUES (?,?,...)",data_array)
c.commit()
```
## query
### Select
- 用`SELECT rowid, *FROM <table_name>`訪問database
```python=
c.execute("SELECT rowid, *FROM <table_name>")
```
### Fetch
- select完可以用fetch返回database的值
```python=
c.execute("SELECT rowid, *FROM <table_name>")
#加rowid可以替table加上id
c.fetchone() (type:tuple)
c.fetchmany(3)
c.fetchall() (type:list)
print(c.fetchall())
```

### WHERE
- WHERE 可以幫select設定指定條件
```python=
c.execute("SELECT rowid,* FROM <table_name> WHERE <col_name> = <value>")
```
- 也可以使用 AND OR
```python=
c.execute("SELECT rowid,* FROM <table_name> WHERE <col_name> = <value> AND <col_name> != <value>")
```
- LIKE 可用於找尋片段字串
    - ex: LIKE %gmail% = -----gmail-----
    - ex: LIKE %ang = -----ang
```python=
c.execute("SELECT rowid,* FROM <table_name> WHERE LIKE %<string>")
```
- ORDER BY
    - 默認為順序DESC 可以讓搜尋結果倒序
    - 如果參數型態是TEXT則會照字首排列 (a>b>c...)
```python=
c.execute("SELECT rowid, *FROM customers ORDER BY <col_name> DESC")
```
## Edit
### update
使用 `UPDATE <table_name> SET <rename_col> = <value> WHERE <col> = <value>`
```python=
c.execute("""UPDATE <table_name> SET <rename_col> = <value> WHERE <col> = <value>
""")
c.commit()
```
### delete
用`DELETE FROM <table_name> WHERE ...`來刪除指定項(通常使用rowid)
```python=
c.execute("DELETE FROM <table_name> WHERE <col_name> = <value>")
conn.commit()
```
### drop tabe
刪除整個table
```python=
c.execute("DROP TABLE <table_name>")
conn.commit()
```
