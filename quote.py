"""A file containing the Quote class and its methods.
Authors: Bruno Lerner, Doria Philo, Yuri Kaz"""
from langdetect import detect, lang_detect_exception
import re

CONTENT_BLACKLIST = ' ""'
AUTHOR_BLACKLIST = "\n ,"
REPRESENTATION_FORMAT = '%s: %s\n'
QUOTES_REPR_SEPARATOR = '-----------------------------------\n'
BOOK_ID_PATTERN = '/(\d*)$'
AUTHOR_ID_PATTERN = '/(\d*)\.'


class Quote:
    """Represents an individual quote and stores its relevant information."""

    def __init__(self, html_quote):
        self.html_quote = html_quote
        self.content, self.language = self._get_content()
        self.author = self._get_author()
        self.book = self._get_book()
        self.likes = self._get_likes()
        self.tags = self._get_tags()
        self.info = [self.content, self.author, self.book, self.likes, self.tags]

    def _get_content(self):
        """Gets the quote's content and the language it is in."""
        content = self.html_quote.find('div', class_="quoteText").contents[0]
        content = content.strip().strip(CONTENT_BLACKLIST)
        try:
            language = detect(content)
        except lang_detect_exception.LangDetectException:
            language = 'undefined'

        return content, language

    def _get_author(self):
        """Gets the name of the author for an individual quote."""
        author = {'id': 0, 'name': ''}
        text_div = self.html_quote.find('div', class_="quoteText")
        author['name'] = text_div.find('span', class_="authorOrTitle").text.strip(AUTHOR_BLACKLIST)

        pic_html = self.html_quote.find('img')
        if pic_html is not None:
            match = re.search(AUTHOR_ID_PATTERN, pic_html['src'])
            if match is not None:
                author_id = match.group(1)
                author['id'] = int(author_id)
        return author

    def _get_book(self):
        """Gets the book's info for an individual quote."""
        book = {'id': 0, 'name': ''}
        book_html = self.html_quote.find('a', class_="authorOrTitle")
        if book_html is not None:
            book['name'] = book_html.text

            match = re.search(BOOK_ID_PATTERN, book_html['href'])
            if match is not None:
                book_id = match.group(1)
                book['id'] = int(book_id)
        return book

    def _get_likes(self):
        """Gets the number of likes for an individual quote."""
        likes_banner = self.html_quote.find('div', class_='right')
        likes = likes_banner.a.text
        likes = int(likes.split()[0])
        return likes

    def _get_tags(self):
        """Gets the tags for an individual quote. Returns them as a list
        of strings."""
        tags_banner = self.html_quote.find('div', class_='quoteFooter')
        tags_banner = tags_banner.find('div', class_='greyText')

        if tags_banner is None:
            return 'No tags found'

        tags_raw = tags_banner.find_all('a')
        tags = []
        for tag in tags_raw:  # cleaning the html strings
            tags.append(tag.text)
        return tags

    def __repr__(self):
        info = {
            'Content': self.content,
            'Language': self.language,
            'Author': self.author.name,
            'Author Id': self.author.id,
            'Book name': self.book.name,
            'Book link': self.book.id,
            'Likes': self.likes,
            'Tags': self.tags
        }
        representation = ""
        for key, value in info.items():
            representation += REPRESENTATION_FORMAT % (key, value)
        representation += QUOTES_REPR_SEPARATOR

        return representation
