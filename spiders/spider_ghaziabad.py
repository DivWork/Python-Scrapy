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
        self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ghaziabad/gynecologist/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)]),
        self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ghaziabad/gynecologist/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)]),
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ghaziabad/general-physician/true_/doc_/%d?lat=12.325780&lng=76.629440" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ghaziabad/pediatrician/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ghaziabad/colorectal-specialist/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ghaziabad/cardiologist/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ghaziabad/diabetologist/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ghaziabad/dentist/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ghaziabad/ent-specialist/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ghaziabad/neurologist/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ghaziabad/urologist/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ghaziabad/psychiatrist/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ghaziabad/immunologist/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ghaziabad/pulmonologist/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ghaziabad/yoga-specialist/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ghaziabad/psychotherapist/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ghaziabad/audiologist/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ghaziabad/physiotherapist/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ghaziabad/endocrinologist/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ghaziabad/homoeopath/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ghaziabad/neurosurgeon/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ghaziabad/ophthalmologist/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ghaziabad/thoracic-surgeon/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ghaziabad/nephrologist/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ghaziabad/oncologist/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ghaziabad/cosmetic-surgeon/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ghaziabad/dermatologist/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ghaziabad/vascular-surgeon/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ghaziabad/orthopedic-surgeon/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ghaziabad/andrologist/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ghaziabad/ivf-specialist/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ghaziabad/general-medicine/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ghaziabad/ayurveda-specialist/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ghaziabad/gastroenterologist/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ghaziabad/neurophysiologist/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	#self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ghaziabad/oncologist/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ghaziabad/bariatric-specialist/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/ghaziabad/acupuncturist/true_/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)])

        super(TravelSpider, self).__init__(name, **kwargs)
	
    
    name = "spider_ghaziabad"
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
