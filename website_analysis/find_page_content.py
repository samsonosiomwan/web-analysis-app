from website_analysis.class_interface import *
from website_analysis.webscraper import *

class FilterPageContent(IFilterPageContent):
    '''class to filter html text and contents of the webpage(attributes:web_scraper_url, methods: filter_webage)'''
    def __init__(self,web_scraper_url):
        #composition to collect request_content from WebScraper class
        self.web_scraper_url = WebScraper(web_scraper_url)

    def filtered_webpage(self):
        '''this method uses regex to filter non useful information e.g newlines, tabs,html tags,common_words(from src.utils module) etc. and returns a list of filtered text'''
        pattern = re.compile(r'[a-zA-Z]+')
        filtered_text = pattern.findall(self.web_scraper_url.request_content())
        return [words for words in filtered_text if words not in common_words]