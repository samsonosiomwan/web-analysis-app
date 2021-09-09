import unittest
from website_analysis.webscraper import *
from website_analysis.common_words import *

class TestInput(unittest.TestCase):
  def setUp(self):
    self.web_scraper = WebScraper('https://www.python.org')
    self.common_words = CommonWords('https://www.python.org')
  def test_request_url(self):
    result = self.web_scraper.request_url().status_code
    self.assertEqual(result, 200)

  def test_request_content(self):
    # web_scraper = WebScraper('https://www.python.org')
    result = self.web_scraper.request_content()
    self.assertIsNotNone(result)

  def test_CommonWords(self):
    result = self.common_words.find_common_words()
    self.assertIsNotNone(result)

  def tearDown(self):
    self.web_scraper = None
