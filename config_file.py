"""A configuration file for Bookworms project.
Authors: Bruno Lerner, Doria Philo, Yuri Kaz"""

# quote
HOST = 'https://www.goodreads.com'
CONTENT_BLACKLIST = ' ”“'
AUTHOR_BLACKLIST = "\n ,"
REPRESENTATION_FORMAT = '%s: %s\n'
QUOTES_REPR_SEPARATOR = '-----------------------------------\n'

# scraper
ROOT_URL = HOST + '/quotes/recently_added'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)' \
             ' AppleWebKit/537.36(KHTML, like Gecko) Chrome/74.0.3729.131' \
             ' Safari/537.36'
PAGE_INDICATOR = '?page='
START_PAGE = 1  # the first page to be scraped
END_PAGE = 100  # last page to be scraped

# outputter
HEADER = ['content', 'author', 'book_name', 'book_link', 'likes', 'tags',
          'img_url']

# main
OUTPUT_FILENAME = 'books_quotes'
