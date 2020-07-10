# -*- coding: utf-8 -*-
import scrapy
from jdData.items import JddataItem
from selenium import webdriver
from selenium.webdriver.chrome.options import Options    # 使用无头浏览器
br = webdriver.Chrome()

br.get('http://www.baidu.com')
print(br.page_source)

class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['jd.com']
    start_urls = ['https://www.jd.com']

    def parse(self, response):
        # item = JdItem()
        # item['title'] = response.selector.css('title')
        item = JddataItem()
        item['title'] = response.xpath('/html/head/title/text()').extract()
        
        yield item 
