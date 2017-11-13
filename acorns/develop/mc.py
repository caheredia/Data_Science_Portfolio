import scrapy
class macySpider(scrapy.Spider):
	name = 'macybot'
	allowed_domains = ['https://www.macys.com/shop/mens-clothing/mens-activewear?id=3296&edge=hybrid']
	start_urls = ['https://www.macys.com/shop/mens-clothing/mens-activewear?id=3296&edge=hybrid']

	def parse(self, response):
		#Extracting the content using css selectors
		titles = response.css(".productDescLink::attr(title)").extract()
		url = response.css(".productDescLink::attr(href)").extract()

		#Give the extracted content row wise
		for item in zip(titles,url):
			#create a dictionary to store the scraped info
			scraped_info = {
			'title' : item[0],
			'url' : item[1],
			}

			#yield or give the scraped info to scrapy
			yield scraped_info
