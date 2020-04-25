# -*- coding: utf-8 -*- 
from scrapy.spiders import CrawlSpider, Rule,Spider
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import HtmlXPathSelector,Selector
from dirbot.items import Hh



'''class googlepag(CrawlSpider):
    name="google"
    allowed_domains = ["google.com"]
    start_urls=["http://www.google.ru/search?q=gabber"]
    rules= (
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//div[@id="foot"]',)), callback="parse_items", follow= True),
    )

    def parse(self,response):

        hxs=Selector(response)
        items = hxs.css('#ires')

        for item in items:
            item = Google()
            item["site"] = items.css('.g a[href]').extract()'''

class Headhunter(Spider):
    name="hh"
    allowed_domains = ["murmansk.hh.ru"]
    npage=16202417 # 1/10
    global number
    number=1
    n=14920000#16202417
    i=0
    start_urls=[]
    
    while(npage>n):
        url= "https://spb.hh.ru/vacancy/" + str(n)
        start_urls.append(url)
        n+=1

    i=0

    def parse(self, response):
        sel = HtmlXPathSelector(response)
        #sel = Selector(response)
       # sites = sel.xpath("//div[@class='g-row m-row_content HH-Sticky-AreaOnContent-Wrapper']")
        #links=[]
       
        items = []
        #i=0
        #f=open('hh.txt','w')
        #f.write(str(sites.extract()))        
        item = Hh()
        item['url']=sel.xpath('//span[@class="share-buttons__button share-buttons__button_twitter"]/a/@data-url').extract()
        item['vacancy'] = sel.xpath('//h1[@class="title b-vacancy-title"]').extract() #//h1[@class="title b-vacancy-title"]/').extract()#site.xpath('a/@href').extract()
        item['employer'] = sel.xpath('//div[@class="b-vacancy-companylogo"]//img/@alt').extract()
        sal=sel.xpath('//td[@class="l-content-colum-1 b-v-info-content"]//meta/@content').extract()
        item['salary'] = sal[1]#.xpath('//h1[@class="title b-vacancy-title"]').extract()
        item['description'] = sel.xpath('//div[@class="b-vacancy-desc-wrapper"]').extract()
        item['prof_obl'] = sel.xpath('//li[@class="vacancy-profareas__item"]/a/@href').extract_first()
        item['city'] = sel.xpath('//td[@class="l-content-colum-2 b-v-info-content"]/div[@class="l-paddings"]').extract()         
        items.append(item)
        #employer= Field()    
        #salary= Field() //div[contains(@class, 'Test')]
        #description= Field()
        #prof_obl= Field()
        #city=Field()
        #self.f.write(str(items[n].extract()))
        #self.f.write(str('\n'))
        return (items)
   # f=open('fuckscrapydevelopers.txt','w')

    '''def parse(self,response):

        hxs=Selector(response)
        sites = hxs.xpath("//div[@id='ires']/ol/li/h3[@class='r']")
        items = []

        for site in sites:
            item = Google()

            item["site"] = site.xpath("//li[@class='g']/h3/a/@hre").extract()
            items.append(item)
            # if(self.i>6):
            self.f.write(str(sites.extract()))


        return items'''



