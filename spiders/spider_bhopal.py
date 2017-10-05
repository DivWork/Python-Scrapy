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
        self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bhopal/gynecologist/true_/doc_/%d?lat=23.211283&lng=77.435089" % k for k in xrange(5)]),
        self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bhopal/gynecologist/true_/doc_/%d?lat=23.211283&lng=77.435089" % k for k in xrange(5)]),
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bhopal/general-physician/true_/doc_/%d?lat=12.325780&lng=76.629440" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bhopal/pediatrician/true_/doc_/%d?lat=23.211283&lng=77.435089" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bhopal/colorectal-specialist/true_/doc_/%d?lat=23.211283&lng=77.435089" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bhopal/cardiologist/true_/doc_/%d?lat=23.211283&lng=77.435089" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bhopal/diabetologist/true_/doc_/%d?lat=23.211283&lng=77.435089" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bhopal/dentist/true_/doc_/%d?lat=23.211283&lng=77.435089" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bhopal/ent-specialist/true_/doc_/%d?lat=23.211283&lng=77.435089" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bhopal/neurologist/true_/doc_/%d?lat=23.211283&lng=77.435089" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bhopal/urologist/true_/doc_/%d?lat=23.211283&lng=77.435089" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bhopal/psychiatrist/true_/doc_/%d?lat=23.211283&lng=77.435089" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bhopal/immunologist/true_/doc_/%d?lat=23.211283&lng=77.435089" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bhopal/pulmonologist/true_/doc_/%d?lat=23.211283&lng=77.435089" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bhopal/yoga-specialist/true_/doc_/%d?lat=23.211283&lng=77.435089" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bhopal/psychotherapist/true_/doc_/%d?lat=23.211283&lng=77.435089" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bhopal/audiologist/true_/doc_/%d?lat=23.211283&lng=77.435089" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bhopal/physiotherapist/true_/doc_/%d?lat=23.211283&lng=77.435089" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bhopal/endocrinologist/true_/doc_/%d?lat=23.211283&lng=77.435089" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bhopal/homoeopath/true_/doc_/%d?lat=23.211283&lng=77.435089" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bhopal/neurosurgeon/true_/doc_/%d?lat=23.211283&lng=77.435089" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bhopal/ophthalmologist/true_/doc_/%d?lat=23.211283&lng=77.435089" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bhopal/thoracic-surgeon/true_/doc_/%d?lat=23.211283&lng=77.435089" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bhopal/nephrologist/true_/doc_/%d?lat=23.211283&lng=77.435089" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bhopal/oncologist/true_/doc_/%d?lat=23.211283&lng=77.435089" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bhopal/cosmetic-surgeon/true_/doc_/%d?lat=23.211283&lng=77.435089" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bhopal/dermatologist/true_/doc_/%d?lat=23.211283&lng=77.435089" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bhopal/vascular-surgeon/true_/doc_/%d?lat=23.211283&lng=77.435089" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bhopal/orthopedic-surgeon/true_/doc_/%d?lat=23.211283&lng=77.435089" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bhopal/andrologist/true_/doc_/%d?lat=23.211283&lng=77.435089" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bhopal/ivf-specialist/true_/doc_/%d?lat=23.211283&lng=77.435089" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bhopal/general-medicine/true_/doc_/%d?lat=23.211283&lng=77.435089" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bhopal/ayurveda-specialist/true_/doc_/%d?lat=23.211283&lng=77.435089" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bhopal/gastroenterologist/true_/doc_/%d?lat=23.211283&lng=77.435089" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bhopal/neurophysiologist/true_/doc_/%d?lat=23.211283&lng=77.435089" % k for k in xrange(5)])
	#self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bhopal/oncologist/true_/doc_/%d?lat=23.211283&lng=77.435089" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bhopal/bariatric-specialist/true_/doc_/%d?lat=23.211283&lng=77.435089" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bhopal/acupuncturist/true_/doc_/%d?lat=23.211283&lng=77.435089" % k for k in xrange(5)])

        super(TravelSpider, self).__init__(name, **kwargs)
	
    
    name = "spider_bhopal"
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
