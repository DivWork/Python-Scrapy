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
        self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chennai/gynecologist/true_/doc_/%d?lat=12.975971&lng=80.221207" % k for k in xrange(5)]),
        self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chennai/gynecologist/true_/doc_/%d?lat=12.975971&lng=80.221207" % k for k in xrange(5)]),
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chennai/general-physician/true_/doc_/%d?lat=12.325780&lng=76.629440" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chennai/pediatrician/true_/doc_/%d?lat=12.975971&lng=80.221207" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chennai/colorectal-specialist/true_/doc_/%d?lat=12.975971&lng=80.221207" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chennai/cardiologist/true_/doc_/%d?lat=12.975971&lng=80.221207" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chennai/diabetologist/true_/doc_/%d?lat=12.975971&lng=80.221207" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chennai/dentist/true_/doc_/%d?lat=12.975971&lng=80.221207" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chennai/ent-specialist/true_/doc_/%d?lat=12.975971&lng=80.221207" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chennai/neurologist/true_/doc_/%d?lat=12.975971&lng=80.221207" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chennai/urologist/true_/doc_/%d?lat=12.975971&lng=80.221207" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chennai/psychiatrist/true_/doc_/%d?lat=12.975971&lng=80.221207" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chennai/immunologist/true_/doc_/%d?lat=12.975971&lng=80.221207" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chennai/pulmonologist/true_/doc_/%d?lat=12.975971&lng=80.221207" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chennai/yoga-specialist/true_/doc_/%d?lat=12.975971&lng=80.221207" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chennai/psychotherapist/true_/doc_/%d?lat=12.975971&lng=80.221207" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chennai/audiologist/true_/doc_/%d?lat=12.975971&lng=80.221207" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chennai/physiotherapist/true_/doc_/%d?lat=12.975971&lng=80.221207" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chennai/endocrinologist/true_/doc_/%d?lat=12.975971&lng=80.221207" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chennai/homoeopath/true_/doc_/%d?lat=12.975971&lng=80.221207" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chennai/neurosurgeon/true_/doc_/%d?lat=12.975971&lng=80.221207" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chennai/ophthalmologist/true_/doc_/%d?lat=12.975971&lng=80.221207" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chennai/thoracic-surgeon/true_/doc_/%d?lat=12.975971&lng=80.221207" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chennai/nephrologist/true_/doc_/%d?lat=12.975971&lng=80.221207" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chennai/oncologist/true_/doc_/%d?lat=12.975971&lng=80.221207" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chennai/cosmetic-surgeon/true_/doc_/%d?lat=12.975971&lng=80.221207" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chennai/dermatologist/true_/doc_/%d?lat=12.975971&lng=80.221207" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chennai/vascular-surgeon/true_/doc_/%d?lat=12.975971&lng=80.221207" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chennai/orthopedic-surgeon/true_/doc_/%d?lat=12.975971&lng=80.221207" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chennai/andrologist/true_/doc_/%d?lat=12.975971&lng=80.221207" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chennai/ivf-specialist/true_/doc_/%d?lat=12.975971&lng=80.221207" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chennai/general-medicine/true_/doc_/%d?lat=12.975971&lng=80.221207" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chennai/ayurveda-specialist/true_/doc_/%d?lat=12.975971&lng=80.221207" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chennai/gastroenterologist/true_/doc_/%d?lat=12.975971&lng=80.221207" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chennai/neurophysiologist/true_/doc_/%d?lat=12.975971&lng=80.221207" % k for k in xrange(5)])
	#self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chennai/oncologist/true_/doc_/%d?lat=12.975971&lng=80.221207" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chennai/bariatric-specialist/true_/doc_/%d?lat=12.975971&lng=80.221207" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/chennai/acupuncturist/true_/doc_/%d?lat=12.975971&lng=80.221207" % k for k in xrange(5)])

        super(TravelSpider, self).__init__(name, **kwargs)
	
    
    name = "spider_chennai"
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
