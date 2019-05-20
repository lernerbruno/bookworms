class Quote:
    def __init__(self, quote):
        self.quote = quote
        self.content = self._get_content(quote)
        self.author = self._get_author(quote)
        self.book_name = self._get_book_name(quote)
        self.book_link = self._get_book_link(quote)
        self.likes = self._get_likes(quote)
        self.tags = self._get_tags(quote)

    def _get_content(self, quote):
        """Takes an individualized raw quote and pulls out all of its
        content as a string."""
        content = quote.find('div', class_="quoteText").contents[0]
        content = content.strip().strip(" ”“")
        return content

    def _get_author(self, quote):
        """Extracts info about author from quote html element."""
        text_div = quote.find('div', class_="quoteText")
        author = text_div.find('span', class_="authorOrTitle").text
        return author

    def _get_book_name(self, quote):
        book_html = quote.find('a', class_="authorOrTitle")
        if book_html is None:
            return 'No book mentioned'
        else:
            return book_html.text

    def _get_book_link(self, quote):
        book_html = quote.find('a', class_="authorOrTitle")
        if book_html is None:
            return 'No book mentioned'
        else:
            uri = book_html['href']
            host = 'https://www.goodreads.com'
            print(host + uri)
            return host + uri

    def _get_likes(self, quote):
        """Takes an individualized raw quote, and pulls out how many likes it
        got. Returns an integer."""
        likes_banner = quote.find('div', class_='right')
        likes = likes_banner.a.text
        likes = int(likes.split()[0])
        return likes

    def _get_tags(self, quote):
        """Takes an individualized raw quote and pulls out all of its tags.
        Returns them as a list of strings."""
        tags_banner = quote.find('div', class_='quoteFooter')
        tags_raw = tags_banner.find_all('a')
        tags = []
        for tag in tags_raw:    #cleaning the html strings
            tags.append(tag.text)
        return tags

