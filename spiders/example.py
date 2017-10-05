from scrapy.item import Item, Field
from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider

import scrapy

class TravelItem(Item):
    pretest_info = Field()
    test_name = Field()
    #address = Field()
    #speciality = Field()

class MySpider(BaseSpider):
    custom_settings = {
    	'ROBOTSTXT_OBEY' : False,
   	 }

    name = 'scrapy_new_spider'
    allowed_domains = ['lalpathlabs.com']
    start_urls = [
	'https://www.lalpathlabs.com/test-by-alphabets/%',
    ]

    def parse(self, response):
	items = []
	item = TravelItem()
	counter = 0
        names = response.xpath("//li/div[@class = 'sectorBox']/div[@class = 'cen']/div[@class='secBox']/a//text()").extract()
	tests = response.xpath("//li/div[@class = 'sectorBox']/div[@class = 'cen']/div[@class='nameBox2']/div[@class='left2'][2]//p//text()").extract()
	for name in names:
            item["test_name"] = name
	    item["pretest_info"] = tests[counter]
	    counter = counter+1
	    yield item

        
