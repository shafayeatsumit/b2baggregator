import scrapy

from tutorial.items import DmozItem

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["http://bikroy.com/en"]
    start_urls = [
        'http://bikroy.com/en/ads/mobile-phones-in-bangladesh-230?page=%s'% page for page in xrange(1,5)
    ]

    def parse(self, response):
        for sel in response.xpath('/html/body/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[1]/div[1]/div'):
            item = DmozItem()
            item['title'] = str(sel.xpath('div[2]/a/text()').extract()[0])
            item['location']=str(sel.xpath('div[2]/p[1]/span[3]/text()').extract()[0])
            item['posting_time']=str(sel.xpath('div[2]/p[1]/span[1]/text()').extract()[0])
            item['category']=str(sel.xpath('div[2]/p[1]/span[5]/text()').extract()[0])
            item['price']=str(sel.xpath('div[2]/p[2]/strong/text()').extract()[0])
            item['link']="http://bikroy.com"+str(sel.xpath('div[2]/a/@href').extract()[0])
            
            yield item
