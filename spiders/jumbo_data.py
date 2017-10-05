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
        self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/new-delhi/gynecologist/true_/doc_/%d?lat=28.703215&lng=77.124519" % k for k in xrange(5)]),
        self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/new-delhi/general-physician/true_/doc_/%d?lat=28.703215&lng=77.124519" % k for k in xrange(5)]),
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/new-delhi/general-physician/true_/doc_/%d?lat=28.703215&lng=77.124519" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/new-delhi/pediatrician/true_/doc_/%d?lat=28.703215&lng=77.124519" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/new-delhi/colorectal-specialist/true_/doc_/%d?lat=28.703215&lng=77.124519" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/new-delhi/cardiologist/true_/doc_/%d?lat=28.703215&lng=77.124519" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/new-delhi/diabetologist/true_/doc_/%d?lat=28.703215&lng=77.124519" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/new-delhi/dentist/true_/doc_/%d?lat=28.703215&lng=77.124519" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/new-delhi/ent-specialist/true_/doc_/%d?lat=28.703215&lng=77.124519" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/new-delhi/neurologist/true_/doc_/%d?lat=28.703215&lng=77.124519" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/new-delhi/urologist/true_/doc_/%d?lat=28.703215&lng=77.124519" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/new-delhi/psychiatrist/true_/doc_/%d?lat=28.703215&lng=77.124519" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/new-delhi/immunologist/true_/doc_/%d?lat=28.703215&lng=77.124519" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/new-delhi/pulmonologist/true_/doc_/%d?lat=28.703215&lng=77.124519" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/new-delhi/yoga-specialist/true_/doc_/%d?lat=28.703215&lng=77.124519" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/new-delhi/psychotherapist/true_/doc_/%d?lat=28.703215&lng=77.124519" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/new-delhi/audiologist/true_/doc_/%d?lat=28.703215&lng=77.124519" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/new-delhi/physiotherapist/true_/doc_/%d?lat=28.703215&lng=77.124519" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/new-delhi/endocrinologist/true_/doc_/%d?lat=28.703215&lng=77.124519" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/new-delhi/homoeopath/true_/doc_/%d?lat=28.703215&lng=77.124519" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/new-delhi/neurosurgeon/true_/doc_/%d?lat=28.703215&lng=77.124519" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/new-delhi/ophthalmologist/true_/doc_/%d?lat=28.703215&lng=77.124519" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/new-delhi/thoracic-surgeon/true_/doc_/%d?lat=28.703215&lng=77.124519" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/new-delhi/nephrologist/true_/doc_/%d?lat=28.703215&lng=77.124519" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/new-delhi/oncologist/true_/doc_/%d?lat=28.703215&lng=77.124519" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/new-delhi/cosmetic-surgeon/true_/doc_/%d?lat=28.703215&lng=77.124519" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/new-delhi/dermatologist/true_/doc_/%d?lat=28.703215&lng=77.124519" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/new-delhi/vascular-surgeon/true_/doc_/%d?lat=28.703215&lng=77.124519" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/new-delhi/orthopedic-surgeon/true_/doc_/%d?lat=28.703215&lng=77.124519" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/new-delhi/andrologist/true_/doc_/%d?lat=28.703215&lng=77.124519" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/new-delhi/ivf-specialist/true_/doc_/%d?lat=28.703215&lng=77.124519" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/new-delhi/general-medicine/true_/doc_/%d?lat=28.703215&lng=77.124519" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/new-delhi/ayurveda-specialist/true_/doc_/%d?lat=28.703215&lng=77.124519" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/new-delhi/gastroenterologist/true_/doc_/%d?lat=28.703215&lng=77.124519" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/new-delhi/neurophysiologist/true_/doc_/%d?lat=28.703215&lng=77.124519" % k for k in xrange(5)])
	#self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/new-delhi/oncologist/true_/doc_/%d?lat=28.703215&lng=77.124519" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/new-delhi/bariatric-specialist/true_/doc_/%d?lat=28.703215&lng=77.124519" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/new-delhi/acupuncturist/true_/doc_/%d?lat=28.703215&lng=77.124519" % k for k in xrange(5)])

        super(TravelSpider, self).__init__(name, **kwargs)
	
    
    name = "spider_delhi"
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
