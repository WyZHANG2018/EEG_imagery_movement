import scrapy
import requests

class edfSpider(scrapy.Spider):
    name = "edfSpider"

    def start_requests(self):
        
        url='https://physionet.org/pn4/eegmmidb/'

        yield scrapy.Request(url=url, callback=self.parse)
        
    def parse(self, response):
        subject_list=response.css('html body main article#page pre a::attr(href)').extract()
        i=0
        for url in subject_list :
            i+=1
            if i>=12&i<=120:
                print url
                yield response.follow(url=url, callback=self.parse_each)
     
   
    def parse_each(self,response):
        edf_list=response.css('html body pre a::attr(href)').extract()
        i=0
        for url in edf_list:
            i+=1
            if ((i>=6)&(i%2==0)):
                url_absolute = response.urljoin(url) 
                r = requests.get(url_absolute, allow_redirects=True)
                open(url, 'wb').write(r.content) 
       


   
        


