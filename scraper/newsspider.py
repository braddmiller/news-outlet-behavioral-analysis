import scrapy
import json
from pprint import pprint

with open('site_list.json') as f:
		sites = json.load(f)
site_array = []
for site in sites:
	site_array.append(sites[site])

print site_array

class NewsSpider(scrapy.Spider):
	name = 'blogspider'
	start_urls = site_array

	def parse(self, response):
		for url in response.css('ul li a::attr("href")').re('.*/category/.*'):
			yield scrapy.Request(response.urljoin(url), self.parse_titles)

	def parse_titles(self, response):
		for post_title in response.css('div.entries > ul > li a::text').extract():
			yield {'title': post_title}