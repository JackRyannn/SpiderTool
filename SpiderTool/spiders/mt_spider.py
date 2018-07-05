import scrapy
from SpiderTool.items import SpidertoolItem


class mt_spider(scrapy.Spider):
    name = "mt"
    start_urls = [
        "https://movie.douban.com/cinema/nowplaying/beijing/"
    ]
    custom_settings = {
        'ITEM_PIPELINES': {'SpiderTool.pipelines.SpidertoolPipeline': 300},
    }

    def parse(self, response):
        for sel in response.xpath('//li[@data-score]'):
            item = SpidertoolItem()
            item['title'] = sel.xpath('@data-title').extract()
            item['score'] = sel.xpath('@data-score').extract()
            # 低于五分滚粗
            if(float(item['score'][0])<7.5):
                continue
            item['star'] = sel.xpath('@data-star').extract()
            item['release'] = sel.xpath('@data-release').extract()
            item['duration'] = sel.xpath('@data-duration').extract()
            item['director'] = sel.xpath('@data-director').extract()
            item['actors'] = sel.xpath('@data-actors').extract()
            item['region'] = sel.xpath('@data-region').extract()
            item['category'] = sel.xpath('@data-category').extract()
            item['enough'] = sel.xpath('@data-enough').extract()
            item['showed'] = sel.xpath('@data-showed').extract()
            item['votecount'] = sel.xpath('@data-votecount').extract()
            item['subject'] = sel.xpath('@data-subject').extract()
            item['pic'] = sel.xpath('ul/li/a/img/@src').extract()
            yield item

