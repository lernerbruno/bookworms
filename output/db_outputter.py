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
            cur.execute("""
                INSERT INTO authors (author_name, GR_author_id)
                VALUES ('{}', '{}');""".format(quote_object.author['name'],
                        quote_object.author['id']))
            cur.execute("""
                    INSERT INTO books (book_name, GR_book_id)
                    VALUES ('{}', '{}');""".format(quote_object.book['name'],
                        quote_object.book['id']))
            cur.execute("""
                    SELECT author_id 
                    FROM authors
                    WHERE author_name=%s;""", quote_object.author['name'])
            author_id = cur.fetchone()
            cur.execute("""
            INSERT INTO quotes (quote_content, likes, tags, author_id)
            VALUES (%s, %d, %s, %d) 
            ON DUPLICATE KEY UPDATE likes=%d;""",
                        (quote_object.content, quote_object.likes,
                        quote_object.tags, author_id,
                        quote_object.likes))
        con.commit()
        con.close()
