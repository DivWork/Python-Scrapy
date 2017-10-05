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
        self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/pune/gynecologist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)]),
        self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/pune/gynecologist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)]),
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/pune/general-physician/true_/doc_/%d?lat=12.325780&lng=76.629440" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/pune/pediatrician/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/pune/colorectal-specialist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/pune/cardiologist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/pune/diabetologist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/pune/dentist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/pune/ent-specialist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/pune/neurologist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/pune/urologist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/pune/psychiatrist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/pune/immunologist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/pune/pulmonologist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/pune/yoga-specialist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/pune/psychotherapist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/pune/audiologist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/pune/physiotherapist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/pune/endocrinologist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/pune/homoeopath/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/pune/neurosurgeon/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/pune/ophthalmologist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/pune/thoracic-surgeon/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/pune/nephrologist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/pune/oncologist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/pune/cosmetic-surgeon/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/pune/dermatologist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/pune/vascular-surgeon/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/pune/orthopedic-surgeon/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/pune/andrologist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/pune/ivf-specialist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/pune/general-medicine/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/pune/ayurveda-specialist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/pune/gastroenterologist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/pune/neurophysiologist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	#self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/pune/oncologist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/pune/bariatric-specialist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/pune/acupuncturist/true_/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)])

        super(TravelSpider, self).__init__(name, **kwargs)
	
    
    name = "spider_pune"
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
