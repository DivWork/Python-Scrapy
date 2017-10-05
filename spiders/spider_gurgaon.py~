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
        self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/gurgaon/gynecologist/true_/doc_/%d?lat=28.578321&lng=77.317818" % k for k in xrange(5)]),
        self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/gurgaon/gynecologist/true_/doc_/%d?lat=28.578321&lng=77.317818" % k for k in xrange(5)]),
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/gurgaon/general-physician/true_/doc_/%d?lat=12.325780&lng=76.629440" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/gurgaon/pediatrician/true_/doc_/%d?lat=28.578321&lng=77.317818" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/gurgaon/colorectal-specialist/true_/doc_/%d?lat=28.578321&lng=77.317818" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/gurgaon/cardiologist/true_/doc_/%d?lat=28.578321&lng=77.317818" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/gurgaon/diabetologist/true_/doc_/%d?lat=28.578321&lng=77.317818" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/gurgaon/dentist/true_/doc_/%d?lat=28.578321&lng=77.317818" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/gurgaon/ent-specialist/true_/doc_/%d?lat=28.578321&lng=77.317818" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/gurgaon/neurologist/true_/doc_/%d?lat=28.578321&lng=77.317818" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/gurgaon/urologist/true_/doc_/%d?lat=28.578321&lng=77.317818" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/gurgaon/psychiatrist/true_/doc_/%d?lat=28.578321&lng=77.317818" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/gurgaon/immunologist/true_/doc_/%d?lat=28.578321&lng=77.317818" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/gurgaon/pulmonologist/true_/doc_/%d?lat=28.578321&lng=77.317818" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/gurgaon/yoga-specialist/true_/doc_/%d?lat=28.578321&lng=77.317818" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/gurgaon/psychotherapist/true_/doc_/%d?lat=28.578321&lng=77.317818" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/gurgaon/audiologist/true_/doc_/%d?lat=28.578321&lng=77.317818" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/gurgaon/physiotherapist/true_/doc_/%d?lat=28.578321&lng=77.317818" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/gurgaon/endocrinologist/true_/doc_/%d?lat=28.578321&lng=77.317818" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/gurgaon/homoeopath/true_/doc_/%d?lat=28.578321&lng=77.317818" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/gurgaon/neurosurgeon/true_/doc_/%d?lat=28.578321&lng=77.317818" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/gurgaon/ophthalmologist/true_/doc_/%d?lat=28.578321&lng=77.317818" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/gurgaon/thoracic-surgeon/true_/doc_/%d?lat=28.578321&lng=77.317818" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/gurgaon/nephrologist/true_/doc_/%d?lat=28.578321&lng=77.317818" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/gurgaon/oncologist/true_/doc_/%d?lat=28.578321&lng=77.317818" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/gurgaon/cosmetic-surgeon/true_/doc_/%d?lat=28.578321&lng=77.317818" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/gurgaon/dermatologist/true_/doc_/%d?lat=28.578321&lng=77.317818" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/gurgaon/vascular-surgeon/true_/doc_/%d?lat=28.578321&lng=77.317818" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/gurgaon/orthopedic-surgeon/true_/doc_/%d?lat=28.578321&lng=77.317818" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/gurgaon/andrologist/true_/doc_/%d?lat=28.578321&lng=77.317818" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/gurgaon/ivf-specialist/true_/doc_/%d?lat=28.578321&lng=77.317818" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/gurgaon/general-medicine/true_/doc_/%d?lat=28.578321&lng=77.317818" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/gurgaon/ayurveda-specialist/true_/doc_/%d?lat=28.578321&lng=77.317818" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/gurgaon/gastroenterologist/true_/doc_/%d?lat=28.578321&lng=77.317818" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/gurgaon/neurophysiologist/true_/doc_/%d?lat=28.578321&lng=77.317818" % k for k in xrange(5)])
	#self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/gurgaon/oncologist/true_/doc_/%d?lat=28.578321&lng=77.317818" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/gurgaon/bariatric-specialist/true_/doc_/%d?lat=28.578321&lng=77.317818" % k for k in xrange(5)])
	self.start_urls.extend(["http://www.medinfi.com/medinfi/doctor-search/gurgaon/acupuncturist/true_/doc_/%d?lat=28.578321&lng=77.317818" % k for k in xrange(5)])

        super(TravelSpider, self).__init__(name, **kwargs)
	
    
    name = "spider_gurgaon"
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
