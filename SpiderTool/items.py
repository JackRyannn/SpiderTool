# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpidertoolItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field();
    score = scrapy.Field();
    star = scrapy.Field();
    release = scrapy.Field();
    duration = scrapy.Field();
    director = scrapy.Field();
    actors = scrapy.Field();
    region = scrapy.Field();
    category = scrapy.Field();
    enough = scrapy.Field();
    showed = scrapy.Field();
    votecount = scrapy.Field();
    subject = scrapy.Field();
    pic = scrapy.Field();
    pass

class SpidertoolItem2(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field();
    url = scrapy.Field();
    pass