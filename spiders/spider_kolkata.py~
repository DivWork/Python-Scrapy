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
        self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/kolkata/gynecologist/true_/doc_/%d?lat=22.498140&lng=88.310837" % k for k in xrange(5)]),
        self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/kolkata/gynecologist/true_/doc_/%d?lat=22.498140&lng=88.310837" % k for k in xrange(5)]),
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/kolkata/general-physician/true_/doc_/%d?lat=12.325780&lng=76.629440" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/kolkata/pediatrician/true_/doc_/%d?lat=22.498140&lng=88.310837" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/kolkata/colorectal-specialist/true_/doc_/%d?lat=22.498140&lng=88.310837" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/kolkata/cardiologist/true_/doc_/%d?lat=22.498140&lng=88.310837" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/kolkata/diabetologist/true_/doc_/%d?lat=22.498140&lng=88.310837" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/kolkata/dentist/true_/doc_/%d?lat=22.498140&lng=88.310837" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/kolkata/ent-specialist/true_/doc_/%d?lat=22.498140&lng=88.310837" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/kolkata/neurologist/true_/doc_/%d?lat=22.498140&lng=88.310837" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/kolkata/urologist/true_/doc_/%d?lat=22.498140&lng=88.310837" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/kolkata/psychiatrist/true_/doc_/%d?lat=22.498140&lng=88.310837" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/kolkata/immunologist/true_/doc_/%d?lat=22.498140&lng=88.310837" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/kolkata/pulmonologist/true_/doc_/%d?lat=22.498140&lng=88.310837" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/kolkata/yoga-specialist/true_/doc_/%d?lat=22.498140&lng=88.310837" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/kolkata/psychotherapist/true_/doc_/%d?lat=22.498140&lng=88.310837" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/kolkata/audiologist/true_/doc_/%d?lat=22.498140&lng=88.310837" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/kolkata/physiotherapist/true_/doc_/%d?lat=22.498140&lng=88.310837" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/kolkata/endocrinologist/true_/doc_/%d?lat=22.498140&lng=88.310837" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/kolkata/homoeopath/true_/doc_/%d?lat=22.498140&lng=88.310837" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/kolkata/neurosurgeon/true_/doc_/%d?lat=22.498140&lng=88.310837" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/kolkata/ophthalmologist/true_/doc_/%d?lat=22.498140&lng=88.310837" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/kolkata/thoracic-surgeon/true_/doc_/%d?lat=22.498140&lng=88.310837" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/kolkata/nephrologist/true_/doc_/%d?lat=22.498140&lng=88.310837" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/kolkata/oncologist/true_/doc_/%d?lat=22.498140&lng=88.310837" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/kolkata/cosmetic-surgeon/true_/doc_/%d?lat=22.498140&lng=88.310837" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/kolkata/dermatologist/true_/doc_/%d?lat=22.498140&lng=88.310837" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/kolkata/vascular-surgeon/true_/doc_/%d?lat=22.498140&lng=88.310837" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/kolkata/orthopedic-surgeon/true_/doc_/%d?lat=22.498140&lng=88.310837" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/kolkata/andrologist/true_/doc_/%d?lat=22.498140&lng=88.310837" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/kolkata/ivf-specialist/true_/doc_/%d?lat=22.498140&lng=88.310837" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/kolkata/general-medicine/true_/doc_/%d?lat=22.498140&lng=88.310837" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/kolkata/ayurveda-specialist/true_/doc_/%d?lat=22.498140&lng=88.310837" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/kolkata/gastroenterologist/true_/doc_/%d?lat=22.498140&lng=88.310837" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/kolkata/neurophysiologist/true_/doc_/%d?lat=22.498140&lng=88.310837" % k for k in xrange(5)])
	#self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/kolkata/oncologist/true_/doc_/%d?lat=22.498140&lng=88.310837" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/kolkata/bariatric-specialist/true_/doc_/%d?lat=22.498140&lng=88.310837" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/kolkata/acupuncturist/true_/doc_/%d?lat=22.498140&lng=88.310837" % k for k in xrange(5)])

        super(TravelSpider, self).__init__(name, **kwargs)
	
    
    name = "spider_kolkata"
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
