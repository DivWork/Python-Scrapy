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
        self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/navi-mumbai/gynecologist/true_/doc_/%d?lat=19.042007&lng=73.026489" % k for k in xrange(5)]),
        self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/navi-mumbai/gynecologist/true_/doc_/%d?lat=19.042007&lng=73.026489" % k for k in xrange(5)]),
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/navi-mumbai/general-physician/true_/doc_/%d?lat=12.325780&lng=76.629440" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/navi-mumbai/pediatrician/true_/doc_/%d?lat=19.042007&lng=73.026489" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/navi-mumbai/colorectal-specialist/true_/doc_/%d?lat=19.042007&lng=73.026489" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/navi-mumbai/cardiologist/true_/doc_/%d?lat=19.042007&lng=73.026489" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/navi-mumbai/diabetologist/true_/doc_/%d?lat=19.042007&lng=73.026489" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/navi-mumbai/dentist/true_/doc_/%d?lat=19.042007&lng=73.026489" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/navi-mumbai/ent-specialist/true_/doc_/%d?lat=19.042007&lng=73.026489" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/navi-mumbai/neurologist/true_/doc_/%d?lat=19.042007&lng=73.026489" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/navi-mumbai/urologist/true_/doc_/%d?lat=19.042007&lng=73.026489" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/navi-mumbai/psychiatrist/true_/doc_/%d?lat=19.042007&lng=73.026489" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/navi-mumbai/immunologist/true_/doc_/%d?lat=19.042007&lng=73.026489" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/navi-mumbai/pulmonologist/true_/doc_/%d?lat=19.042007&lng=73.026489" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/navi-mumbai/yoga-specialist/true_/doc_/%d?lat=19.042007&lng=73.026489" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/navi-mumbai/psychotherapist/true_/doc_/%d?lat=19.042007&lng=73.026489" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/navi-mumbai/audiologist/true_/doc_/%d?lat=19.042007&lng=73.026489" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/navi-mumbai/physiotherapist/true_/doc_/%d?lat=19.042007&lng=73.026489" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/navi-mumbai/endocrinologist/true_/doc_/%d?lat=19.042007&lng=73.026489" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/navi-mumbai/homoeopath/true_/doc_/%d?lat=19.042007&lng=73.026489" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/navi-mumbai/neurosurgeon/true_/doc_/%d?lat=19.042007&lng=73.026489" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/navi-mumbai/ophthalmologist/true_/doc_/%d?lat=19.042007&lng=73.026489" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/navi-mumbai/thoracic-surgeon/true_/doc_/%d?lat=19.042007&lng=73.026489" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/navi-mumbai/nephrologist/true_/doc_/%d?lat=19.042007&lng=73.026489" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/navi-mumbai/oncologist/true_/doc_/%d?lat=19.042007&lng=73.026489" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/navi-mumbai/cosmetic-surgeon/true_/doc_/%d?lat=19.042007&lng=73.026489" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/navi-mumbai/dermatologist/true_/doc_/%d?lat=19.042007&lng=73.026489" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/navi-mumbai/vascular-surgeon/true_/doc_/%d?lat=19.042007&lng=73.026489" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/navi-mumbai/orthopedic-surgeon/true_/doc_/%d?lat=19.042007&lng=73.026489" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/navi-mumbai/andrologist/true_/doc_/%d?lat=19.042007&lng=73.026489" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/navi-mumbai/ivf-specialist/true_/doc_/%d?lat=19.042007&lng=73.026489" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/navi-mumbai/general-medicine/true_/doc_/%d?lat=19.042007&lng=73.026489" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/navi-mumbai/ayurveda-specialist/true_/doc_/%d?lat=19.042007&lng=73.026489" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/navi-mumbai/gastroenterologist/true_/doc_/%d?lat=19.042007&lng=73.026489" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/navi-mumbai/neurophysiologist/true_/doc_/%d?lat=19.042007&lng=73.026489" % k for k in xrange(5)])
	#self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/navi-mumbai/oncologist/true_/doc_/%d?lat=19.042007&lng=73.026489" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/navi-mumbai/bariatric-specialist/true_/doc_/%d?lat=19.042007&lng=73.026489" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/navi-mumbai/acupuncturist/true_/doc_/%d?lat=19.042007&lng=73.026489" % k for k in xrange(5)])

        super(TravelSpider, self).__init__(name, **kwargs)
	
    
    name = "spider_navi-mumbai"
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
