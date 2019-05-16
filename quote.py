class Quote:
    def __init__(self, quote):
        self.quote = quote
        self.author = self.__get_author(quote)
        self.tags = self.__get_tags(quote)
        self.number_of_likes = self.__get_likes(quote)
        self.book = self.__get_book(quote)

    def __get_author(self, quote):
        """
        Extracts info about author from quote html element
        """
        text_div = quote.find('div', class_="quoteText")
        author = text_div.find('span', class_="authorOrTitle").text
        return author

    def __get_likes(self, quote):
        """Takes an individualized raw quote, and pulls out how many likes it
        got. Returns an integer."""
        likes_banner = quote.find('div', class_='right')
        likes = likes_banner.a.text
        likes = int(likes.split()[0])
        return likes

    def __get_tags(self, quote):
        """Takes an individualized raw quote and pulls out all of its tags.
        Returns them as a list of strings."""
        tags_banner = quote.find('div', class_='quoteFooter')
        tags_list = tags_banner.find_all('a')
        print(tags_list)  # TODO: clean this string
