# Scrapy settings for electronics project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'dpc'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['dpc.spiders']
NEWSPIDER_MODULE = 'dpc.spiders'
DEFAULT_ITEM_CLASS = 'dpc.awards.dpcAwards'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

FEED_URI = 'electronics__%(name)s__%(time)s.csv'
FEED_FORMAT = 'csv'