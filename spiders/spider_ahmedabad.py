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
        self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/gynecologist/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)]),
        self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/gynecologist/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)]),
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/general-physician/true_/doc_/%d?lat=12.325780&lng=76.629440" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/pediatrician/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/colorectal-specialist/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/cardiologist/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/diabetologist/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/dentist/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/ent-specialist/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/neurologist/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/urologist/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/psychiatrist/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/immunologist/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/pulmonologist/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/yoga-specialist/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/psychotherapist/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/audiologist/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/physiotherapist/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/endocrinologist/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/homoeopath/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/neurosurgeon/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/ophthalmologist/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/thoracic-surgeon/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/nephrologist/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/oncologist/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/cosmetic-surgeon/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/dermatologist/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/vascular-surgeon/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/orthopedic-surgeon/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/andrologist/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/ivf-specialist/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/general-medicine/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/ayurveda-specialist/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/gastroenterologist/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/neurophysiologist/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	#self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/oncologist/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/bariatric-specialist/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ahmedabad/acupuncturist/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])

        super(TravelSpider, self).__init__(name, **kwargs)
	
    
    name = "spider_ahmedabad"
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
