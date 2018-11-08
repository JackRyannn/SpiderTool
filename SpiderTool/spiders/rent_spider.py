import scrapy
from SpiderTool.items import SpidertoolItem2


class mt_spider(scrapy.Spider):
    name = "rent"
    start_urls = [
        "https://www.douban.com/group/zhufang/",
        "https://www.douban.com/group/279962/",
   	"https://www.douban.com/group/opking/",
	"https://www.douban.com/group/625354/",
	"https://www.douban.com/group/465554/",
    	"https://www.douban.com/group/beijingzufang/",
    ]
    custom_settings = {
        'ITEM_PIPELINES': {'SpiderTool.pipelines.SpidertoolPipeline2': 300},
    }
    def parse(self, response):
        keywords = ["车公庄","阜成门","西直门","慈寿寺","海淀五路居","花园桥","白石桥南"]
        avoid = ["求租","妹子","女生","只限"]

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

