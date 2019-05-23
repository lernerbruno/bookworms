"""A file containing the Scraper class and its methods.
Authors: Bruno Lerner, Doria Philo, Yuri Kaz"""

import requests
from bs4 import BeautifulSoup
from quote import Quote
from config_file import USER_AGENT, PAGE_INDICATOR, START_PAGE, END_PAGE


class Scraper:
    """Used to scrape a 'goodreads' web page for its book quotes."""

    def __init__(self, root_url):
        self.root_url = root_url
        self.soup = BeautifulSoup(self._get_page_content(root_url),
                                  'html.parser')

    def _get_page_content(self, url):
        """Pulls the whole url's HTML as string."""
        headers = {'user-agent': USER_AGENT}
        r = requests.get(url, headers=headers)
        return r.text

    def _get_quotes_elements(self):
        """Gets a list of all individual quotes as HTML elements."""
        quotes = self.soup.find_all('div', class_='quoteDetails')
        return quotes

    def _create_quotes_objects(self, quotes_elements):
        """Iterates over the elements found in HTML and generate
        Quote objects from them."""
        quotes_objects = []
        for html_quote in quotes_elements:
            new_quote = Quote(html_quote)
            quotes_objects.append(new_quote)
        return quotes_objects

    def _new_url(self, url, page_num):
        """Creates a new proper url containing the page number from the
        input."""
        url_new = '%s%s%d' % (url, PAGE_INDICATOR, page_num)
        return url_new

    def _iterate_pages(self, url):
        """Goes through the numbers from start page to end page and creating a
        proper url for each page number. Returns a list of all URLs."""
        url_list = []
        for i in range(START_PAGE, END_PAGE + 1):
            url_new = self._new_url(url, i)
            url_list.append(url_new)
        return url_list

    def scrap(self):
        """This function holds the scraping workflow."""
        quotes_elements = self._get_quotes_elements()
        quotes_objects = self._create_quotes_objects(quotes_elements)
        return quotes_objects
