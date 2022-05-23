import scrapy
from ..items import AmazonReviewsItem


class AmazonSandisk32gbSpider(scrapy.Spider):
    name = 'amazon_sandisk_32gb'
    allowed_domains = ['amazon.com','www.amazon.in']
    page_number = 2
    start_urls = [
        'https://www.amazon.in/SanDisk-Cruzer-Blade-Flash-Drive/product-reviews/B005FYNT3G/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'
    ]

    def parse(self, response):
        data = AmazonReviewsItem()

        customer_name = response.css('.a-profile-name::text').extract()
        review_date = response.css('.review-date::text').extract()
        review = response.css('.review-text-content span::text').extract()


        data['customer_name'] = customer_name
        data['review_date'] = review_date
        data['review'] = review

        yield data

        next_page = ('https://www.amazon.in/SanDisk-Cruzer-Blade-Flash-Drive/product-reviews/B005FYNT3G/ref=cm_cr_arp_d_paging_btm_next_'+str(AmazonSandisk32gbSpider.page_number)+'?ie=UTF8&reviewerType=all_reviews&pageNumber='+str(AmazonSandisk32gbSpider.page_number)+'')

        if AmazonSandisk32gbSpider.page_number <= 500:
            AmazonSandisk32gbSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)


