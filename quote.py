"""A file containing the Quote class and its methods.
Authors: Bruno Lerner, Doria Philo, Yuri Kaz"""

from config_file import CONTENT_BLACKLIST, AUTHOR_BLACKLIST, HOST, \
    REPRESENTATION_FORMAT, QUOTES_REPR_SEPARATOR
from langdetect import detect


class Quote:
    """Represents an individual quote and stores its relevant information."""

    def __init__(self, html_quote):
        self.html_quote = html_quote
        self.content, self.language = self._get_content()
        self.author = self._get_author()
        self.book = self._get_book()
        self.likes = self._get_likes()
        self.tags = self._get_tags()
        self.picture_url = self._get_pic_url()
        self.info = [self.content, self.author, self.book, self.likes, self.tags, self.picture_url]

    def _get_content(self):
        """Gets the quote's content and the language it is in."""
        content = self.html_quote.find('div', class_="quoteText").contents[0]
        content = content.strip().strip(CONTENT_BLACKLIST)
        language = detect(content)      #using it from the langdetect package
        return content, language

    def _get_author(self):
        """Gets the name of the author for an individual quote."""
        text_div = self.html_quote.find('div', class_="quoteText")
        author = text_div.find('span', class_="authorOrTitle").text
        author = author.strip(AUTHOR_BLACKLIST)
        return author

    def _get_book(self):
        """Gets the book's info for an individual quote."""
        book = {}
        book_html = self.html_quote.find('a', class_="authorOrTitle")

        if book_html is not None:
            book['name'] = book_html.text
            book['link'] = HOST + book_html['href']

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
            return 'No tags found.'
        tags_raw = tags_banner.find_all('a')
        tags = []
        for tag in tags_raw:  # cleaning the html strings
            tags.append(tag.text)
        return tags

    def __repr__(self):
        info = {
            'Content': self.content,
            'Author': self.author,
            'Book name': self.book_name,
            'Book link': self.book_link,
            'Likes': self.likes,
            'Tags': self.tags
        }
        representation = ""
        for key, value in info.items():
            representation += REPRESENTATION_FORMAT % (key, value)
        representation += QUOTES_REPR_SEPARATOR

        return representation

    def _get_pic_url(self):
        """Gets the author's picture URL for an individual quote."""
        pic_html = self.html_quote.find('img')
        if pic_html is None:
            return 'No picture found.'  # If needed, we can later change
            # it to NaN or None.
        return pic_html['src']
