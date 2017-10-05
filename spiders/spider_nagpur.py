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
        self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/nagpur/gynecologist/true_/doc_/%d?lat=21.130047&lng=79.079376" % k for k in xrange(5)]),
        self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/nagpur/gynecologist/true_/doc_/%d?lat=21.130047&lng=79.079376" % k for k in xrange(5)]),
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/nagpur/general-physician/true_/doc_/%d?lat=12.325780&lng=76.629440" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/nagpur/pediatrician/true_/doc_/%d?lat=21.130047&lng=79.079376" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/nagpur/colorectal-specialist/true_/doc_/%d?lat=21.130047&lng=79.079376" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/nagpur/cardiologist/true_/doc_/%d?lat=21.130047&lng=79.079376" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/nagpur/diabetologist/true_/doc_/%d?lat=21.130047&lng=79.079376" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/nagpur/dentist/true_/doc_/%d?lat=21.130047&lng=79.079376" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/nagpur/ent-specialist/true_/doc_/%d?lat=21.130047&lng=79.079376" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/nagpur/neurologist/true_/doc_/%d?lat=21.130047&lng=79.079376" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/nagpur/urologist/true_/doc_/%d?lat=21.130047&lng=79.079376" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/nagpur/psychiatrist/true_/doc_/%d?lat=21.130047&lng=79.079376" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/nagpur/immunologist/true_/doc_/%d?lat=21.130047&lng=79.079376" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/nagpur/pulmonologist/true_/doc_/%d?lat=21.130047&lng=79.079376" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/nagpur/yoga-specialist/true_/doc_/%d?lat=21.130047&lng=79.079376" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/nagpur/psychotherapist/true_/doc_/%d?lat=21.130047&lng=79.079376" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/nagpur/audiologist/true_/doc_/%d?lat=21.130047&lng=79.079376" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/nagpur/physiotherapist/true_/doc_/%d?lat=21.130047&lng=79.079376" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/nagpur/endocrinologist/true_/doc_/%d?lat=21.130047&lng=79.079376" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/nagpur/homoeopath/true_/doc_/%d?lat=21.130047&lng=79.079376" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/nagpur/neurosurgeon/true_/doc_/%d?lat=21.130047&lng=79.079376" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/nagpur/ophthalmologist/true_/doc_/%d?lat=21.130047&lng=79.079376" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/nagpur/thoracic-surgeon/true_/doc_/%d?lat=21.130047&lng=79.079376" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/nagpur/nephrologist/true_/doc_/%d?lat=21.130047&lng=79.079376" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/nagpur/oncologist/true_/doc_/%d?lat=21.130047&lng=79.079376" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/nagpur/cosmetic-surgeon/true_/doc_/%d?lat=21.130047&lng=79.079376" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/nagpur/dermatologist/true_/doc_/%d?lat=21.130047&lng=79.079376" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/nagpur/vascular-surgeon/true_/doc_/%d?lat=21.130047&lng=79.079376" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/nagpur/orthopedic-surgeon/true_/doc_/%d?lat=21.130047&lng=79.079376" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/nagpur/andrologist/true_/doc_/%d?lat=21.130047&lng=79.079376" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/nagpur/ivf-specialist/true_/doc_/%d?lat=21.130047&lng=79.079376" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/nagpur/general-medicine/true_/doc_/%d?lat=21.130047&lng=79.079376" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/nagpur/ayurveda-specialist/true_/doc_/%d?lat=21.130047&lng=79.079376" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/nagpur/gastroenterologist/true_/doc_/%d?lat=21.130047&lng=79.079376" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/nagpur/neurophysiologist/true_/doc_/%d?lat=21.130047&lng=79.079376" % k for k in xrange(5)])
	#self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/nagpur/oncologist/true_/doc_/%d?lat=21.130047&lng=79.079376" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/nagpur/bariatric-specialist/true_/doc_/%d?lat=21.130047&lng=79.079376" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/nagpur/acupuncturist/true_/doc_/%d?lat=21.130047&lng=79.079376" % k for k in xrange(5)])

        super(TravelSpider, self).__init__(name, **kwargs)
	
    
    name = "spider_nagpur"
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
