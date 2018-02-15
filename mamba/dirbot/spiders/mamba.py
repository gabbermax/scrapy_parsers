from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.http.request import Request
from dirbot.items import Mamba


class DmozSpider(Spider):
    name = "mamba"
    allowed_domains = ["m.mamba.ru"]
    npage=10#598605
    n=0
    i=0
    start_urls=[]

    while(npage>n):
            
        url= "http://m.mamba.ru/?area=SearchResult&photoSize=normal&status=all&lookFor=N&location=0_0_0_0&fromAge=18&toAge=80&offset=" + str(n) + "&force_wap=1"
        #https://m.mamba.ru/?area=SearchResult&photoSize=normal&status=all&lookFor=N&location=0_0_0_0&fromAge=18&toAge=80&offset=6584666&force_wap=1   6584655
        start_urls.append(url)
        n+=11







    def parse(self, response):
        sel = Selector(response)
        sites = sel.css('td[class="txt-container"] strong')
        items = []

        for site in sites:
            '''item = Mamba()
            item["user"] = site.xpath("a/text()").extract()
            item["number"]=self.i
            items.append(item)
            self.i=self.i+1'''
            user_url= "http://m.mamba.ru"+str(site.xpath("a/@href").extract())
            Request(user_url,self.get_user_info)
        return items

    #need to proceed users page


    def get_user_info(self,response):
        item=Mamba()
        item['name']=sel.xpath("//span[@style='font-size:13px;']").extract();
        items.append(item)




