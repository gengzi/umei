#!/usr/bin/env Python
# coding=utf-8
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from umei.items import UmeiItem,UmeiImage
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class UmeiPipeline(object):

    def __init__(self):
        pass


    def process_item(self, item, spider):
        if isinstance(item,UmeiItem):
            print item
            pass
        elif isinstance(item,UmeiImage):
            print item
            pass
        else:
            print "匹配不到正确的item"
            return
