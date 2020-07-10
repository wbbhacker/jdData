# -*- coding: utf-8 -*-
import scrapy
from jdData.items import JddataItem

class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['jd.com']
    start_urls = ['https://mall.jd.com/view_search-669859-12005175-99-1-24-1.html']

    def parse(self, response):
        # item = JdItem()
        # item['title'] = response.selector.css('title')
        jDesc = response.xpath('//div[@class="jDesc"]/a/text()')[0]
        item = JddataItem()
        print(jDesc)
        item['title'] = jDesc.extract()
        
        yield item 
