# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import  LinkExtractor
from umei.items import UmeiItem


class umeiSpider_test(CrawlSpider):
    #爬虫名称
    name = "umeispider"
    #允许爬取的域
    allow_domains = ['umei.cc']




