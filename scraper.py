import requests
from bs4 import BeautifulSoup, NavigableString
import quote


class Scraper:
    USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ' \
                 '(KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'

    def __init__(self, root_url):
        self.root_url = root_url
        self.soup = BeautifulSoup(self._get_page_content(root_url),
                                  'html.parser')

    def _get_page_content(self, url):
        """Gets the url and do the request. 
        It returns the whole HTML as string."""
        headers = {'user-agent': self.USER_AGENT}
        r = requests.get(url, headers=headers)
        return r.text

    def _get_quotes_elements(self):
        """ Gets a list of all individual quotes as HTML elements. """
        quotes = self.soup.find_all('div', class_='quoteDetails')
        return quotes

    def _create_quotes_objects(self, quotes):
        """It iterates over the elements found in HTML and generate 
        Quote objects from them."""
        quotes_objects = []
        for q in quotes:
            new_quote = quote.Quote(q)
            quotes_objects.append(new_quote)
        return quotes_objects

    def _new_url(self, url, page_num):
        """ Creates a proper URL containing the page number from the input. """
        page_indicator = '?page='
        url_new = url + page_indicator + str(page_num)
        return url_new

    def _iterate_pages(self, url):
        """ Using the new_url function, this function goes through the numbers
        from 1 to 100 and creates a proper URL for each page number.
        Returns a list of all URLs. """
        url_list = []
        for i in range(1, 101):
            url_new = self._new_url(url, i)
            url_list.append(url_new)
        return url_list

    def scrap(self):
        """This function holds the scraping workflow."""
        html_quotes = self._get_quotes_elements()
        detailed_quotes = self._create_quotes_objects(html_quotes)
        for dq in detailed_quotes:
            print(dq)
