# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class MangascraperPipeline(object):
#     def process_item(self, item, spider):
#         return item

import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem

class MyImagesPipeline(ImagesPipeline):
#     def get_media_requests(self, item, info):
#         for img_url in item['image_urls']:
# #            meta = {'filename': item['image_name']}
#             meta = {'item':item}
#             yield scrapy.Request(url=img_url, meta=meta)

    # def file_path(self, request, response=None, info=None):
    #     return scrapy.Request.meta.get('filename','')
    #
    # def get_media_requests(self, item, info):
    #     return [scrapy.Request(url, meta={'filename':item.get('image_name')}) for url in item.get(self.images_urls_field, [])]

    # def file_path(self, request, response=None, info=None):
    #     print "\n"*2
    #     print scrapy.Request.meta.get(item['image_names'])
    #     return scrapy.Request.meta.get(item['image_names'])
    #     print "\n"*2

    def file_path(self, request, response=None, info=None):
        image_guid = scrapy.Request.item.get('image_names')
        print "\n"*2 + image_guid + "\n"*2
        return 'full/%s.jpg' % (image_guid)

    def get_media_requests(self, item, info):
        for img_url in item['image_urls']:
            # img_url = item['image_urls']
            meta = {'filename': item['image_names']}
            yield scrapy.Request(url=img_url, meta=meta)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['images'] = image_paths # item['image_paths'] = image_paths
        return item
