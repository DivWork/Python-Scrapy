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
        self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/jaipur/gynecologist/true_/doc_/%d?lat=26.910528&lng=75.802200" % k for k in xrange(5)]),
        self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/jaipur/gynecologist/true_/doc_/%d?lat=26.910528&lng=75.802200" % k for k in xrange(5)]),
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/jaipur/general-physician/true_/doc_/%d?lat=12.325780&lng=76.629440" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/jaipur/pediatrician/true_/doc_/%d?lat=26.910528&lng=75.802200" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/jaipur/colorectal-specialist/true_/doc_/%d?lat=26.910528&lng=75.802200" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/jaipur/cardiologist/true_/doc_/%d?lat=26.910528&lng=75.802200" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/jaipur/diabetologist/true_/doc_/%d?lat=26.910528&lng=75.802200" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/jaipur/dentist/true_/doc_/%d?lat=26.910528&lng=75.802200" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/jaipur/ent-specialist/true_/doc_/%d?lat=26.910528&lng=75.802200" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/jaipur/neurologist/true_/doc_/%d?lat=26.910528&lng=75.802200" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/jaipur/urologist/true_/doc_/%d?lat=26.910528&lng=75.802200" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/jaipur/psychiatrist/true_/doc_/%d?lat=26.910528&lng=75.802200" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/jaipur/immunologist/true_/doc_/%d?lat=26.910528&lng=75.802200" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/jaipur/pulmonologist/true_/doc_/%d?lat=26.910528&lng=75.802200" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/jaipur/yoga-specialist/true_/doc_/%d?lat=26.910528&lng=75.802200" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/jaipur/psychotherapist/true_/doc_/%d?lat=26.910528&lng=75.802200" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/jaipur/audiologist/true_/doc_/%d?lat=26.910528&lng=75.802200" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/jaipur/physiotherapist/true_/doc_/%d?lat=26.910528&lng=75.802200" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/jaipur/endocrinologist/true_/doc_/%d?lat=26.910528&lng=75.802200" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/jaipur/homoeopath/true_/doc_/%d?lat=26.910528&lng=75.802200" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/jaipur/neurosurgeon/true_/doc_/%d?lat=26.910528&lng=75.802200" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/jaipur/ophthalmologist/true_/doc_/%d?lat=26.910528&lng=75.802200" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/jaipur/thoracic-surgeon/true_/doc_/%d?lat=26.910528&lng=75.802200" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/jaipur/nephrologist/true_/doc_/%d?lat=26.910528&lng=75.802200" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/jaipur/oncologist/true_/doc_/%d?lat=26.910528&lng=75.802200" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/jaipur/cosmetic-surgeon/true_/doc_/%d?lat=26.910528&lng=75.802200" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/jaipur/dermatologist/true_/doc_/%d?lat=26.910528&lng=75.802200" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/jaipur/vascular-surgeon/true_/doc_/%d?lat=26.910528&lng=75.802200" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/jaipur/orthopedic-surgeon/true_/doc_/%d?lat=26.910528&lng=75.802200" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/jaipur/andrologist/true_/doc_/%d?lat=26.910528&lng=75.802200" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/jaipur/ivf-specialist/true_/doc_/%d?lat=26.910528&lng=75.802200" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/jaipur/general-medicine/true_/doc_/%d?lat=26.910528&lng=75.802200" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/jaipur/ayurveda-specialist/true_/doc_/%d?lat=26.910528&lng=75.802200" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/jaipur/gastroenterologist/true_/doc_/%d?lat=26.910528&lng=75.802200" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/jaipur/neurophysiologist/true_/doc_/%d?lat=26.910528&lng=75.802200" % k for k in xrange(5)])
	#self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/jaipur/oncologist/true_/doc_/%d?lat=26.910528&lng=75.802200" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/jaipur/bariatric-specialist/true_/doc_/%d?lat=26.910528&lng=75.802200" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/jaipur/acupuncturist/true_/doc_/%d?lat=26.910528&lng=75.802200" % k for k in xrange(5)])

        super(TravelSpider, self).__init__(name, **kwargs)
	
    
    name = "spider_jaipur"
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
