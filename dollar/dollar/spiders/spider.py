import scrapy
from ..items import DollarItem
from scrapy.selector import Selector
from selenium import webdriver


class SpiderSpider(scrapy.Spider):
    name = "spider"
    allowed_domains = ["www.tgju.org"]
    start_urls = ["https://www.tgju.org/profile/price_dollar_rl/history"]

    def parse(self, response):
        items = DollarItem()
        sel = Selector()
        table_body = sel.xpath('//tbody[@id="table-list"]')
        for row in table_body.xpath('.//tr'):
            items['start'] = row.xpath('td[1]/text()').get()
            items['min_'] = row.xpath('td[2]/text()').get()
            items['max_'] = row.xpath('td[3]/text()').get()
            items['end'] = row.xpath('td[4]/text()').get()
            items['change'] = row.xpath('td[5]/span/text()').get()
            items['pct_change'] = row.xpath('td[6]/span/text()').get()
            items['date'] = row.xpath('td[7]/text()').get()
            items['date1'] = row.xpath('td[8]/text()').get()
            yield items
        next_page = response.css("#DataTables_Table_0_next").get()
        if next_page is not None:
            response.follow(next_page, callback=self.parse)
