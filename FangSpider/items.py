# -*- coding: utf-8 -*-
############################################################################
# 程序：上海链家网爬虫
# 功能：抓取上海链家二手房在售大约5万记录
# 创建时间：2016/11/26
# 更新时间：2016/11/26
# 使用库：Scrapy、BeautifulSoup4、MySQLdb
# 作者：yuzhucu
#############################################################################
# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class FangSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    fang_key = scrapy.Field()
    fang_desc = scrapy.Field()
    fang_url = scrapy.Field()
    price = scrapy.Field()
    price_pre = scrapy.Field()
    xiaoqu = scrapy.Field()
    huxing = scrapy.Field()
    mianji = scrapy.Field()
    quyu = scrapy.Field()
    bankuai = scrapy.Field()
    louceng = scrapy.Field()
    chaoxiang = scrapy.Field()
    age = scrapy.Field()
    subway = scrapy.Field()
    taxfree = scrapy.Field()
    haskey = scrapy.Field()
    col_look = scrapy.Field()
