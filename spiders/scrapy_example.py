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
        #self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bengaluru/gynecologist/true_/doc_/%d?lat=12.933221&lng=77.632195" % k for k in xrange(5)]),
        self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bengaluru/gynecologist/true_/doc_/%d?lat=12.933221&lng=77.632195" % k for k in xrange(5)]),
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bengaluru/general-physician/true_/doc_/%d?lat=12.325780&lng=76.629440" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bengaluru/pediatrician/true_/doc_/%d?lat=12.933221&lng=77.632195" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bengaluru/colorectal-specialist/true_/doc_/%d?lat=12.933221&lng=77.632195" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bengaluru/cardiologist/true_/doc_/%d?lat=12.933221&lng=77.632195" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bengaluru/diabetologist/true_/doc_/%d?lat=12.933221&lng=77.632195" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bengaluru/dentist/true_/doc_/%d?lat=12.933221&lng=77.632195" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bengaluru/ent-specialist/true_/doc_/%d?lat=12.933221&lng=77.632195" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bengaluru/neurologist/true_/doc_/%d?lat=12.933221&lng=77.632195" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bengaluru/urologist/true_/doc_/%d?lat=12.933221&lng=77.632195" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bengaluru/psychiatrist/true_/doc_/%d?lat=12.933221&lng=77.632195" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bengaluru/immunologist/true_/doc_/%d?lat=12.933221&lng=77.632195" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bengaluru/pulmonologist/true_/doc_/%d?lat=12.933221&lng=77.632195" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bengaluru/yoga-specialist/true_/doc_/%d?lat=12.933221&lng=77.632195" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bengaluru/psychotherapist/true_/doc_/%d?lat=12.933221&lng=77.632195" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bengaluru/audiologist/true_/doc_/%d?lat=12.933221&lng=77.632195" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bengaluru/physiotherapist/true_/doc_/%d?lat=12.933221&lng=77.632195" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bengaluru/endocrinologist/true_/doc_/%d?lat=12.933221&lng=77.632195" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bengaluru/homoeopath/true_/doc_/%d?lat=12.933221&lng=77.632195" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bengaluru/neurosurgeon/true_/doc_/%d?lat=12.933221&lng=77.632195" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bengaluru/ophthalmologist/true_/doc_/%d?lat=12.933221&lng=77.632195" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bengaluru/thoracic-surgeon/true_/doc_/%d?lat=12.933221&lng=77.632195" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bengaluru/nephrologist/true_/doc_/%d?lat=12.933221&lng=77.632195" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bengaluru/oncologist/true_/doc_/%d?lat=12.933221&lng=77.632195" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bengaluru/cosmetic-surgeon/true_/doc_/%d?lat=12.933221&lng=77.632195" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bengaluru/dermatologist/true_/doc_/%d?lat=12.933221&lng=77.632195" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bengaluru/vascular-surgeon/true_/doc_/%d?lat=12.933221&lng=77.632195" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bengaluru/orthopedic-surgeon/true_/doc_/%d?lat=12.933221&lng=77.632195" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bengaluru/andrologist/true_/doc_/%d?lat=12.933221&lng=77.632195" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bengaluru/ivf-specialist/true_/doc_/%d?lat=12.933221&lng=77.632195" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bengaluru/general-medicine/true_/doc_/%d?lat=12.933221&lng=77.632195" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bengaluru/ayurveda-specialist/true_/doc_/%d?lat=12.933221&lng=77.632195" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bengaluru/gastroenterologist/true_/doc_/%d?lat=12.933221&lng=77.632195" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bengaluru/neurophysiologist/true_/doc_/%d?lat=12.933221&lng=77.632195" % k for k in xrange(5)])
	#self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bengaluru/oncologist/true_/doc_/%d?lat=12.933221&lng=77.632195" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bengaluru/bariatric-specialist/true_/doc_/%d?lat=12.933221&lng=77.632195" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/bengaluru/acupuncturist/true_/doc_/%d?lat=12.933221&lng=77.632195" % k for k in xrange(5)])

        super(TravelSpider, self).__init__(name, **kwargs)
	
    
    name = "spider_monster"
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
