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
        self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/gynecologist/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)]),
        self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/gynecologist/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)]),
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/general-physician/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/pediatrician/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/colorectal-specialist/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/cardiologist/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/diabetologist/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/dentist/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/ent-specialist/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/neurologist/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/urologist/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/psychiatrist/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/immunologist/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/pulmonologist/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/yoga-specialist/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/psychotherapist/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/audiologist/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/physiotherapist/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/endocrinologist/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/homoeopath/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/neurosurgeon/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/ophthalmologist/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/thoracic-surgeon/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/nephrologist/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/oncologist/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/cosmetic-surgeon/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/dermatologist/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/vascular-surgeon/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/orthopedic-surgeon/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/andrologist/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/ivf-specialist/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/general-medicine/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/ayurveda-specialist/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/gastroenterologist/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/neurophysiologist/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	#self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/oncologist/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/bariatric-specialist/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/vadodara/acupuncturist/true_/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)])

        super(TravelSpider, self).__init__(name, **kwargs)
	
    
    name = "spider_vadodara"
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
