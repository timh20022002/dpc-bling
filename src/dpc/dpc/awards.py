# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class dpcAwards(Item):
    # define the fields for your item here like:
    retailer = Field()
    name = Field()
    url = Field()
    brand = Field()
    image = Field()
    section = Field()
    category = Field()
    subcategory = Field()
    price = Field()
    
    # Debug Fields
    error = Field()
    stage = Field()
