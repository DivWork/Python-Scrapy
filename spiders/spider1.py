import scrapy

from newproject.items import NewprojectItem

class NewSpider(scrapy.Spider):
    name = "spider1"
    allowed_domains = ["medinfi.com"]
    start_urls = [
        "http://www.medinfi.com/medinfi/doctor-search/bengaluru/doc_/%d?lat=12.933221&lng=77.632195" % i for i in xrange(5)
	#"http://www.medinfi.com/medinfi/doctor-search/bengaluru/general-physician/true_/doc_/%d?lat=12.933221&lng=77.632195" % k for k in xrange(5)
	#"http://www.medinfi.com/medinfi/doctor-search/new-delhi/doc_/%d?lat=28.703215&lng=77.124519" % k for k in xrange(5)
	#"http://www.medinfi.com/medinfi/doctor-search/mumbai/doc_/%d?lat=19.113646&lng=72.869736" % k for k in xrange(5)
	#"http://www.medinfi.com/medinfi/doctor-search/hyderabad/doc_/%d?lat=17.437462&lng=78.448288" % k for k in xrange(5)
	#"http://www.medinfi.com/medinfi/doctor-search/kolkata/doc_/%d?lat=22.498140&lng=88.310837" % k for k in xrange(5)
	#"http://www.medinfi.com/medinfi/doctor-search/pune/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)
	#"http://www.medinfi.com/medinfi/doctor-search/ahmedabad/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)
	#"http://www.medinfi.com/medinfi/doctor-search/noida/doc_/%d?lat=18.557699&lng=73.798584" % k for k in xrange(5)
	#"http://www.medinfi.com/medinfi/doctor-search/jaipur/doc_/%d?lat=26.910528&lng=75.802200" % k for k in xrange(5)
	#"http://www.medinfi.com/medinfi/doctor-search/ghaziabad/doc_/%d?lat=23.019281&lng=72.518974" % k for k in xrange(5)
	#"http://www.medinfi.com/medinfi/doctor-search/navi-mumbai/doc_/%d?lat=19.042007&lng=73.026489" % k for k in xrange(5)
	#"http://www.medinfi.com/medinfi/doctor-search/gurgaon/doc_/%d?lat=28.578321&lng=77.317818" % k for k in xrange(5)
	#"http://www.medinfi.com/medinfi/doctor-search/lucknow/doc_/%d?lat=26.879892&lng=80.992630" % k for k in xrange(5)
	#"http://www.medinfi.com/medinfi/doctor-search/indore/doc_/%d?lat=22.725136&lng=75.892609" % k for k in xrange(5)
	#"http://www.medinfi.com/medinfi/doctor-search/bhopal/doc_/%d?lat=23.211283&lng=77.435089" % k for k in xrange(5)
	#"http://www.medinfi.com/medinfi/doctor-search/chandigarh/doc_/%d?lat=30.726053&lng=76.759628" % k for k in xrange(5)
	#"http://www.medinfi.com/medinfi/doctor-search/nagpur/doc_/%d?lat=21.130047&lng=79.079376" % k for k in xrange(5)
	#"http://www.medinfi.com/medinfi/doctor-search/thiruvananthapuram/doc_/%d?lat=8.511871&lng=76.925537" % k for k in xrange(5)
	#"http://www.medinfi.com/medinfi/doctor-search/coimbatore/doc_/%d?lat=11.021102&lng=76.966820" % k for k in xrange(5)
	#"http://www.medinfi.com/medinfi/doctor-search/surat/doc_/%d?lat=21.228922&lng=72.830322" % k for k in xrange(5)
	#"http://www.medinfi.com/medinfi/doctor-search/chennai/doc_/%d?lat=12.975971&lng=80.221207" % k for k in xrange(5)
	#"http://www.medinfi.com/medinfi/doctor-search/ludhiana/doc_/%d?lat=30.915318&lng=75.834633" % k for k in xrange(5)
	#"http://www.medinfi.com/medinfi/doctor-search/mysuru/doc_/%d?lat=12.325780&lng=76.629440" % k for k in xrange(5)
	#"http://www.medinfi.com/medinfi/doctor-search/vadodara/doc_/%d?lat=22.295252&lng=73.170822" % k for k in xrange(5)
	
	
    ]

    custom_settings = {
    'ROBOTSTXT_OBEY' : False,
    }

    def parse(self, response):
	#for sel in response.xpath('//div[@class="resDetailsDiv"]'):
	address = response.xpath("//div[@class='docInfoDiv']/span//text()").extract()
	name = response.xpath('//div[@class="docInfoDiv"]/div/h2//text()').extract()
	speciality = response.xpath('//div[@class="docInfoDiv"]/div/div//span[2]/text()').extract()
	#print selnew
	item = NewprojectItem()
	count = 0
	
	for add in address :
		print add
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
	#yield item
		
		
			#yield item
		#yield item
		
		#new4 = [item.replace('','') for item in new3]
		#newdata = newdata.replace('\t','')
		#newdata = newdata.replace('\n','')
		#print item['name']
		#item['name'] = 
		#for new in sel.xpath('//div[@class="docInfoDiv"]/span/text()'):
			#item['address'] = new.extract()
			
        	#item['address'] = yield{ "name":sel.xpath('//div[@class="docInfoDiv"]/span/text()').extract()}
        	#item['name'] = yield {"address":sel.xpath('//div[@class="docInfoDiv"]/div/h2//text()').extract()}
        	#item['speciality'] = yield {"speciality":sel.xpath('//div[@class="docInfoDiv"]/div/div/span//text()').extract()}
	
        		
		#for new2 in sel.xpath('//div[@class="docInfoDiv"]/div/h2//text()'):
			#item['name'] = new2.extract()
			
		#for new3 in sel.xpath('//div[@class="docInfoDiv"]/div/div/span//text()'):
			#item['speciality'] = new3.extract()
	
	
		
