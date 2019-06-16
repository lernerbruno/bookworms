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
                VALUES (%s, %s)
            
                SET @author_id = LAST_INSERT_ID()
                
                INSERT INTO books (book_name, GR_book_id)
                VALUES (%s, %d)
            
                SET @book_id = LAST_INSERT_ID()
                
                INSERT INTO quotes (quote_content, likes, tags, author_id, book_id)
                VALUES (%s, %d, $s ,@author_id, @book_id) 
                ON DUPLICATE KEY UPDATE likes=%d
            """, quote_object.author['name'], quote_object.author['id'],
                    quote_object.book['name'], quote_object.book['id'],
                    quote_object.content, quote_object.likes, str(quote_object.tags),
                    quote_object.likes)

        # I dont think we are using this commit, but we could do a commit for each page,
        #   so If a page has a problem, we would know which info we are lacking (TODO?)
        con.commit()
        con.close()
