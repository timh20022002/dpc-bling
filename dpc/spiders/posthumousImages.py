'''
Created on 19 Nov 2011

@author: niallotuama
'''


 
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector

from dpc import settings
from dpc.items import awardItem

from re import search
from math import ceil
import md5

def genmd5(s):
    m = md5.new(); 
    m.update( s ); 
    return m.hexdigest()
    
class awardSpider(CrawlSpider):
    name = 'dpcAwards_comments'
    allowed_domains = ['dpchallenge.com']
    
    awards = {
        # posthumous' bling
        '50695': {
          'awarder': 'posthumous',
          'awards' : [
              ['http://blackyak.com/dpc/bluepost.jpg', 'blue',  genmd5('50695'+'1')],
              ['http://blackyak.com/dpc/redpost.jpg', 'red', genmd5('50695'+'2')],
              ['http://blackyak.com/dpc/yellowpost.jpg', 'yellow', genmd5('50695'+'3')],
              ['http://blackyak.com/dpc/artpost.jpg', 'gallery', genmd5('50695'+'4')],
              ['http://blackyak.com/dpc/blurpost.jpg', 'blur', genmd5('50695'+'5')],
              ['http://images.dpchallenge.com/images_portfolio/60000-64999/60915/120/746233.jpg', 'master', genmd5('50695'+'6')],
          ]
        },
        
        # xianart's bling
        '53572': {
          'awarder': 'xianart',
          'awards' : [
              ['http://images.dpchallenge.com/images_portfolio/50000-54999/53572/120/Copyrighted_Image_Reuse_Prohibited_657241.jpg', 'blue', genmd5('53572'+'1')],
              ['http://images.dpchallenge.com/images_portfolio/50000-54999/53572/120/Copyrighted_Image_Reuse_Prohibited_657242.jpg', 'red', genmd5('53572'+'2')],
              ['http://images.dpchallenge.com/images_portfolio/50000-54999/53572/120/Copyrighted_Image_Reuse_Prohibited_657243.jpg', 'yellow', genmd5('53572'+'3')],
          ]
        },
        
        # vlado's bling
        '32011': {
          'awarder': 'vlado',
          'awards' : [
             ['http://images.dpchallenge.com/images_portfolio/30000-34999/32011/800/Copyrighted_Image_Reuse_Prohibited_858386.png', 'MUPIMHO', genmd5('32011'+'1')],
          ]
        },
        
        # Yo_Spiff's bling
        '83313': {
          'awarder': 'Yo_Spiff',
          'awards' : [
              ['http://images.dpchallenge.com/images_portfolio/80000-84999/83313/120/Copyrighted_Image_Reuse_Prohibited_737193.jpg', 'shoehorn blue', genmd5('32011'+'1')],
              ['http://images.dpchallenge.com/images_portfolio/80000-84999/83313/120/Copyrighted_Image_Reuse_Prohibited_737192.jpg', 'shoehorn red', genmd5('32011'+'2')],
              ['http://images.dpchallenge.com/images_portfolio/80000-84999/83313/120/Copyrighted_Image_Reuse_Prohibited_737194.jpg', 'shoehorn yellos', genmd5('32011'+'3')],
          ]
        },
        
        # blindjustice's bling
        '12611': {
          'awarder': 'blindjustice',
          'awards' : [
             ['http://images.dpchallenge.com/images_portfolio/10000-14999/12611/120/Copyrighted_Image_Reuse_Prohibited_984308.jpg', 'paully', genmd5('12611'+'1')],
          ]
        },
        
        # Greetmir's bling
        '70828': {
          'awarder': 'Greetmir',
          'awards' : [
             ['http://images.dpchallenge.com/images_portfolio/70000-74999/70828/120/503169.gif', 'OOBie', genmd5('70828'+'1')],
          ]
        },
        
        # Kali's bling
        '9462': {
          'awarder': 'Kali',
          'awards' : [
              ['http://images.dpchallenge.com/images_portfolio/5000-9999/9462/120/Copyrighted_Image_Reuse_Prohibited_670650.jpg', 'blue', genmd5('9462'+'1')],
              ['http://images.dpchallenge.com/images_portfolio/5000-9999/9462/120/Copyrighted_Image_Reuse_Prohibited_670651.jpg', 'red', genmd5('9462'+'2')],
              ['http://images.dpchallenge.com/images_portfolio/5000-9999/9462/120/Copyrighted_Image_Reuse_Prohibited_670652.jpg', 'yellow', genmd5('9462'+'3')],
          ]
        },
        
        # undieyatch's bling
        '3724': {
          'awarder': 'undieyatch',
          'awards' : [
            ['http://lh5.ggpht.com/_N9z0wRqDr5U/SWK1fmqYr6I/AAAAAAAAAEg/uCu7yJVBKs8/50x50_inver-b.jpg', 'pictogram', genmd5('3724'+'1')],
          ]
        },
        
        # Bear_Music's bling
        '30861': {
          'awarder': 'Bear_Music',
          'awards' : [
              ['http://images.dpchallenge.com/images_portfolio/30000-34999/30861/120/Copyrighted_Image_Reuse_Prohibited_762723.jpg', 'golden paw', genmd5('30861'+'1')],
              ['http://images.dpchallenge.com/images_portfolio/30000-34999/30861/120/Copyrighted_Image_Reuse_Prohibited_762724.jpg', 'silver paw', genmd5('30861'+'2')],
              ['http://images.dpchallenge.com/images_portfolio/30000-34999/30861/120/Copyrighted_Image_Reuse_Prohibited_762725.jpg', 'bronze paw', genmd5('30861'+'3')],
          ] 
        },
        
        # ubique's bling
        '30364': {
          'awarder': 'ubique',
          'awards' : [
              ['http://images.dpchallenge.com/images_portfolio/30000-34999/30861/120/Copyrighted_Image_Reuse_Prohibited_827763.jpg', 'print', genmd5('30364'+'1')],
              ['http://images.dpchallenge.com/images_challenge/0-999/354/120/Copyrighted_Image_Reuse_Prohibited_197649.jpg', '        print big', genmd5('30364'+'2')],
              ['http://images.dpchallenge.com/images_portfolio/30000-34999/30364/120/Copyrighted_Image_Reuse_Prohibited_800078.jpg', 'print small', genmd5('30364'+'3')],
          ]
        },
              
        # vawendy's bling
        '103142': {
          'awarder': 'vawendy',
          'awards' : [
            ['http://images.dpchallenge.com/images_portfolio/100000-104999/103142/120/Copyrighted_Image_Reuse_Prohibited_811107.jpg', 'bluebird of happiness', genmd5('103142'+'1')],
          ]
        },
        
        # paulbltw's bling
        '100393': {
          'awarder': 'paulbtlw',
          'awards' : [
             ['http://images.dpchallenge.com/images_portfolio/100000-104999/100393/120/Copyrighted_Image_Reuse_Prohibited_859062.jpg', 'unconventional eye', genmd5('100393'+'1')],
          ]
        },
        
        # bspurgeon's bling
        '54645': {
          'awarder': 'bspurgeon',
          'awards' : [
             ['http://images.dpchallenge.com/images_portfolio/50000-54999/54645/120/Copyrighted_Image_Reuse_Prohibited_963227.jpg', 'silver sturgeon ', genmd5('54645'+'1')],
          ]
        },
        
        # Yanko's bling
        '41337': {
          'awarder': 'yanko',
          'awards' : [
              ['http://images.dpchallenge.com/images_portfolio/40000-44999/41337/120/Copyrighted_Image_Reuse_Prohibited_657188.gif', 'blue', genmd5('41337'+'1')],
              ['http://images.dpchallenge.com/images_portfolio/40000-44999/41337/120/Copyrighted_Image_Reuse_Prohibited_657189.gif', 'red', genmd5('41337'+'2')],
              ['http://images.dpchallenge.com/images_portfolio/40000-44999/41337/120/Copyrighted_Image_Reuse_Prohibited_657190.gif', 'yellow', genmd5('41337'+'3')],
              ['http://images.dpchallenge.com/images_portfolio/40000-44999/41337/120/Copyrighted_Image_Reuse_Prohibited_657191.gif', 'green', genmd5('41337'+'4')],
          ]
        },
        
        # chromeydome's bling
        '82985': {
          'awarder': 'chromeydome',
          'awards' : [
              ['http://images.dpchallenge.com/images_portfolio/80000-84999/82985/120/Copyrighted_Image_Reuse_Prohibited_677021.jpg', 'Post Lumy Award', genmd5('82985'+'1')],
              ['http://images.dpchallenge.com/images_portfolio/80000-84999/82985/120/Copyrighted_Image_Reuse_Prohibited_677020.jpg', 'Post Lumy Award', genmd5('82985'+'2')],
              ['http://images.dpchallenge.com/images_portfolio/80000-84999/82985/120/Copyrighted_Image_Reuse_Prohibited_747600.jpg', 'Post Lumy Award', genmd5('82985'+'3')],
          ]
        },
        
        # timfythetoo's bling
        '53147': {
          'awarder': 'timfythetoo',
          'awards' : [
              ['http://images.dpchallenge.com/images_portfolio/50000-54999/53147/800/Copyrighted_Image_Reuse_Prohibited_649858.jpg', 'blue', genmd5('53147'+'1')],
              ['http://images.dpchallenge.com/images_portfolio/50000-54999/53147/800/Copyrighted_Image_Reuse_Prohibited_649859.jpg', 'red', genmd5('53147'+'2')],
              ['http://images.dpchallenge.com/images_portfolio/50000-54999/53147/800/Copyrighted_Image_Reuse_Prohibited_649860.jpg', 'yellow', genmd5('53147'+'3')],
          ]
        },
              
        # Dr. Confuser's bling
        '18197': {
          'awarder': 'Dr. Confuser',
          'awards' : [
             ['http://images.dpchallenge.com/images_portfolio/15000-19999/18197/120/Copyrighted_Image_Reuse_Prohibited_896464.gif', 'Purple Prose Winner', genmd5('18197'+'1')],
          ]
        },
    }
    
    
    
    
    # There's a convenient start page that lists all the categories
    start_urls = []; 
    commentsStub = "http://www.dpchallenge.com/comment_browse.php?TYPE=made&PP=50&ORDER=desc&HELPFUL=all&USER_ID="
    for awarderID in awards:
        start_urls.append( commentsStub + str(awarderID) )
        break
    #start_urls = ['http://www.dpchallenge.com/comment_browse.php?TYPE=made&PP=50&ORDER=desc&HELPFUL=all&USER_ID=30861']
    
    
    # Rule 1: Defines how we traverse the comments pages
    rule1 = SgmlLinkExtractor( 
        restrict_xpaths = (
            '//img[@src="/images/page/next.gif"]/..',
            '//img[@src="/images/page/1.gif"]/..'
        ),
    )
    
    # The rules array
    rules = (
        Rule( rule1, callback = 'parseComments', follow = True ),
    )
    
    
    
    
    
    def parseComments(self, request):
        hxs = HtmlXPathSelector(request)
        print "Parsing: ", request.url
        
        # Get the ID of the awarder from the request URL
        awarderUserID = search( r'USER_ID=(\d+)', request.url )
        if not awarderUserID:
            print "Unable to parse awarder id from: ", request.url
            return
        awarderUserID = awarderUserID.group(1)

        # Loop over the comments in this page
        comments = hxs.select( '//table//tr[contains(@class,"forum-bg")]' )
        
        for i in range(1,len(comments)):
            comment = comments[i]


            # This means an image is found in the comment
            imgSrc = comment.select('.//img/@src' )
            
            if imgSrc:
                imgSrc = imgSrc.extract()
                for img in imgSrc:
                    for award in self.awards[awarderUserID]['awards']:
                        blingStub = search( r'.*/(.*?)$', award[0] ).group(1)
                        blingSearch = search( blingStub, img )
                        
                        if blingSearch:
    
                            # AWARDED INFO
                            awarded = comment.select('.//a[contains(@href,"profile")]' )
                            awardedUserID = awarded.select( './/@href' ).extract()
                            awardedUserID = search( r'USER_ID=(\d+)', str(awardedUserID[0]) ).group(1)
                            awardedImageID = comment.select('.//a[contains(@href,"IMAGE_ID")]/@href' ).extract()
                            awardedImageID = search( r'IMAGE_ID=(\d+)', str(awardedImageID[0]) ).group(1)
                            
                            
                            # Presumably only one awarder will award anything
    
                            item = {}
                            item["awarderUserID"] = awarderUserID
                            item["awardID"] = award[2]
                            item["awardName"] = award[1]
                            item["awardedUserID"] = awardedUserID
                            item["awardedImageID"] = awardedImageID
                            item["awardImageURL"] = award[0]
                            
                            
                            # We don't have the date or challenge ID of this 
                            # item yet, so we must make a request to the image URL
                            print 'Requesting: back: http://www.dpchallenge.com/image.php?IMAGE_ID=' + awardedImageID
                            request = Request( 
                                url      = 'http://www.dpchallenge.com/image.php?IMAGE_ID=' + awardedImageID, 
                                callback = self.appendItem
                            )
                            request.meta['item'] = item
                            yield request 
                            
        
        
        
    
    def appendItem( self, request ): 
        print "Accepting: ", request.url
        
        hxs = HtmlXPathSelector(request)
        
        item = request.meta["item"]
        challenge = hxs.select( '//a[contains(@href,"challenge_results.php")]' )[0]
        challengeID = search( r'(\d+)', str(challenge.select( '@href' ).extract()) ).group(1)
        print challengeID
        
        imageStub = "http://images.dpchallenge.com/images_challenge/1000-1999/"
        if int(challengeID) < 1000:
            imageStub = "http://images.dpchallenge.com/images_challenge/0-999/"
        thumbURL = imageStub + str(challengeID) + "/120/Copyrighted_Image_Reuse_Prohibited_" + item["awardedImageID"] + ".jpg";
        imageURL = imageStub + str(challengeID) + "/800/Copyrighted_Image_Reuse_Prohibited_" + item["awardedImageID"] + ".jpg";

        # Generate item to return
        i = awardItem (
            awardID         = item["awardID"],
            awarderUserID   = item["awarderUserID"],
            awardedUserID   = item["awardedUserID"],
            awardedImageID  = item["awardedImageID"],
            challengeID     = challengeID,
            thumbURL        = thumbURL,
            imageURL        = imageURL,
            awardName       = item["awardName"],
            awardImageURL   = item["awardImageURL"]
        )
        
        return i
    
        
        
    
SPIDER = awardSpider()

