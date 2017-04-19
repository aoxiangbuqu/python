# -*- coding: utf-8 -*-
import pymysql
from .setting import *

MYSQL_HSOT =DB_CFG_MYSQL["host"]
MYSQL_USER =DB_CFG_MYSQL["user"]
MYSQL_PWD =DB_CFG_MYSQL["pwd"]
MYSQL_PORT =DB_CFG_MYSQL["port"]
MYSQL_DB =DB_CFG_MYSQL["database"]

conn = pymysql.connect(host = MYSQL_HSOT, user = MYSQL_USER, passwd = MYSQL_PWD,
                                      db = MYSQL_DB, port = MYSQL_PORT,charset="utf8")

cur = conn.cursor()


class Sql:
    @classmethod
    def inser_date(cls,title,name,address,houseType,allPrice,avePrice,area):
        sql="""
             insert into fang_base(title,name,address,houseType,allPrice,avePrice,area) 
             values ("%s","%s","%s","%s","%s","%s","%s")""" %(title,name,address,houseType,allPrice,avePrice,area)
        #print(sql)
        cur.execute(sql)
        if name:
            print('have data')
            cur.execute('commit')
        else:
            print('end。。。。。。')
            conn.close()