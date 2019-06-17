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

            # I think this following approach is better, but something is wrong, need to debug
            #
            # cur.execute("""
            #     INSERT INTO authors (author_name, GR_author_id)
            #     VALUES ("{}", {});
            #
            #     SET @author_id = LAST_INSERT_ID();
            #
            #     INSERT INTO books (book_name, GR_book_id)
            #     VALUES ("{}", {});
            #
            #     SET @book_id = LAST_INSERT_ID();
            #
            #     INSERT INTO quotes (quote_content, likes, tags, author_id, book_id)
            #     VALUES ('{}', {}, '{}' ,@author_id, @book_id)
            #     ON DUPLICATE KEY UPDATE likes={};
            # """.format(quote_object.author['name'], quote_object.author['id'],
            #            quote_object.book['name'], quote_object.book['id'],
            #            quote_object.content, quote_object.likes, str(quote_object.tags),
            #            quote_object.likes))

            cur.execute("""
                   INSERT INTO authors (author_name, GR_author_id)
                   VALUES ("{}", {});""".format(quote_object.author['name'],
                                                quote_object.author['id']))

            cur.execute("""
                   SELECT LAST_INSERT_ID();""")
            author_id = cur.fetchone()[0]

            cur.execute("""
                   INSERT INTO books (book_name, GR_book_id)
                   VALUES ("{}", {});""".format(quote_object.book['name'],
                                                quote_object.book['id']))

            cur.execute("""
                   SELECT LAST_INSERT_ID();""")
            book_id = cur.fetchone()[0]

            cur.execute("""
                   INSERT INTO quotes (quote_content, likes, tags, author_id, book_id)
                   VALUES ("{}", {}, "{}", {}, {})
                   ON DUPLICATE KEY UPDATE likes={};""".format(quote_object.content.replace('"', '\\"'),
                                                               quote_object.likes,
                                                               str(quote_object.tags), author_id, book_id,
                                                               quote_object.likes))

        # I dont think we are using this commit, but we could do a commit for each page,
        #   so If a page has a problem, we would know which info we are lacking (TODO?)
        con.commit()
        con.close()
