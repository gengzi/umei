#!/usr/bin/env Python
# coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from umei.items import UmeiItem,UmeiImage


class UmeispiderSpider(CrawlSpider):
    #爬虫名称
    name = 'umeiSpider'
    #允许的域
    allowed_domains = ['umei.cc']
    #开始爬取的url地址
    start_urls = ['http://www.umei.cc/meinvtupian/xingganmeinv/']

    #【1】匹配每一页的信息
    z_page_le  = LinkExtractor(allow=r'/\d{1,3}\.htm')
    #【2】匹配每一个图组的信息
    image_le = LinkExtractor(allow=('/\d{6}.htm'))
    #【3】匹配图组的每一页信息
    img_page_le = LinkExtractor(allow=('/\d+_\d+\.htm'))

    #爬取的规则
    rules = (
        Rule(z_page_le, follow=True),
        Rule(image_le, callback='parse_item', follow=True),
        Rule(img_page_le, callback='parse_item_image', follow=True),
    )

    #还有一种思路，将 图组列表页面的 url 改成 图组分页的 url。 这样只需要写一个解析方法
    #将http://www.umei.cc/meinvtupian/xingganmeinv/125335.htm   http://www.umei.cc/meinvtupian/xingganmeinv/125335_1.htm

    def parse_item(self, response):
        """
        解析分页数据
        :param response:
        :return:
        """
        print response.url
        item = UmeiItem()
        #extract() 是转换为 unciode的编码格式
        #1,图组名称
        item['imageName'] = response.xpath('//div[@class="ArticleTitle"]/strong/text()').extract()[0]
        #2,图组的说明
        item['imageContent'] = response.xpath('//p[@class="ArticleDesc"]/text()').extract()[0]
        #3,图组的标签，是一个列表，需要组拼一下
        item['imageTags'] = response.xpath('//dl[@class="articleTag l"]/dd/a/text()').extract()
        item['imageTags'] = ",".join(item['imageName'])
        #4,图组的编号
        imageUrl = response.url
        item['iamgeId'] = imageUrl.split("/")[-1].split(".")[0]
        #5,图组的url
        item['iamgeUrl'] = imageUrl

        #抓取第一页的imageurl
        z_image_url = "http://www.umei.cc/meinvtupian/xingganmeinv/"+imageUrl.split("/")[-1].split(".")[0]+"_1.htm"

        yield scrapy.Request(url=z_image_url,callback=self.parse_item_image)

        yield item


    def parse_item_image(self,response):
        """
        解析图片的url
        :param response:
        :return:
        """
        print response.url
        zitem = UmeiImage()
        zitem['zimageurl'] = response.xpath('//div[@class="ImageBody"]//img/@src').extract()[0]
        imageUrl = response.url
        zitem['zimageId'] = imageUrl.split("/")[-1].split(".")[0].split("_")[0]

        yield zitem