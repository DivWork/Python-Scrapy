import scrapy
import re
import js2xml


from newproject.items1 import NewprojectItem
from scrapy.http import XmlResponse 
from lxml import etree
from pprint import pprint

class NewSpider(scrapy.Spider):
    name = "spider2"
    allowed_domains = ["medinfi.com"]
    start_urls = [
        "http://www.medinfi.com/medinfi/doctor-search/bengaluru/doc_/%d?lat=12.933221&lng=77.632195" % i for i in xrange(5)
	#"http://www.medinfi.com/medinfi/doctor-search/new-delhi/doc_/%d?lat=28.703215&lng=77.124519" % k for k in xrange(5)
	#"http://www.medinfi.com/medinfi/doctor-search/mumbai/doc_/1?lat=19.113646&lng=72.869736" % k for k in xrange(5)
	#"http://www.medinfi.com/medinfi/doctor-search/hyderabad/doc_/1?lat=17.437462&lng=78.448288" % k for k in xrange(5)
	#"http://www.medinfi.com/medinfi/doctor-search/kolkata/doc_/1?lat=22.498140&lng=88.310837" % k for k in xrange(5)
	#"http://www.medinfi.com/medinfi/doctor-search/pune/doc_/1?lat=18.557699&lng=73.798584" % k for k in xrange(5)
	#"http://www.medinfi.com/medinfi/doctor-search/ahmedabad/doc_/1?lat=23.019281&lng=72.518974" % k for k in xrange(5)
	#"http://www.medinfi.com/medinfi/doctor-search/noida/doc_/1?lat=18.557699&lng=73.798584" % k for k in xrange(5)
	#"http://www.medinfi.com/medinfi/doctor-search/jaipur/doc_/1?lat=26.910528&lng=75.802200" % k for k in xrange(5)
	#"http://www.medinfi.com/medinfi/doctor-search/ghaziabad/doc_/1?lat=23.019281&lng=72.518974" % k for k in xrange(5)
	#"http://www.medinfi.com/medinfi/doctor-search/navi-mumbai/doc_/1?lat=19.042007&lng=73.026489" % k for k in xrange(5)
	#"http://www.medinfi.com/medinfi/doctor-search/gurgaon/doc_/1?lat=28.578321&lng=77.317818" % k for k in xrange(5)
	#"http://www.medinfi.com/medinfi/doctor-search/lucknow/doc_/1?lat=26.879892&lng=80.992630" % k for k in xrange(5)
	#"http://www.medinfi.com/medinfi/doctor-search/indore/doc_/1?lat=22.725136&lng=75.892609" % k for k in xrange(5)
	#"http://www.medinfi.com/medinfi/doctor-search/bhopal/doc_/1?lat=23.211283&lng=77.435089" % k for k in xrange(5)
	#"http://www.medinfi.com/medinfi/doctor-search/chandigarh/doc_/1?lat=30.726053&lng=76.759628" % k for k in xrange(5)
	#"http://www.medinfi.com/medinfi/doctor-search/nagpur/doc_/1?lat=21.130047&lng=79.079376" % k for k in xrange(5)
	#"http://www.medinfi.com/medinfi/doctor-search/thiruvananthapuram/doc_/1?lat=8.511871&lng=76.925537" % k for k in xrange(5)
	#"http://www.medinfi.com/medinfi/doctor-search/coimbatore/doc_/1?lat=11.021102&lng=76.966820" % k for k in xrange(5)
	#"http://www.medinfi.com/medinfi/doctor-search/surat/doc_/1?lat=21.228922&lng=72.830322" % k for k in xrange(5)
	#"http://www.medinfi.com/medinfi/doctor-search/chennai/doc_/1?lat=12.975971&lng=80.221207" % k for k in xrange(5)
	#"http://www.medinfi.com/medinfi/doctor-search/ludhiana/doc_/1?lat=30.915318&lng=75.834633" % k for k in xrange(5)
	#"http://www.medinfi.com/medinfi/doctor-search/mysuru/doc_/1?lat=12.325780&lng=76.629440" % k for k in xrange(5)
	#"http://www.medinfi.com/medinfi/doctor-search/vadodara/doc_/1?lat=22.295252&lng=73.170822" % k for k in xrange(5)
	
    ]
    custom_settings = {
    'ROBOTSTXT_OBEY' : False,
    }

    def parse(self, response):
	
	links = response.xpath('//div[@class = "row"]/a/@href').extract()
	
	item = NewprojectItem()
	
	
	for link in links :
		print "http://www.medinfi.com"+link
		yield scrapy.Request("http://www.medinfi.com"+link , callback =self.parsefunction)
	
    def parsefunction(self,response):
	item = NewprojectItem()
	
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
		
		

	
		
		
		
	
	
		
