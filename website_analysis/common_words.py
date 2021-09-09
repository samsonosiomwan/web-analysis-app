from website_analysis.class_interface import *
from website_analysis.find_page_content import *

class CommonWords(ICommonWords):
    '''finds top 7 words commonly used in scraped website.(methods: find_common_words, common_words,total_words_found)'''
    def __init__(self, web_scraper_url):
        #using compostion to use information from filter_webpage method in Filter_Page_Content class
        self.web_scraper_url = FilterPageContent(web_scraper_url)
    def find_common_words(self):
        '''this method returns a tuple of top 7 most used words in a list of the scraped webpage'''
        return Counter(self.web_scraper_url.filtered_webpage()).most_common(7)
    def words_found(self):
        '''this method returns a list of words found in find_common_words method'''
        return [words[0] for words in self.find_common_words()]
    def total_words_found(self):
        '''this method returns a list of total number of each words_found counted in find_common_words method'''
        return [total[1] for total in self.find_common_words()]