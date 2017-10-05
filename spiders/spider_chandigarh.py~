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
        self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chandigarh/gynecologist/true_/doc_/%d?lat=30.726053&lng=76.759628" % k for k in xrange(5)]),
        self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chandigarh/gynecologist/true_/doc_/%d?lat=30.726053&lng=76.759628" % k for k in xrange(5)]),
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chandigarh/general-physician/true_/doc_/%d?lat=12.325780&lng=76.629440" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chandigarh/pediatrician/true_/doc_/%d?lat=30.726053&lng=76.759628" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chandigarh/colorectal-specialist/true_/doc_/%d?lat=30.726053&lng=76.759628" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chandigarh/cardiologist/true_/doc_/%d?lat=30.726053&lng=76.759628" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chandigarh/diabetologist/true_/doc_/%d?lat=30.726053&lng=76.759628" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chandigarh/dentist/true_/doc_/%d?lat=30.726053&lng=76.759628" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chandigarh/ent-specialist/true_/doc_/%d?lat=30.726053&lng=76.759628" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chandigarh/neurologist/true_/doc_/%d?lat=30.726053&lng=76.759628" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chandigarh/urologist/true_/doc_/%d?lat=30.726053&lng=76.759628" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chandigarh/psychiatrist/true_/doc_/%d?lat=30.726053&lng=76.759628" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chandigarh/immunologist/true_/doc_/%d?lat=30.726053&lng=76.759628" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chandigarh/pulmonologist/true_/doc_/%d?lat=30.726053&lng=76.759628" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chandigarh/yoga-specialist/true_/doc_/%d?lat=30.726053&lng=76.759628" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chandigarh/psychotherapist/true_/doc_/%d?lat=30.726053&lng=76.759628" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chandigarh/audiologist/true_/doc_/%d?lat=30.726053&lng=76.759628" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chandigarh/physiotherapist/true_/doc_/%d?lat=30.726053&lng=76.759628" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chandigarh/endocrinologist/true_/doc_/%d?lat=30.726053&lng=76.759628" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chandigarh/homoeopath/true_/doc_/%d?lat=30.726053&lng=76.759628" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chandigarh/neurosurgeon/true_/doc_/%d?lat=30.726053&lng=76.759628" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chandigarh/ophthalmologist/true_/doc_/%d?lat=30.726053&lng=76.759628" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chandigarh/thoracic-surgeon/true_/doc_/%d?lat=30.726053&lng=76.759628" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chandigarh/nephrologist/true_/doc_/%d?lat=30.726053&lng=76.759628" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chandigarh/oncologist/true_/doc_/%d?lat=30.726053&lng=76.759628" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chandigarh/cosmetic-surgeon/true_/doc_/%d?lat=30.726053&lng=76.759628" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chandigarh/dermatologist/true_/doc_/%d?lat=30.726053&lng=76.759628" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chandigarh/vascular-surgeon/true_/doc_/%d?lat=30.726053&lng=76.759628" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chandigarh/orthopedic-surgeon/true_/doc_/%d?lat=30.726053&lng=76.759628" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chandigarh/andrologist/true_/doc_/%d?lat=30.726053&lng=76.759628" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chandigarh/ivf-specialist/true_/doc_/%d?lat=30.726053&lng=76.759628" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chandigarh/general-medicine/true_/doc_/%d?lat=30.726053&lng=76.759628" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chandigarh/ayurveda-specialist/true_/doc_/%d?lat=30.726053&lng=76.759628" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chandigarh/gastroenterologist/true_/doc_/%d?lat=30.726053&lng=76.759628" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chandigarh/neurophysiologist/true_/doc_/%d?lat=30.726053&lng=76.759628" % k for k in xrange(5)])
	#self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chandigarh/oncologist/true_/doc_/%d?lat=30.726053&lng=76.759628" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chandigarh/bariatric-specialist/true_/doc_/%d?lat=30.726053&lng=76.759628" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chandigarh/acupuncturist/true_/doc_/%d?lat=30.726053&lng=76.759628" % k for k in xrange(5)])

        super(TravelSpider, self).__init__(name, **kwargs)
	
    
    name = "spider_chandigarh"
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
