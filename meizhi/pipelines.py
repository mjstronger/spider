# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import Request
import re
from scrapy.pipelines.images import ImagesPipeline

class MeizhiPipeline(ImagesPipeline):
    def get_media_requests(self,item,info):
        # for image_url in item['imgurl']:
        #     yield Request(image_url,meta={'name':item['imgname']})
        for i in range(0,len(item['imgurl'])):
            yield Request(item['imgurl'][i],meta={'imgname':item['imgname'][i],'wjjname':item['wjjname']})
    def file_path(self,request,response=None,info=None):

        # image_guid = request.url.split('/')[-1]
        image_guid = request.meta['imgname']
        wjjname = request.meta['wjjname']
        wjjname = re.sub(r'[?\\*|"<>:/]','',wjjname)
        filename = u'{0}/{1}.jpg'.format(wjjname,image_guid)
        return filename
