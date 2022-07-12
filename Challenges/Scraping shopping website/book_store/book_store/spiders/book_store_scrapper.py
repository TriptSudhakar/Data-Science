import scrapy

class Booksspider(scrapy.Spider):
    name = "bookscrapper"

    def start_requests(self):
        urls = [
            'http://books.toscrape.com/'
            ]
        
        for url in urls:
            # yield "image_url,book_title,product_price'\n'"
            yield scrapy.Request(url = url, callback=self.parse)

    def parse(self, response):
        for li in response.css('ol.row li'):
            image_url = li.css('article.product_pod div.image_container a img::attr(src)').get()
            book_title = li.css('article.product_pod h3 a::attr(title)').get()
            product_price = li.css('article.product_pod div.product_price p.price_color::text').get()
            # yield f"{image_url},{book_title},{product_price}'\n'"
            yield {
                "image_url": image_url,
                "book_title": book_title,
                "product_price": product_price
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback = self.parse)