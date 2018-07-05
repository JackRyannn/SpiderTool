import scrapy
from SpiderTool.items import SpidertoolItem2


class mt_spider(scrapy.Spider):
    name = "rent"
    start_urls = [
        "https://www.douban.com/group/zhufang/",
        "https://www.douban.com/group/279962/"
    ]
    custom_settings = {
        'ITEM_PIPELINES': {'SpiderTool.pipelines.SpidertoolPipeline2': 300},
    }
    def parse(self, response):
        keywords = ["望京","花家地","将台"]
        avoid = ["求租"]

        for sel in response.xpath('//td[@class="title"]/a[@title]'):
            flag = False
            item = SpidertoolItem2()


            item['title'] = sel.xpath('@title').extract()
            item['url'] = sel.xpath('@href').extract()

            #包含关键词
            for key in keywords:
                if str(item['title']).find(key)>=0:
                    flag = True
                    for j in avoid:
                        if str(item['title']).find(j) >= 0:
                            flag = False
                    break
            if not flag:
                continue
            yield item

