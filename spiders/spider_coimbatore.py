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
        self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/coimbatore/gynecologist/true_/doc_/%d?lat=11.021102&lng=76.966820" % k for k in xrange(5)]),
        self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/coimbatore/gynecologist/true_/doc_/%d?lat=11.021102&lng=76.966820" % k for k in xrange(5)]),
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/coimbatore/general-physician/true_/doc_/%d?lat=12.325780&lng=76.629440" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/coimbatore/pediatrician/true_/doc_/%d?lat=11.021102&lng=76.966820" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/coimbatore/colorectal-specialist/true_/doc_/%d?lat=11.021102&lng=76.966820" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/coimbatore/cardiologist/true_/doc_/%d?lat=11.021102&lng=76.966820" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/coimbatore/diabetologist/true_/doc_/%d?lat=11.021102&lng=76.966820" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/coimbatore/dentist/true_/doc_/%d?lat=11.021102&lng=76.966820" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/coimbatore/ent-specialist/true_/doc_/%d?lat=11.021102&lng=76.966820" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/coimbatore/neurologist/true_/doc_/%d?lat=11.021102&lng=76.966820" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/coimbatore/urologist/true_/doc_/%d?lat=11.021102&lng=76.966820" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/coimbatore/psychiatrist/true_/doc_/%d?lat=11.021102&lng=76.966820" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/coimbatore/immunologist/true_/doc_/%d?lat=11.021102&lng=76.966820" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/coimbatore/pulmonologist/true_/doc_/%d?lat=11.021102&lng=76.966820" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/coimbatore/yoga-specialist/true_/doc_/%d?lat=11.021102&lng=76.966820" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/coimbatore/psychotherapist/true_/doc_/%d?lat=11.021102&lng=76.966820" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/coimbatore/audiologist/true_/doc_/%d?lat=11.021102&lng=76.966820" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/coimbatore/physiotherapist/true_/doc_/%d?lat=11.021102&lng=76.966820" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/coimbatore/endocrinologist/true_/doc_/%d?lat=11.021102&lng=76.966820" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/coimbatore/homoeopath/true_/doc_/%d?lat=11.021102&lng=76.966820" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/coimbatore/neurosurgeon/true_/doc_/%d?lat=11.021102&lng=76.966820" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/coimbatore/ophthalmologist/true_/doc_/%d?lat=11.021102&lng=76.966820" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/coimbatore/thoracic-surgeon/true_/doc_/%d?lat=11.021102&lng=76.966820" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/coimbatore/nephrologist/true_/doc_/%d?lat=11.021102&lng=76.966820" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/coimbatore/oncologist/true_/doc_/%d?lat=11.021102&lng=76.966820" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/coimbatore/cosmetic-surgeon/true_/doc_/%d?lat=11.021102&lng=76.966820" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/coimbatore/dermatologist/true_/doc_/%d?lat=11.021102&lng=76.966820" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/coimbatore/vascular-surgeon/true_/doc_/%d?lat=11.021102&lng=76.966820" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/coimbatore/orthopedic-surgeon/true_/doc_/%d?lat=11.021102&lng=76.966820" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/coimbatore/andrologist/true_/doc_/%d?lat=11.021102&lng=76.966820" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/coimbatore/ivf-specialist/true_/doc_/%d?lat=11.021102&lng=76.966820" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/coimbatore/general-medicine/true_/doc_/%d?lat=11.021102&lng=76.966820" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/coimbatore/ayurveda-specialist/true_/doc_/%d?lat=11.021102&lng=76.966820" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/coimbatore/gastroenterologist/true_/doc_/%d?lat=11.021102&lng=76.966820" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/coimbatore/neurophysiologist/true_/doc_/%d?lat=11.021102&lng=76.966820" % k for k in xrange(5)])
	#self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/coimbatore/oncologist/true_/doc_/%d?lat=11.021102&lng=76.966820" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/coimbatore/bariatric-specialist/true_/doc_/%d?lat=11.021102&lng=76.966820" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/coimbatore/acupuncturist/true_/doc_/%d?lat=11.021102&lng=76.966820" % k for k in xrange(5)])

        super(TravelSpider, self).__init__(name, **kwargs)
	
    
    name = "spider_coimbatore"
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
