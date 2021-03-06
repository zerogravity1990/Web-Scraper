# -*- coding: utf-8 -*-
import scrapy
from .. import items

class ImmortaleSpider(scrapy.Spider):
    name = 'immortale'
    allowed_domains = ['www.mangaeden.com']
    start_urls = ['https://www.mangaeden.com/en/it-manga/limmortale/0/1/']


    def parse(self, response):
        item = items.MangascraperItem()
        urls_list = []
        for url in response.xpath('//img[@id="mainImg"]/@src').extract():
            urls_list.append("https:" + url)
        item['image_urls'] = urls_list
        item['image_names'] = response.url.split("/")[-3] + "-" + response.url.split("/")[-2]   #result is like "chapter-page", "1-25"
        yield item

        next_page = response.xpath('//a[@class="ui-state-default next"]/@href').extract()
        if next_page:
            next_href = next_page[0]
            next_page_url = response.urljoin(next_href)
            request = scrapy.Request(url=next_page_url)
            yield request
