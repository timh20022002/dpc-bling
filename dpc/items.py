# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class awardItem(Item):
    awardID = Field() 
    awarderUserID = Field() 
    awardedUserID = Field()
    awardedImageID = Field() 
    challengeID = Field()
    thumbURL = Field() 
    imageURL = Field()
    awardName = Field()
    awardImageURL = Field() 

    def setChallengeID(self,id):
        self.challengeID = id; 