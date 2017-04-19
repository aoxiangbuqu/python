from scrapy.cmdline import execute
execute(['scrapy', 'crawl', 'dmoz'])
"""
import pymysql
 
conn = pymysql.connect(host="127.0.0.1",port=3306,user="fang",passwd="fang",db="fang",charset="utf8")
 
cur = conn.cursor()
 
sql = "select * from fang_base"
 
cur.execute(sql)

rows = cur.fetchall()

print(rows)
"""