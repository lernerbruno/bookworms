import requests
from bs4 import BeautifulSoup


class Scraper:

    def __init__(self, root_url):
        self.root_url = root_url
        self.soup = BeautifulSoup(self.__get_page_content(root_url), 'html.parser')

    def __get_page_content(self, url):
        headers = {'user-agent': 'bruno'}
        r = requests.get(url, headers=headers)
        return r.text

    def __get_quotes(self):
        quotes = self.soup.find_all('div', class_='quoteDetails')
        return quotes

    def __get_info_from_quotes(self, quotes):
        quotes_info = []
        for quote in quotes:
            quotes_info.append(self.__get_quote_info(quote))

    def __get_quote_info(self, quote):
        author = self.__get_author(quote)
        # quote_text = get_text(quote)
        # likes = get_likes(quote)
        # tags = get_tags(quote)
        # book, book_link = get_book(quote)
        #
        # quote_obj = quote.Quote(quote_text, author, tags, likes, book)
        # return quote_obj
        return

    def __get_author(self, quote):
        text_div = quote.find('div', class_="quoteText")
        author = text_div.find('span', class_="authorOrTitle").text
        return author

    def __get_likes(self, quote):
        """Takes an individualized raw quote, and pulls out how many likes it got. Returns an integer."""
        likes_banner = quote.find('div', class_='right')
        likes = likes_banner.a.text
        likes = int(likes.split()[0])
        return likes

    def __get_tags(self, quote):
        """Takes an individualized raw quote and pulls out all of its tags. Returns them as a list of strings."""
        tags_banner = quote.find('div', class_='quoteFooter')
        tags_list = tags_banner.find_all('a')
        print(tags_list)  # TODO: clean this string
        
    def __new_url(self, url, page_num):
        """ Creates a proper URL containing the page number from the input and a
        default of showing 50 questions per page. """
        addition = '?page='
        url_new = url + addition + str(page_num)
        return url_new

    def __iterate_pages(self, url):
        """ Using the new_url function, this function goes through the numbers
        from 1 to 100 and creates a proper URL for each page number.
         Returns a list of all URLs. """
        url_list = []
        for i in range(1, 101):
            url_new = self.new_url(url, i)
            url_list.append(url_new)
        return url_list

    def scrap(self):
        quotes = self.__get_quotes()
        info = self.__get_info_from_quotes(quotes)

