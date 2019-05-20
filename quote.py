class Quote:
    HOST = 'https://www.goodreads.com'
    CONTENT_BLACKLIST = ' ”“'

    def __init__(self, quote):
        self.html_quote = quote
        self.content = self._get_content()
        self.author = self._get_author()
        self.book_name = self._get_book_name()
        self.book_link = self._get_book_link()
        self.likes = self._get_likes()
        self.tags = self._get_tags()

    def _get_content(self):
        """Takes an individualized raw quote and pulls out all of its
        content as a string."""
        content = self.html_quote.find('div', class_="quoteText").contents[0]
        content = content.strip().strip(self.CONTENT_BLACKLIST)
        return content

    def _get_author(self):
        """Extracts info about author from quote html element."""
        text_div = self.html_quote.find('div', class_="quoteText")
        author = text_div.find('span', class_="authorOrTitle").text
        return author

    def _get_book_name(self):
        book_html = self.html_quote.find('a', class_="authorOrTitle")
        if book_html is None:
            return 'No book mentioned'
        else:
            return book_html.text

    def _get_book_link(self):
        book_html = self.html_quote.find('a', class_="authorOrTitle")
        if book_html is None:
            return 'No book mentioned'
        else:
            uri = book_html['href']
            return self.HOST + uri

    def _get_likes(self):
        """Takes an individualized raw quote, and pulls out how many likes it
        got. Returns an integer."""
        likes_banner = self.html_quote.find('div', class_='right')
        likes = likes_banner.a.text
        likes = int(likes.split()[0])
        return likes

    def _get_tags(self):
        """Takes an individualized raw quote and pulls out all of its tags.
        Returns them as a list of strings."""
        tags_banner = self.html_quote.find('div', class_='quoteFooter')
        tags_raw = tags_banner.find_all('a')
        tags = []
        for tag in tags_raw:    # cleaning the html strings
            tags.append(tag.text)
        return tags

