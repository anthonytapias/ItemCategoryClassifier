import requests
from bs4 import BeautifulSoup
import re
# from listing import Listing


cat = ['EDUCATION', 'BUSINESS', 'DATING', 'SPORTS', 'WEATHER', 'FOOD_AND_DRINK', 'HEALTH_AND_FITNESS', 'BEAUTY', 'MUSIC_AND_AUDIO', 'NEWS_AND_MAGAZINES', 'TRAVEL_AND_LOCAL', 'TOOLS', ]


class ListingBuilder:
    def run(self):
        cl = CraigsListScraper()
        listings = []
        cl.webpage_html()
        for listing_html in cl.listings_html():
            parser = ListingParser(listing_html)
            listing = (parser.title())
            listings.append(listing)
        return listings





class CraigsListScraper:
    def webpage_html(self, url = 'https://play.google.com/store/apps/details?id=com.microsoft.office.lync15'):
        craigslist_request = requests.get(url)
        self.craigslist_html = craigslist_request.text
        return self.craigslist_html

    def listings_html(self, craigslist_html = None):
        craigslist_html = craigslist_html or self.craigslist_html
        craigslist_soup = BeautifulSoup(craigslist_html)
        listings =  craigslist_soup.findAll('div', {'class':"LXrl4c"})
        self.listings = listings
        return self.listings




class ListingParser:
    def __init__(self, listing_html):
        self.listing_html = listing_html


    def title(self):
        return self.parse(self.listing_html, 'DWPxHb')

#     def location(self):
#         return self.parse(self.listing_html, 'cui-location-name')




    # def housing(self):
    #     housing = self.parse(self.listing_html, 'housing')
        # if housing:
        #     return housing.strip()

    # def price(self, listings = None):
    #     price = self.parse(self.listing_html, 'price')
    #     return int(price[1:])

    def parse(self, listing_html, criteria):
        result = listing_html.find(class_=re.compile(r'.*%s' % criteria))
        if result:
            return result.text
        
        
