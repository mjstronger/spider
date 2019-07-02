import scrapy
from meizhi.items import MeizhiItem

class MeizhiSpider(scrapy.Spider):
    page_link = set()
    name = 'meizhip'
    allowed_domains = ['www.mmonly.cc']
    start_urls = ['http://www.mmonly.cc/ktmh/']

    def parse(self, response):
        item = MeizhiItem()
        item['imgurl'] = response.xpath('//div[@class="ABox"]/a/img/@src').extract()
        item['imgname'] = response.xpath('//div[@class="ABox"]/a/img/@alt').extract()
        item['wjjname'] = response.url
        number = response.xpath('//div[@id="pageNum"]/a/@href').extract()
        for i in range(0, len(number)):

            next_pages = number[i]
            if next_pages:
                next_page = "http://www.mmonly.cc/ktmh/" + next_pages
                self.page_link.add(next_page)
                yield scrapy.Request(next_page,callback=self.parse)
        yield item
        pass
