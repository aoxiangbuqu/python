from .sql import Sql
from tutorial.items import DmozItem


class FangPiepeline(object):
    def process_item(self,item, spider):
        title=item['title']
        name = item['name']
        address = item['address']
        houseType = item['houseType']
        allPrice = item['allPrice']
        avePrice = item['avePrice']
        area = item['area'] 
        Sql.inser_date(title,name, address, houseType, allPrice, avePrice, area)
        print("begin....")