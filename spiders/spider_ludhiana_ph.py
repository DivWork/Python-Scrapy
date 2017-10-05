import scrapy
from scrapy.item import Item, Field
from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider

import re
import js2xml


#from newproject.items1 import NewprojectItem
from scrapy.http import XmlResponse 
from lxml import etree
from pprint import pprint
class TravelItem(Item):
    name = Field()
    phonenumber = Field()
    #speciality = Field()

class TravelSpider(BaseSpider):
    custom_settings = {
    	'ROBOTSTXT_OBEY' : False,
   	 }
    def __init__(self, name=None, **kwargs):
        self.start_urls = []
        self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/gynecologist/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)]),
        self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/gynecologist/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)]),
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/general-physician/true_/doc_/%d?lat=12.325780&lng=76.629440" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/pediatrician/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/colorectal-specialist/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/cardiologist/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/diabetologist/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/dentist/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/ent-specialist/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/neurologist/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/urologist/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/psychiatrist/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/immunologist/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/pulmonologist/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/yoga-specialist/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/psychotherapist/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/audiologist/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/physiotherapist/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/endocrinologist/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/homoeopath/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/neurosurgeon/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/ophthalmologist/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/thoracic-surgeon/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/nephrologist/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/oncologist/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/cosmetic-surgeon/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/dermatologist/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/vascular-surgeon/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/orthopedic-surgeon/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/andrologist/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/ivf-specialist/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/general-medicine/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/ayurveda-specialist/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/gastroenterologist/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/neurophysiologist/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	#self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/oncologist/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/bariatric-specialist/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/acupuncturist/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])

        super(TravelSpider, self).__init__(name, **kwargs)
	
    
    name = "spider_ludhiana_ph"
    allowed_domains = ["medinfi.com"]

    def parse(self, response):
		#hxs = HtmlXPathSelector(response)
		items = []
		links = response.xpath('//div[@class = "row"]/a/@href').extract()
	
	#item = NewprojectItem()
	
	
		for link in links :
			print "http://www.medinfi.com"+link
			yield scrapy.Request("http://www.medinfi.com"+link , callback =self.parsefunction)
	
    def parsefunction(self,response):
	item = TravelItem()
	#print "sometext"
	
	values = response.xpath('//script[2]/text()').extract()
	names = response.xpath("//div/h1[@class='docName']//text()").extract()
	
	
	counter = 0
	
	
	for value in values:
		tree = js2xml.parse(value)
		print(js2xml.pretty_print(tree))
		value = js2xml.jsonlike.make_dict(tree.xpath('//var[@name="phNo"]/string')[0])
		
		pprint(value)
		item['name'] = names[counter]
		item['phonenumber'] = value
		counter = counter+1
		yield item
