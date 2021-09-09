import requests
from bs4 import BeautifulSoup
import re
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np 
from src.utils import *
from abc import ABC, abstractmethod

class IWebScraper(ABC):
    '''webscrapper interface containing the url to scrape and the webpage to scrape content'''
    @abstractmethod
    def request_url():
        pass
    # @abstractmethod
    def webpage_content():
        pass

class IFilterPageContent(ABC):
    '''filter text interface to filter html gotten from webpage'''
    @abstractmethod
    def filtered_webpage():
        pass

class ICommonWords(ABC):
    '''common words interface with find_common_words method, words_found method, total_words_found method'''
    def find_common_words(self):
        pass
    def words_found(self):
        pass
    def total_words_found(self):
        pass

class IWebPageAnalysisChart(ABC):
    '''interface for web analysis and its methods are(common_words(), pie_chart(), bar_chart())'''

    @abstractmethod
    def pie_chart():
        pass

    @abstractmethod
    def bar_chart():
        pass