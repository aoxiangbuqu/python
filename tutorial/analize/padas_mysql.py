# -*- coding:utf8 -*-
import pandas as pd
import pymysql
from pylab import *
mysql_cn= pymysql.connect(host='localhost', port=3306,user='fang', passwd='fang', db='fang',charset='utf8')
df = pd.read_sql('select substring_index(avePrice,"元",1) as avp  from fang_base order by id ;', con=mysql_cn)

#print(df.values)
a = df.iloc[1:1000]

print(a)

figure(figsize=(10,6), dpi=80)
subplot(1,1,1)
plot(a)
show()



mysql_cn.close()