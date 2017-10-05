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
        self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/mumbai/gynecologist/true_/doc_/%d?lat=19.113646&lng=72.869736" % k for k in xrange(5)]),
        self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/mumbai/gynecologist/true_/doc_/%d?lat=19.113646&lng=72.869736" % k for k in xrange(5)]),
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/mumbai/general-physician/true_/doc_/%d?lat=12.325780&lng=76.629440" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/mumbai/pediatrician/true_/doc_/%d?lat=19.113646&lng=72.869736" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/mumbai/colorectal-specialist/true_/doc_/%d?lat=19.113646&lng=72.869736" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/mumbai/cardiologist/true_/doc_/%d?lat=19.113646&lng=72.869736" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/mumbai/diabetologist/true_/doc_/%d?lat=19.113646&lng=72.869736" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/mumbai/dentist/true_/doc_/%d?lat=19.113646&lng=72.869736" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/mumbai/ent-specialist/true_/doc_/%d?lat=19.113646&lng=72.869736" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/mumbai/neurologist/true_/doc_/%d?lat=19.113646&lng=72.869736" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/mumbai/urologist/true_/doc_/%d?lat=19.113646&lng=72.869736" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/mumbai/psychiatrist/true_/doc_/%d?lat=19.113646&lng=72.869736" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/mumbai/immunologist/true_/doc_/%d?lat=19.113646&lng=72.869736" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/mumbai/pulmonologist/true_/doc_/%d?lat=19.113646&lng=72.869736" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/mumbai/yoga-specialist/true_/doc_/%d?lat=19.113646&lng=72.869736" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/mumbai/psychotherapist/true_/doc_/%d?lat=19.113646&lng=72.869736" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/mumbai/audiologist/true_/doc_/%d?lat=19.113646&lng=72.869736" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/mumbai/physiotherapist/true_/doc_/%d?lat=19.113646&lng=72.869736" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/mumbai/endocrinologist/true_/doc_/%d?lat=19.113646&lng=72.869736" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/mumbai/homoeopath/true_/doc_/%d?lat=19.113646&lng=72.869736" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/mumbai/neurosurgeon/true_/doc_/%d?lat=19.113646&lng=72.869736" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/mumbai/ophthalmologist/true_/doc_/%d?lat=19.113646&lng=72.869736" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/mumbai/thoracic-surgeon/true_/doc_/%d?lat=19.113646&lng=72.869736" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/mumbai/nephrologist/true_/doc_/%d?lat=19.113646&lng=72.869736" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/mumbai/oncologist/true_/doc_/%d?lat=19.113646&lng=72.869736" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/mumbai/cosmetic-surgeon/true_/doc_/%d?lat=19.113646&lng=72.869736" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/mumbai/dermatologist/true_/doc_/%d?lat=19.113646&lng=72.869736" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/mumbai/vascular-surgeon/true_/doc_/%d?lat=19.113646&lng=72.869736" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/mumbai/orthopedic-surgeon/true_/doc_/%d?lat=19.113646&lng=72.869736" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/mumbai/andrologist/true_/doc_/%d?lat=19.113646&lng=72.869736" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/mumbai/ivf-specialist/true_/doc_/%d?lat=19.113646&lng=72.869736" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/mumbai/general-medicine/true_/doc_/%d?lat=19.113646&lng=72.869736" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/mumbai/ayurveda-specialist/true_/doc_/%d?lat=19.113646&lng=72.869736" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/mumbai/gastroenterologist/true_/doc_/%d?lat=19.113646&lng=72.869736" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/mumbai/neurophysiologist/true_/doc_/%d?lat=19.113646&lng=72.869736" % k for k in xrange(5)])
	#self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/mumbai/oncologist/true_/doc_/%d?lat=19.113646&lng=72.869736" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/mumbai/bariatric-specialist/true_/doc_/%d?lat=19.113646&lng=72.869736" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/mumbai/acupuncturist/true_/doc_/%d?lat=19.113646&lng=72.869736" % k for k in xrange(5)])

        super(TravelSpider, self).__init__(name, **kwargs)
	
    
    name = "spider_mumbai"
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
