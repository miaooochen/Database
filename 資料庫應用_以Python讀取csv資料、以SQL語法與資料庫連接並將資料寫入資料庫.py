#以Python讀取csv資料、以SQL語法與資料庫連接並將資料寫入資料庫
import csv,sqlite3
#讀取檔案
with open('109各鄉鎮市區人口密度1.csv','r',encoding='utf-8')as csvinfile:
    csvreader = csv.reader(csvinfile)
    csvlist = list(csvreader)
#連接資料庫 並新建欄位    
conn = sqlite3.connect('population2.db')
cursor = conn.cursor()
sql ='CREATE TABLE IF NOT EXISTS population\
(id Integer primary key AUTOINCREMENT,統計年 int,區域別 varchar(50),年底人口數 int,土地面積 int,人口密度 int)'
cursor.execute(sql)
#輸入109各鄉鎮市區人口密度資料至資料庫
for i in range(2,372):  
    sql2 = 'INSERT OR IGNORE INTO population(統計年,區域別,年底人口數,土地面積,人口密度)\
    VALUES("{0}","{1}","{2}","{3}","{4}")'#values內必為字串
    sql2 = sql2.format(csvlist[i][0],csvlist[i][1],csvlist[i][2],csvlist[i][3],csvlist[i][4])   
    cursor.execute(sql2)
    
conn.commit()#創表及篩選不需要 插入資料才需要
#篩選有新北市開頭的資料
sql3 = 'SELECT * FROM population LIMIT 5 '#WHERE 區域別 = "新北市%"
cur = cursor.execute(sql3)
rows = cur.fetchall()
print(rows)
'''for i in range(len(rows)):
    if i < 5:
        print(rows[i])'''
#關閉資料庫連接
conn.close()

'''for i in range(len(data)):
            sql = """INSERT INTO towndata (year, site, people_total, area, population)
                                    VALUES (%s, %s, %s, %s, %s)"""
            var = (data.iloc[i,0], data.iloc[i,1], data.iloc[i,2], data.iloc[i,3], data.iloc[i,4])     
            cursor.execute(sql, var)'''