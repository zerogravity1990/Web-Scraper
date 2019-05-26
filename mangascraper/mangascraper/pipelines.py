# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.project import get_project_settings
import os

class MyImagesPipeline(ImagesPipeline):

    IMAGES_STORE = get_project_settings().get("IMAGES_STORE")

    def item_completed(self, result, item, info):
        image_path = [x["path"] for ok, x in result if ok]
        os.rename(self.IMAGES_STORE + "/" + image_path[0], self.IMAGES_STORE + "/full/" + item["image_names"][0] + ".jpg")
        return item

# TODO: try to override file_path instead of os.rename
