# -*-coding:utf8 -*-
import scrapy 
from bs4 import BeautifulSoup
from scrapy.http import Request 
from test.test_threading_local import target
import re
from  tutorial.items import DmozItem
import time
class Myspider(scrapy.Spider):
 
    name = 'dmoz'
    allowed_domains = ['23wx.com']
    bash_url = 'http://esf.xian.fang.com/house-a0482/'
    bashurl = '.htm'
 
    def start_requests(self):
        for i in range(1, 50):
            url = self.bash_url + 'i3'+str(i)
            print(url)
            time.sleep(1)
            yield Request(url, self.parse)
        #yield Request('http://www.bxwx9.org/bsort1/0/1.htm', self.parse)
 
    def parse(self, response):
        #tds = BeautifulSoup(response.text,'lxml').select('.houseList')
        item = DmozItem()
        tds = BeautifulSoup(response.text,'lxml').find_all("div", class_="houseList")
        for td in tds:
            for t in td.find_all("dl",class_="list rel"):
                item['title']=t.find("p",class_="title").get_text()
                item['name']=t.find("p",class_="mt10").contents[1].string
                item['address']=t.find("p",class_="mt10").contents[3].string
                a = ''
                house_type=t.find("p",class_="mt12").stripped_strings
                for hou in house_type:
                    a =a+hou
                    #print(a)
                item['houseType']=a
               
                item['allPrice']=t.find("p",class_="mt5 alignR").get_text()
                #print("单价:"+t.find("p",class_="danjia alignR mt5").contents[0].string)
                item['avePrice']=t.find("p",class_="danjia alignR mt5").get_text()
                item['area']=t.find("div",class_="area alignR").contents[1].string
                yield item
                #for child in t.find("p",class_="mt10"):
                #    print(child.string)
    
                #for d in t.find_all("p",class_="mt10"):
                  
            
          
            
          
            