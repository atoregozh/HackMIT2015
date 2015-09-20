from amazonproduct import API

api = API(locale='us')
items = api.item_search('leisure women summer vacation girls')

# get all books from result set and
# print author and title
for item in items:
    print 'Title: "%s"' % (item.ItemAttributes.Title)
# import keys
# from amazon.api import AmazonAPI

# AMAZON_ACCESS_KEY = keys.AMAZON_ACCESS_KEY
# AMAZON_SECRET_KEY = keys.AMAZON_SECRET_KEY
# AMAZON_ASSOC_TAG = keys.AMAZON_ASSOC_TAG
# amazon = AmazonAPI(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOC_TAG)
# products = amazon.search(Keywords='kindle', SearchIndex='All')
# for i, product in enumerate(products):
# 	print "{0}. '{1}'".format(i, product.title)