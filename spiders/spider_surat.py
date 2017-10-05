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
        self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/gynecologist/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)]),
        self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/gynecologist/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)]),
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/general-physician/true_/doc_/%d?lat=12.325780&lng=76.629440" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/pediatrician/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/colorectal-specialist/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/cardiologist/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/diabetologist/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/dentist/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/ent-specialist/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/neurologist/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/urologist/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/psychiatrist/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/immunologist/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/pulmonologist/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/yoga-specialist/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/psychotherapist/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/audiologist/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/physiotherapist/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/endocrinologist/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/homoeopath/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/neurosurgeon/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/ophthalmologist/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/thoracic-surgeon/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/nephrologist/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/oncologist/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/cosmetic-surgeon/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/dermatologist/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/vascular-surgeon/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/orthopedic-surgeon/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/andrologist/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/ivf-specialist/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/general-medicine/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/ayurveda-specialist/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/gastroenterologist/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/neurophysiologist/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	#self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/oncologist/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/bariatric-specialist/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/surat/acupuncturist/true_/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)])

        super(TravelSpider, self).__init__(name, **kwargs)
	
    
    name = "spider_surat"
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
