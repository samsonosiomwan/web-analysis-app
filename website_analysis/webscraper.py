from website_analysis.class_interface import *

class WebScraper(IWebScraper):
    '''class to process webscraping accepts the url(website address) as argument'''
    def __init__(self,enter_url):
        self.enter_url = enter_url
    
    def request_url(self):
        '''method to get requested url: accepts no argument and returns a url request'''
        return requests.get(self.enter_url)
    
    def request_content(self):
        '''method to get webpage content(webpage text): accepts no argument and returns raw string using beautifulsoup'''
        webpage_text = BeautifulSoup(self.request_url().text,'html.parser')
        return webpage_text.text