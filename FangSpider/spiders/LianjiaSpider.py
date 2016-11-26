# -*- coding:utf-8 -*-
import scrapy, re, json, sys
from bs4 import BeautifulSoup
import time
from FangSpider.items import FangSpiderItem
reload(sys)
sys.setdefaultencoding('utf-8')

class LianjiaSpider(scrapy.Spider):
    name = "lianjia2"
    allowed_domains = ["http://sh.lianjia.com/"]
    start_urls = (
        'http://sh.lianjia.com/ershoufang/pudongxinqu/',
    )
    regions=['xuhui']
    def start_requests(self,_regions=regions):
        '''需爬取的链接'''
        reqs = []
        for region in _regions:
            for i in range(1,101):
                req = scrapy.Request("http://sh.lianjia.com/ershoufang/"+region+"/d%s"%i)
                #print region,u'第----------------------------------------------------------------'
                reqs.append(req)
        return reqs

    def parse(self, response):
        base_url='http://sh.lianjia.com'
        items = []
        res=response.body
        soup=BeautifulSoup(res,'html.parser')
        soup.encode('utf-8')
        for fang in  soup.select('.info-panel'):
               item = FangSpiderItem()
               item['fang_key']=fang.select('h2')[0].a['key'].strip()
               item['fang_desc']=fang.select('h2')[0].text.strip()
               item['fang_url']=base_url+fang.select('h2')[0].a['href'].strip()
               item['price']=fang.select('.price')[0].text.strip()
               item['price_pre']=fang.select('.price-pre')[0].text.strip()
               item['xiaoqu']=fang.select('.where')[0].a.text.strip()
               item['huxing']=fang.select('.where')[0].contents[3].text.strip()
               item['mianji']=fang.select('.where')[0].contents[5].text.strip()
               item['bankuai']=''
               item['chaoxiang']=''
               item['age']=''
               item['subway']=''
               item['taxfree']=''
               item['haskey']=''
               item['col_look']=''
               item['quyu']=fang.select('.con')[0].contents[1].text.strip()
               #item['bankuai']=fang.select('.con')[0].contents[3].text.strip()
               if len(fang.select('.con')[0].contents) >=4 :
                   item['louceng']=fang.select('.con')[0].contents[4].string.strip()
               if len(fang.select('.con')[0].contents) >=6 :
                   item['chaoxiang']=fang.select('.con')[0].contents[6].string.strip()
               if len(fang.select('.con')[0].contents) >=8 :
                   item['age']=fang.select('.con')[0].contents[8].string.strip()
               if len(fang.select('.con')[0].contents) > 9 :
                   item['age']=fang.select('.con')[0].contents[-1].string.strip()
               if len(fang.select('.fang-subway-ex')) >0 :
                    item['subway']=fang.select('.fang-subway-ex')[0].text.strip()
               if len(fang.select('.taxfree-ex')) >0 :
                    item['taxfree']=fang.select('.taxfree-ex')[0].text.strip()
               if len(fang.select('.haskey-ex')) >0 :
                    item['haskey']=fang.select('.haskey-ex')[0].text.strip()
               if len(fang.select('.square')) >0 :
                    item['col_look']=fang.select('.square')[0].span.text.strip()
               #print u'在售：', u'房源编号:',item['fang_key'],u'房源描述:',item['fang_desc'],\
               #  u'区域:',item['quyu'],u'版块:',item['bankuai'], u'楼层:',item['louceng'],u'朝向:',item['chaoxiang'],u'房龄:',item['age'],\
               #  u'小区:',item['xiaoqu'],u'户型 :', item['huxing'],u'面积:',item['mianji'],\
               #  u'总价:',item['price'],u'单价:',item['price_pre'],u'看房人数:',item['col_look']#,u'房源链接:',item['fang_url']#\
               #  #u'交通 :',item['subway'],u'税费:',item['taxfree'],u'钥匙:',item['haskey'],u'房源链接:',item['fang_url']
               #print u'在售：',  item['fang_key'],item['fang_desc'],\
               #   item['quyu'] ,item['louceng'], item['chaoxiang'], item['age'],\
               #   item['xiaoqu'] , item['huxing'],item['mianji'],\
               #   item['price'],item['price_pre'],item['col_look']#,u'房源链接:',item['fang_url']#\
                 #u'交通 :',item['subway'],u'税费:',item['taxfree'],u'钥匙:',item['haskey'],u'房源链接:',item['fang_url']
               items.append(item)
        #print '-----Spider items----------------------------------------------------------------'

        #for item in items:
        #     print u'在售：', u'房源编号:',item['fang_key'],u'房源描述:',item['fang_desc'],u'房源链接:',item['fang_url'],\
        #         u'区域:',item['quyu'],u'版块:',item['bankuai'], u'楼层:',item['louceng'],u'朝向:',item['chaoxiang'],u'房龄:',item['age'],\
        #         u'小区:',item['xiaoqu'],u'户型 :', item['huxing'],u'面积:',item['mianji'],\
        #         u'总价 :',item['price'],u'单价:',item['price_pre'],u'看房人数:',item['col_look'],\
        #         u'交通 :',item['subway'],u'税费:',item['taxfree'],u'钥匙:',item['haskey']


        #print '---------------------------------------------------------------------'

        return items
