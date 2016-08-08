import scrapy

from guardian.items import ArticleItem
from readability import Document
from utils import strip_tags
import datetime


class GuardianCrawler(scrapy.Spider):
    name = 'guardian'
    start_urls = ['https://www.theguardian.com/au']
    allowed_domains = ["theguardian.com"]

    def parse(self, response):
        for url in response.css('a[data-link-name="article"]::attr(href)'):
            #full_url = response.urljoin(url.extract())
            yield scrapy.Request(url.extract(), self.parse_article)
        
        for url in response.css('.top-navigation__action::attr(href)'):
            yield scrapy.Request(url.extract(), self.parse_section)


    def parse_section(self, response):
        for url in response.css('a[data-link-name="article"]::attr(href)'):
            #full_url = response.urljoin(url.extract())
            yield scrapy.Request(url.extract(), self.parse_article)
    
    def parse_article(self, response):
        article = ArticleItem()
        article['headline'] = response.css('h1.content__headline::text').extract_first().strip()
        if article['headline'] == None:
            article['headline'] = response.xpath('//*[@id="article"]/header/div[1]/div/div/h1/text()').extract_first().strip()
        if article['headline'] == None:
            article['headline'] = response.xpath('//*[@id="article"]/header/div[1]/div/div/h1/span/text()').extract_first().strip()
        article['imageUrl'] = response.xpath('//*[@id="img-1"]/a/div/picture/img/@src').extract_first()
        article['url']      = response.url
        article['author']   = response.xpath('//*[@id="article"]/div[2]/div/div[1]/div[2]/p[1]/span[1]/a/span/text()').extract_first()
        if article['author'] == None:
            article['author'] = response.xpath('//*[@id="article"]/header/div[1]/div/div/span/span/a/span/text()').extract_first()
        if article['author'] == None:
            article['author'] = response.xpath('//*[@id="article"]/div[2]/div/div[1]/div[2]/p[1]/text()').extract_first()
        if article['author'] == None:
            article['author'] = response.xpath('//*[@id="article"]/div/div/div[1]/div/div[2]/div[2]/p[1]/span/a/span/text()').extract_first()
        if article['author'] == None:
            article['author'] = response.xpath('//*[@id="article"]/div[2]/div/div[1]/div[2]/div/p[1]/span/a/span/text()').extract_first()



        article['cacheDateTime']= datetime.datetime.now()

        
        article['text'] = response.css('body').extract_first()
        #doc = Document(body)
        #article['text'] = strip_tags(doc.summary())

        yield article
        



