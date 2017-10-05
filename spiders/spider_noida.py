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
        self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/noida/gynecologist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)]),
        self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/noida/gynecologist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)]),
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/noida/general-physician/true_/doc_/%d?lat=12.325780&lng=76.629440" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/noida/pediatrician/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/noida/colorectal-specialist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/noida/cardiologist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/noida/diabetologist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/noida/dentist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/noida/ent-specialist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/noida/neurologist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/noida/urologist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/noida/psychiatrist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/noida/immunologist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/noida/pulmonologist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/noida/yoga-specialist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/noida/psychotherapist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/noida/audiologist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/noida/physiotherapist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/noida/endocrinologist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/noida/homoeopath/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/noida/neurosurgeon/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/noida/ophthalmologist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/noida/thoracic-surgeon/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/noida/nephrologist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/noida/oncologist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/noida/cosmetic-surgeon/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/noida/dermatologist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/noida/vascular-surgeon/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/noida/orthopedic-surgeon/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/noida/andrologist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/noida/ivf-specialist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/noida/general-medicine/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/noida/ayurveda-specialist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/noida/gastroenterologist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/noida/neurophysiologist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	#self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/noida/oncologist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/noida/bariatric-specialist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/noida/acupuncturist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])

        super(TravelSpider, self).__init__(name, **kwargs)
	
    
    name = "spider_noida"
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
