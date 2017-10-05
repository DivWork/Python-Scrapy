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
        self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/gynecologist/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)]),
        self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/gynecologist/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)]),
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/general-physician/true_/doc_/%d?lat=12.325780&lng=76.629440" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/pediatrician/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/colorectal-specialist/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/cardiologist/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/diabetologist/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/dentist/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/ent-specialist/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/neurologist/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/urologist/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/psychiatrist/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/immunologist/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/pulmonologist/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/yoga-specialist/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/psychotherapist/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/audiologist/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/physiotherapist/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/endocrinologist/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/homoeopath/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/neurosurgeon/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/ophthalmologist/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/thoracic-surgeon/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/nephrologist/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/oncologist/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/cosmetic-surgeon/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/dermatologist/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/vascular-surgeon/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/orthopedic-surgeon/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/andrologist/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/ivf-specialist/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/general-medicine/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/ayurveda-specialist/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/gastroenterologist/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/neurophysiologist/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	#self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/oncologist/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/bariatric-specialist/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/acupuncturist/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])

        super(TravelSpider, self).__init__(name, **kwargs)
	
    
    name = "spider_surat_ph"
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
