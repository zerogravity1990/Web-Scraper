# -*- coding: utf-8 -*-
import scrapy


class ImmortaleSpider(scrapy.Spider):
    name = 'immortale'
    allowed_domains = ['www.mangaeden.com']
    start_urls = ['http://https://www.mangaeden.com/en/it-manga/limmortale/0/1/']

    def parse(self, response):
        pass
