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
        self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/gynecologist/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)]),
        self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/gynecologist/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)]),
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/general-physician/true_/doc_/%d?lat=12.325780&lng=76.629440" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/pediatrician/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/colorectal-specialist/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/cardiologist/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/diabetologist/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/dentist/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/ent-specialist/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/neurologist/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/urologist/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/psychiatrist/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/immunologist/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/pulmonologist/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/yoga-specialist/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/psychotherapist/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/audiologist/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/physiotherapist/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/endocrinologist/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/homoeopath/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/neurosurgeon/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/ophthalmologist/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/thoracic-surgeon/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/nephrologist/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/oncologist/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/cosmetic-surgeon/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/dermatologist/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/vascular-surgeon/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/orthopedic-surgeon/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/andrologist/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/ivf-specialist/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/general-medicine/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/ayurveda-specialist/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/gastroenterologist/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/neurophysiologist/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	#self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/oncologist/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/bariatric-specialist/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ludhiana/acupuncturist/true_/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)])

        super(TravelSpider, self).__init__(name, **kwargs)
	
    
    name = "spider_ludhiana"
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