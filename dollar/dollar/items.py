# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from w3lib.html import remove_tags
from itemloaders.processors import MapCompose, TakeFirst


class DollarItem(scrapy.Item):
     start = scrapy.Field(input_processor=MapCompose(remove_tags, int), output_processor=TakeFirst)
     min_ = scrapy.Field(input_processor=MapCompose(remove_tags, int), output_processor=TakeFirst)
     max_ = scrapy.Field(input_processor=MapCompose(remove_tags, int), output_processor=TakeFirst)
     end  = scrapy.Field(input_processor=MapCompose(remove_tags, int), output_processor=TakeFirst)
     change = scrapy.Field(input_processor=MapCompose(remove_tags, int), output_processor=TakeFirst)
     pct_change = scrapy.Field(input_processor=MapCompose(remove_tags, int), output_processor=TakeFirst)
     date = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst)
     date1 = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst)
