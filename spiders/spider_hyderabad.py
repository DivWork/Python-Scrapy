from scrapy.item import Item, Field
from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider



class TravelItem(Item):
    name = Field()
    address = Field()
    speciality = Field()

class TravelSpider(BaseSpider):
    custom_settings = {
    	'ROBOTSTXT_OBEY' : False,
   	 }
    def __init__(self, name=None, **kwargs):
        self.start_urls = []
        self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/hyderabad/gynecologist/true_/doc_/%d?lat=17.437462&lng=78.448288" % k for k in xrange(5)]),
        self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/hyderabad/gynecologist/true_/doc_/%d?lat=17.437462&lng=78.448288" % k for k in xrange(5)]),
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/hyderabad/general-physician/true_/doc_/%d?lat=12.325780&lng=76.629440" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/hyderabad/pediatrician/true_/doc_/%d?lat=17.437462&lng=78.448288" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/hyderabad/colorectal-specialist/true_/doc_/%d?lat=17.437462&lng=78.448288" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/hyderabad/cardiologist/true_/doc_/%d?lat=17.437462&lng=78.448288" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/hyderabad/diabetologist/true_/doc_/%d?lat=17.437462&lng=78.448288" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/hyderabad/dentist/true_/doc_/%d?lat=17.437462&lng=78.448288" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/hyderabad/ent-specialist/true_/doc_/%d?lat=17.437462&lng=78.448288" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/hyderabad/neurologist/true_/doc_/%d?lat=17.437462&lng=78.448288" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/hyderabad/urologist/true_/doc_/%d?lat=17.437462&lng=78.448288" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/hyderabad/psychiatrist/true_/doc_/%d?lat=17.437462&lng=78.448288" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/hyderabad/immunologist/true_/doc_/%d?lat=17.437462&lng=78.448288" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/hyderabad/pulmonologist/true_/doc_/%d?lat=17.437462&lng=78.448288" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/hyderabad/yoga-specialist/true_/doc_/%d?lat=17.437462&lng=78.448288" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/hyderabad/psychotherapist/true_/doc_/%d?lat=17.437462&lng=78.448288" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/hyderabad/audiologist/true_/doc_/%d?lat=17.437462&lng=78.448288" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/hyderabad/physiotherapist/true_/doc_/%d?lat=17.437462&lng=78.448288" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/hyderabad/endocrinologist/true_/doc_/%d?lat=17.437462&lng=78.448288" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/hyderabad/homoeopath/true_/doc_/%d?lat=17.437462&lng=78.448288" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/hyderabad/neurosurgeon/true_/doc_/%d?lat=17.437462&lng=78.448288" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/hyderabad/ophthalmologist/true_/doc_/%d?lat=17.437462&lng=78.448288" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/hyderabad/thoracic-surgeon/true_/doc_/%d?lat=17.437462&lng=78.448288" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/hyderabad/nephrologist/true_/doc_/%d?lat=17.437462&lng=78.448288" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/hyderabad/oncologist/true_/doc_/%d?lat=17.437462&lng=78.448288" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/hyderabad/cosmetic-surgeon/true_/doc_/%d?lat=17.437462&lng=78.448288" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/hyderabad/dermatologist/true_/doc_/%d?lat=17.437462&lng=78.448288" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/hyderabad/vascular-surgeon/true_/doc_/%d?lat=17.437462&lng=78.448288" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/hyderabad/orthopedic-surgeon/true_/doc_/%d?lat=17.437462&lng=78.448288" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/hyderabad/andrologist/true_/doc_/%d?lat=17.437462&lng=78.448288" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/hyderabad/ivf-specialist/true_/doc_/%d?lat=17.437462&lng=78.448288" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/hyderabad/general-medicine/true_/doc_/%d?lat=17.437462&lng=78.448288" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/hyderabad/ayurveda-specialist/true_/doc_/%d?lat=17.437462&lng=78.448288" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/hyderabad/gastroenterologist/true_/doc_/%d?lat=17.437462&lng=78.448288" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/hyderabad/neurophysiologist/true_/doc_/%d?lat=17.437462&lng=78.448288" % k for k in xrange(5)])
	#self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/hyderabad/oncologist/true_/doc_/%d?lat=17.437462&lng=78.448288" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/hyderabad/bariatric-specialist/true_/doc_/%d?lat=17.437462&lng=78.448288" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/hyderabad/acupuncturist/true_/doc_/%d?lat=17.437462&lng=78.448288" % k for k in xrange(5)])

        super(TravelSpider, self).__init__(name, **kwargs)
	
    
    name = "spider_hyderabad"
    allowed_domains = ["medinfi.com"]

    def parse(self, response):
		#hxs = HtmlXPathSelector(response)
		items = []
		item = TravelItem()
		address = response.xpath("//div[@class='docInfoDiv']/span//text()").extract()
		name = response.xpath('//div[@class="docInfoDiv"]/div/h2//text()').extract()
		speciality = response.xpath('//div[@class="docInfoDiv"]/div/div//span[2]/text()').extract()
		#print selnew
		#item = NewprojectItem()
		count = 0
	
		for add in address :
			#print add
			item['address'] = add
		
		#for nam in name :
		
			item['name'] = name[count]
		#for special in speciality :
			#print special
			special = speciality[count].strip()
			special = special.replace("-","")
			item['speciality'] = special
		
			count = count+1
			yield item
