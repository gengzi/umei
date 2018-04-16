# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class UmeiItem(scrapy.Item):
    # define the fields for your item here like:
    #图组的名称
    imageName = scrapy.Field()
    #图组的缩略图
    #imageThumbnail = scrapy.Field()
    #图组描述
    imageContent = scrapy.Field()
    #图组的标签
    imageTags = scrapy.Field()
    #图组的编号
    iamgeId = scrapy.Field()
    #图组的网址
    iamgeUrl = scrapy.Field()
    #图组的所有图片信息
    #imageList = scrapy.Field()


class UmeiImage(scrapy.Item):
    #图组中的一张图片的路径
    zimageurl = scrapy.Field()
    #图组的编号
    zimageId = scrapy.Field()




