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
        self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/thiruvananthapuram/gynecologist/true_/doc_/%d?lat=8.511871&lng=76.925537" % k for k in xrange(5)]),
        self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/thiruvananthapuram/gynecologist/true_/doc_/%d?lat=8.511871&lng=76.925537" % k for k in xrange(5)]),
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/thiruvananthapuram/general-physician/true_/doc_/%d?lat=12.325780&lng=76.629440" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/thiruvananthapuram/pediatrician/true_/doc_/%d?lat=8.511871&lng=76.925537" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/thiruvananthapuram/colorectal-specialist/true_/doc_/%d?lat=8.511871&lng=76.925537" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/thiruvananthapuram/cardiologist/true_/doc_/%d?lat=8.511871&lng=76.925537" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/thiruvananthapuram/diabetologist/true_/doc_/%d?lat=8.511871&lng=76.925537" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/thiruvananthapuram/dentist/true_/doc_/%d?lat=8.511871&lng=76.925537" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/thiruvananthapuram/ent-specialist/true_/doc_/%d?lat=8.511871&lng=76.925537" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/thiruvananthapuram/neurologist/true_/doc_/%d?lat=8.511871&lng=76.925537" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/thiruvananthapuram/urologist/true_/doc_/%d?lat=8.511871&lng=76.925537" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/thiruvananthapuram/psychiatrist/true_/doc_/%d?lat=8.511871&lng=76.925537" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/thiruvananthapuram/immunologist/true_/doc_/%d?lat=8.511871&lng=76.925537" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/thiruvananthapuram/pulmonologist/true_/doc_/%d?lat=8.511871&lng=76.925537" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/thiruvananthapuram/yoga-specialist/true_/doc_/%d?lat=8.511871&lng=76.925537" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/thiruvananthapuram/psychotherapist/true_/doc_/%d?lat=8.511871&lng=76.925537" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/thiruvananthapuram/audiologist/true_/doc_/%d?lat=8.511871&lng=76.925537" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/thiruvananthapuram/physiotherapist/true_/doc_/%d?lat=8.511871&lng=76.925537" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/thiruvananthapuram/endocrinologist/true_/doc_/%d?lat=8.511871&lng=76.925537" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/thiruvananthapuram/homoeopath/true_/doc_/%d?lat=8.511871&lng=76.925537" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/thiruvananthapuram/neurosurgeon/true_/doc_/%d?lat=8.511871&lng=76.925537" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/thiruvananthapuram/ophthalmologist/true_/doc_/%d?lat=8.511871&lng=76.925537" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/thiruvananthapuram/thoracic-surgeon/true_/doc_/%d?lat=8.511871&lng=76.925537" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/thiruvananthapuram/nephrologist/true_/doc_/%d?lat=8.511871&lng=76.925537" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/thiruvananthapuram/oncologist/true_/doc_/%d?lat=8.511871&lng=76.925537" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/thiruvananthapuram/cosmetic-surgeon/true_/doc_/%d?lat=8.511871&lng=76.925537" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/thiruvananthapuram/dermatologist/true_/doc_/%d?lat=8.511871&lng=76.925537" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/thiruvananthapuram/vascular-surgeon/true_/doc_/%d?lat=8.511871&lng=76.925537" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/thiruvananthapuram/orthopedic-surgeon/true_/doc_/%d?lat=8.511871&lng=76.925537" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/thiruvananthapuram/andrologist/true_/doc_/%d?lat=8.511871&lng=76.925537" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/thiruvananthapuram/ivf-specialist/true_/doc_/%d?lat=8.511871&lng=76.925537" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/thiruvananthapuram/general-medicine/true_/doc_/%d?lat=8.511871&lng=76.925537" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/thiruvananthapuram/ayurveda-specialist/true_/doc_/%d?lat=8.511871&lng=76.925537" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/thiruvananthapuram/gastroenterologist/true_/doc_/%d?lat=8.511871&lng=76.925537" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/thiruvananthapuram/neurophysiologist/true_/doc_/%d?lat=8.511871&lng=76.925537" % k for k in xrange(5)])
	#self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/thiruvananthapuram/oncologist/true_/doc_/%d?lat=8.511871&lng=76.925537" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/thiruvananthapuram/bariatric-specialist/true_/doc_/%d?lat=8.511871&lng=76.925537" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/thiruvananthapuram/acupuncturist/true_/doc_/%d?lat=8.511871&lng=76.925537" % k for k in xrange(5)])

        super(TravelSpider, self).__init__(name, **kwargs)
	
    
    name = "spider_thiruvananthapuram"
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
