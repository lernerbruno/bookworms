"""A file containing the Quote class and its methods.
Authors: Bruno Lerner, Doria Philo, Yuri Kaz"""
from config_file import Configurations

CONTENT_BLACKLIST = ' ”“'
AUTHOR_BLACKLIST = "\n ,"
REPRESENTATION_FORMAT = '%s: %s\n'
QUOTES_REPR_SEPARATOR = '-----------------------------------\n'


class Quote:
    """Represents an individual quote and stores its relevant information."""

    def __init__(self, html_quote):
        self.html_quote = html_quote
        self.content = self._get_content()
        self.author = self._get_author()
        self.book_name = self._get_book_name()
        self.book_link = self._get_book_link()
        self.likes = self._get_likes()
        self.tags = self._get_tags()
        self.picture_url = self._get_pic_url()
        self.info = [self.content, self.author, self.book_name,
                     self.book_link, self.likes, self.tags, self.picture_url]

    def _get_content(self):
        """Gets the quote's content."""
        content = self.html_quote.find('div', class_="quoteText").contents[0]
        content = content.strip().strip(CONTENT_BLACKLIST)
        return content

    def _get_author(self):
        """Gets the name of the author for an individual quote."""
        text_div = self.html_quote.find('div', class_="quoteText")
        author = text_div.find('span', class_="authorOrTitle").text
        author = author.strip(AUTHOR_BLACKLIST)
        return author

    def _get_book_name(self):
        """Gets the book's name for an individual quote."""
        book_html = self.html_quote.find('a', class_="authorOrTitle")
        if book_html is None:
            return 'No book mentioned'
        else:
            return book_html.text

    def _get_book_link(self):
        """Gets the book's link for an individual quote."""
        book_html = self.html_quote.find('a', class_="authorOrTitle")
        if book_html is None:
            return 'No book mentioned'
        else:
            uri = book_html['href']
            return Configurations.host + uri

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
        tags_banner = self.html_quote.find('div', class_='greyText')
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
