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
        self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/lucknow/gynecologist/true_/doc_/%d?lat=26.879892&lng=80.992630" % k for k in xrange(5)]),
        self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/lucknow/gynecologist/true_/doc_/%d?lat=26.879892&lng=80.992630" % k for k in xrange(5)]),
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/lucknow/general-physician/true_/doc_/%d?lat=12.325780&lng=76.629440" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/lucknow/pediatrician/true_/doc_/%d?lat=26.879892&lng=80.992630" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/lucknow/colorectal-specialist/true_/doc_/%d?lat=26.879892&lng=80.992630" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/lucknow/cardiologist/true_/doc_/%d?lat=26.879892&lng=80.992630" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/lucknow/diabetologist/true_/doc_/%d?lat=26.879892&lng=80.992630" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/lucknow/dentist/true_/doc_/%d?lat=26.879892&lng=80.992630" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/lucknow/ent-specialist/true_/doc_/%d?lat=26.879892&lng=80.992630" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/lucknow/neurologist/true_/doc_/%d?lat=26.879892&lng=80.992630" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/lucknow/urologist/true_/doc_/%d?lat=26.879892&lng=80.992630" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/lucknow/psychiatrist/true_/doc_/%d?lat=26.879892&lng=80.992630" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/lucknow/immunologist/true_/doc_/%d?lat=26.879892&lng=80.992630" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/lucknow/pulmonologist/true_/doc_/%d?lat=26.879892&lng=80.992630" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/lucknow/yoga-specialist/true_/doc_/%d?lat=26.879892&lng=80.992630" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/lucknow/psychotherapist/true_/doc_/%d?lat=26.879892&lng=80.992630" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/lucknow/audiologist/true_/doc_/%d?lat=26.879892&lng=80.992630" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/lucknow/physiotherapist/true_/doc_/%d?lat=26.879892&lng=80.992630" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/lucknow/endocrinologist/true_/doc_/%d?lat=26.879892&lng=80.992630" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/lucknow/homoeopath/true_/doc_/%d?lat=26.879892&lng=80.992630" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/lucknow/neurosurgeon/true_/doc_/%d?lat=26.879892&lng=80.992630" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/lucknow/ophthalmologist/true_/doc_/%d?lat=26.879892&lng=80.992630" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/lucknow/thoracic-surgeon/true_/doc_/%d?lat=26.879892&lng=80.992630" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/lucknow/nephrologist/true_/doc_/%d?lat=26.879892&lng=80.992630" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/lucknow/oncologist/true_/doc_/%d?lat=26.879892&lng=80.992630" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/lucknow/cosmetic-surgeon/true_/doc_/%d?lat=26.879892&lng=80.992630" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/lucknow/dermatologist/true_/doc_/%d?lat=26.879892&lng=80.992630" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/lucknow/vascular-surgeon/true_/doc_/%d?lat=26.879892&lng=80.992630" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/lucknow/orthopedic-surgeon/true_/doc_/%d?lat=26.879892&lng=80.992630" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/lucknow/andrologist/true_/doc_/%d?lat=26.879892&lng=80.992630" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/lucknow/ivf-specialist/true_/doc_/%d?lat=26.879892&lng=80.992630" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/lucknow/general-medicine/true_/doc_/%d?lat=26.879892&lng=80.992630" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/lucknow/ayurveda-specialist/true_/doc_/%d?lat=26.879892&lng=80.992630" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/lucknow/gastroenterologist/true_/doc_/%d?lat=26.879892&lng=80.992630" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/lucknow/neurophysiologist/true_/doc_/%d?lat=26.879892&lng=80.992630" % k for k in xrange(5)])
	#self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/lucknow/oncologist/true_/doc_/%d?lat=26.879892&lng=80.992630" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/lucknow/bariatric-specialist/true_/doc_/%d?lat=26.879892&lng=80.992630" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/lucknow/acupuncturist/true_/doc_/%d?lat=26.879892&lng=80.992630" % k for k in xrange(5)])

        super(TravelSpider, self).__init__(name, **kwargs)
	
    
    name = "spider_lucknow"
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
