# -*- coding: utf-8 -*-
############################################################################
# 程序：上海链家网爬虫
# 功能：抓取上海链家二手房在售大约5万记录
# 创建时间：2016/11/26
# 更新时间：2016/11/26
# 使用库：Scrapy、BeautifulSoup4、MySQLdb
# 作者：yuzhucu
#############################################################################
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb
import re, json, sys, time
sucess_count = 0
error_count = 0
class FangspiderPipeline(object):
    def process_item(self, item, spider):
        global sucess_count,error_count
        mysql_con = spider.settings.get('MYSQL_CONNECT')
        con = MySQLdb.connect(**mysql_con)
        cur = con.cursor()
        sql = ("insert into lianjia_fang_list(fang_key,fang_desc,fang_url,price,price_pre,xiaoqu,huxing,mianji,quyu,bankuai,louceng,chaoxiang,age,subway,taxfree,haskey,col_look) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        item_list = (item['fang_key'],item['fang_desc'],item['fang_url'],item['price'],item['price_pre'],item['xiaoqu'], item['huxing'], item['mianji'],item['quyu'],item['bankuai'],item['louceng'],item['chaoxiang'],item['age'],item['subway'],item['taxfree'],item['haskey'],item['col_look'])
        try:
            cur.execute(sql,item_list)
        except Exception,e:
            error_count += 1
            print getCurrentTime(),"Insert Error Count:",error_count,e,item['fang_key'],item['quyu'] ,item['xiaoqu'] ,item['price'], item['huxing'],item['mianji']
            con.rollback()
        else:
            con.commit()
            sucess_count += 1
            print getCurrentTime(),'Success Count:',sucess_count,u':',  item['fang_key'],item['quyu'] ,item['xiaoqu'] ,item['price'], item['huxing'],item['mianji']
        cur.close()
        con.close()
        return item

def getCurrentTime():
    return time.strftime('[%Y-%m-%d %H:%M:%S]',time.localtime(time.time()))