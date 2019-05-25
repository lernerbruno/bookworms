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
        self.soup = None
        self.quote_objects = []

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
        for html_quote in quotes_elements:
            new_quote = Quote(html_quote)
            self.quotes_objects.append(new_quote)

    def scrap_single_page(self):
        """This function holds the scraping workflow for 1 page."""
        quotes_elements = self._get_quotes_elements()
        self._create_quotes_objects(quotes_elements)

    def _new_url(self, page_num):
        """ Creates a proper URL containing the page number from the input. """
        url_new = '%s%s%d' % (self.root_url, PAGE_INDICATOR, page_num)
        return url_new

    def _get_url_list(self):
        """ Using the new_url function, this function goes through the numbers
        from 1 to 100 and creates a proper URL for each page number.
        Returns a list of all URLs. """
        url_list = []
        for i in range(START_PAGE, END_PAGE + 1):
            url_new = self._new_url(i)
            url_list.append(url_new)
        return url_list

    def scrap(self):
        url_list = self._get_url_list()
        for url in url_list:
            self.soup = BeautifulSoup(self._get_page_content(url),
                                      'html.parser')
            self.scrap_single_page()
        return self.quote_objects
