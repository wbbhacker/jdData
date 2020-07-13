# -*- coding: utf-8 -*-
import scrapy
from jdData.items import JddataItem

class JdSpider(scrapy.Spider):

    name = 'jd'
    allowed_domains = ['jd.com']
    start_urls = [
        'https://mall.jd.com/index-753450.html'  #联想天佑授权专卖店
    ]

    level1Link = []  #一级 分类
    level2link = {}  #型号
  
    def parse(self, response):

        leve1Array = response.xpath('//div[@class="sub-menu-wrap"]//a[@class="leaf-link"]')
        self.getLevel_1(leve1Array)



        arr = [self.level1Link[0]]
        # arr = self.level1Link
        for item in arr:
            url = item['link']
            print('********A')
            print(url)
            yield scrapy.Request(url=url, callback=self.getLevel_2, cb_kwargs=item)

        # item = JddataItem()
        # item['title'] = jDesc.extract()
        # yield item 

    def getLevel_1(self,arrLink):
        for item in arrLink:
            self.level1Link.append({
                'name':item.xpath('text()')[0].get(),
                'link':'https://'+item.xpath('@href')[0].get()[2:]
            })

    def getLevel_2(self, response,name,link):
        print('************8')
        print(name)
        leve2Array = response.xpath('//div[@class="jPic"]/a')
        for item in leve2Array:
            url = 'https://'+item.xpath('@href')[0].get()[2:]
            print(url)


        
