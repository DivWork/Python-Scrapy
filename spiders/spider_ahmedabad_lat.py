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
    lat = Field()
    #phonenumber = Field()
    #speciality = Field()

class TravelSpider(BaseSpider):
    custom_settings = {
    	'ROBOTSTXT_OBEY' : False,
   	 }
    def __init__(self, name=None, **kwargs):
        self.start_urls = []
        self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/gynecologist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)]),
        self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/gynecologist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)]),
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/general-physician/true_/doc_/%d?lat=28.578321&lng=77.317818" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/pediatrician/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/colorectal-specialist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/cardiologist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/diabetologist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/dentist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/ent-specialist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/neurologist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/urologist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/psychiatrist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/immunologist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/pulmonologist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/yoga-specialist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/psychotherapist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/audiologist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/physiotherapist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/endocrinologist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/homoeopath/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/neurosurgeon/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/ophthalmologist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/thoracic-surgeon/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/nephrologist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/oncologist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/cosmetic-surgeon/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/dermatologist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/vascular-surgeon/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/orthopedic-surgeon/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/andrologist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/ivf-specialist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/general-medicine/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/ayurveda-specialist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/gastroenterologist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/neurophysiologist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	#self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/oncologist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/bariatric-specialist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/acupuncturist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])

        super(TravelSpider, self).__init__(name, **kwargs)
	
    
    name = "spider_ahmedabad_lat"
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
	#item = NewprojectItem()
	#print "sometext"
	item = TravelItem()
	
	values = response.xpath('//script[2]/text()').extract()
	names = response.xpath("//div/h1[@class='docName']//text()").extract()
	
	
	counter = 0
	
	
	for value in values:
		tree = js2xml.parse(value)
		print(js2xml.pretty_print(tree))
		value = js2xml.jsonlike.make_dict(tree.xpath('//var[@name="cachingLocationInfo"]/string')[0])
		
		#pprint(value)
		#print names[counter]
		#item['name'] = names[counter]
		item['lat'] = value
		#counter = counter+1
		yield item
