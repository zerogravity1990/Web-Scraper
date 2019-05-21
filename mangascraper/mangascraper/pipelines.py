# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MangascraperPipeline(object):
    def process_item(self, item, spider):
        return item


class MyImagesPipeline(ImagesPipeline):
#     def get_media_requests(self, item, info):
#         for img_url in item['image_urls']:
# #            meta = {'filename': item['image_name']}
#             meta = {'item':item}
#             yield scrapy.Request(url=img_url, meta=meta)

    def file_path(self, request, response=None, info=None):
        return scrapy.Request.meta.get('filename','')

    def get_media_requests(self, item, info):
        return [scrapy.Request(url, meta={'filename':item.get('image_name')}) for url in item.get(self.images_urls_field, [])]
