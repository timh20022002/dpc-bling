'''
Created on 18 Nov 2011

@author: niallotuama
'''


 
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector

from dpc import settings
from dpc.awards import ElectronicsItem

from re import match
from math import ceil


class dabsSpider(CrawlSpider):
    name = 'dpc'
    
    
    allowed_domains = ['dpchallenge.com']
    
    # There's a convenient start page that lists all the categories
    start_urls = ['http://www.dpchallenge.com/challenge_archive.php']
    
    
    # Rules: Extract the categories and subcategories
    rule1 = SgmlLinkExtractor(
        allow = ( 'challenge_results.php' )
    )
    
    
    
    
    # The rules array
    rules = (
        Rule( rule1, callback='parseProducts', follow=True ), 
    )
    
    def parseProducts(self, request):
        hxs = HtmlXPathSelector(request)
        
        return
        
        
        
    
SPIDER = dabsSpider()

