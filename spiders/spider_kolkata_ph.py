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
        self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/gynecologist/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)]),
        self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/gynecologist/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)]),
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/general-physician/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/pediatrician/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/colorectal-specialist/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/cardiologist/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/diabetologist/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/dentist/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/ent-specialist/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/neurologist/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/urologist/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/psychiatrist/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/immunologist/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/pulmonologist/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/yoga-specialist/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/psychotherapist/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/audiologist/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/physiotherapist/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/endocrinologist/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/homoeopath/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/neurosurgeon/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/ophthalmologist/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/thoracic-surgeon/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/nephrologist/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/oncologist/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/cosmetic-surgeon/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/dermatologist/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/vascular-surgeon/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/orthopedic-surgeon/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/andrologist/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/ivf-specialist/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/general-medicine/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/ayurveda-specialist/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/gastroenterologist/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/neurophysiologist/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	#self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/oncologist/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/bariatric-specialist/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/acupuncturist/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])

        super(TravelSpider, self).__init__(name, **kwargs)
	
    
    name = "spider_vadodara_ph"
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
