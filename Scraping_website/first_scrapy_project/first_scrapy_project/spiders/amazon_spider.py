import scrapy
from ..items import FirstScrapyProjectItem

class AmazonSpiderSpider(scrapy.Spider):
    name = 'myntra'
    start_urls = [
        'https://www.myntra.com/books'
    ]

    def parse(self, response):
        items =  FirstScrapyProjectItem()

        product_name = response.css('.product-discountedPrice::text').extract()
        # product_rating = response.css('._3LWZlK').css('::text').extract()
        # product_price = response.css('._30jeq3').css('::text').extract()
        # product_image_link = response.css('._3exPp9::attr(src)').extract()

        items['product_name'] = product_name
        # items['product_rating'] = product_rating
        # items[' product_price'] =  product_price
        # items['product_image_link'] = product_image_link

        yield items
