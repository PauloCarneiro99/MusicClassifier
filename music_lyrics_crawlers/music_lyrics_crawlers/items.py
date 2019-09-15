# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LyricsItem(scrapy.Item):
    style = scrapy.Field()

    lyrics = scrapy.Field()

    title = scrapy.Field()
    author = scrapy.Field()

    data = scrapy.Field()
