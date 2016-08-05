import scrapy

class GuardianCrawler(scrapy.Spider):
    name = 'guardian'
    start_urls = ['https://www.theguardian.com/au']
    allowed_domains = ["theguardian.com"]

    def parse(self, response):
        for url in response.css('a[data-link-name="article"]::attr(href)'):
            #print url.extract()
            #print '\n\n'
            #full_url = response.urljoin(url.extract())
            yield scrapy.Request(url.extract(), self.parse_article)
    
    def parse_article(self, response):
        yield {
            'title': response.css('h1.content__headline::text').extract_first()
        }



