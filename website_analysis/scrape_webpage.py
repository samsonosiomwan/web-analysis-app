import website_analysis
from website_analysis.webpage_analysis_chart import *

class ScrapeWebpage:
    '''this class has web_analysis method that requests for url to scrape from the user, accepts it process the user input'''
    def web_analysis(self):
        '''function to scrape and process website analysis,accepts no argument and returns results in charts'''
        scrape_website= input('Would you like to scrape a website (y/n)?: ')
        while True:
            try:

                if scrape_website == 'y':
                    try:
                        enter_url = input('Enter a website to analyze: ')
                        #analyse scraped site by instantiating the webPageAnalysisChart
                        webpage_analysis = WebPageAnalysisChart(enter_url)
                        webpage_analysis.display_charts()
                        self.web_analysis().open()

                    except:
                        print('connection error: please enter a valid url format (e.g: https://www.yoursite.com),check your internet and try again.')
                        self.web_analysis()

                elif scrape_website == 'n':
                    exit('Thanks for analyzing! Come back again!')
                else:
                    raise ValueError
            except ValueError:
                print('invalid response: respond with \'y or n\' and try again')
            break
    
   


    