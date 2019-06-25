"""A specific class to output information to a database
Authors: Bruno Lerner, Doria Philo, Yuri Kaz"""

from output import outputter
import pymysql


class DBOutputter(outputter.Outputter):
    """Used to output the content to a database."""

    def __init__(self, quotes_objects):
        super().__init__(quotes_objects)

    def write_output(self):
        username = input('Please enter your MySQL username: ')
        password = input('Please enter your MySQL password: ')
        con = pymysql.connect(host='localhost', database='book_quotes',
                              password=password, user=username)
        cur = con.cursor()
        for quote_object in self.quotes_objects:
            if quote_object.language != 'en':
                continue

            try:
                cur.execute("""
                       INSERT INTO authors (author_name, GR_author_id)
                       VALUES ("{}", {});""".format(quote_object.author['name'],
                                                    quote_object.author['id']))
            except pymysql.err.IntegrityError:
                print("Found an existing author")

            cur.execute("""
                   SELECT author_id FROM authors 
                   WHERE author_name = "{}";""".format(quote_object.author['name']))
            author_id = cur.fetchone()[0]

            try:
                cur.execute("""
                       INSERT INTO books (book_name, GR_book_id)
                       VALUES ("{}", {});""".format(quote_object.book['name'],
                                                    quote_object.book['id']))
            except pymysql.err.IntegrityError:
                print("Found an existing book")
                
            cur.execute("""
                   SELECT book_id FROM books
                   WHERE book_name = "{}";""".format(quote_object.book['name']))
            book_id = cur.fetchone()[0]

            cur.execute("""
                   INSERT INTO quotes (quote_content, likes, author_id, book_id)
                   VALUES ("{}", {}, {}, {})
                   ON DUPLICATE KEY UPDATE likes={};""".format(quote_object.content.replace('"', '\\"'),
                                                               quote_object.likes,
                                                               author_id, book_id,
                                                               quote_object.likes))
            cur.execute("""
                   SELECT quote_id FROM quotes
                   WHERE quote_content like "{}%";""".format(quote_object.content[:100]))
            quote_id = cur.fetchone()[0]

            for tag in quote_object.tags:
                try:
                    cur.execute("""
                           INSERT INTO tags (tag_name)
                           VALUES ("{}");""".format(tag))
                except pymysql.err.IntegrityError:
                    print("Found an existing tag")
                finally:
                    cur.execute("""
                           SELECT tag_id FROM tags
                           WHERE tag_name = "{}";""".format(tag))
                    tag_id = cur.fetchone()[0]

                    cur.execute("""
                           INSERT INTO quote_tags (quote_id,tag_id)
                           VALUES ({}, {});""".format(quote_id, tag_id))

        # I dont think we are using this commit, but we could do a commit for each page,
        #   so If a page has a problem, we would know which info we are lacking (TODO?)
        con.commit()
        con.close()
