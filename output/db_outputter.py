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

            # If there is an author, we wanna save it in author's table
            if quote_object.author['name'] is not None:
                try:
                    cur.execute("""
                           INSERT INTO authors (author_name, GR_author_id, gender, year_of_birth, ethnic_group, country)
                           VALUES (%s, %s, %s, %s, %s, %s);""", (quote_object.author['name'],
                                                                 quote_object.author['id'],
                                                                 quote_object.api_data['gender'],
                                                                 quote_object.api_data['year'],
                                                                 quote_object.api_data['ethnic_group'],
                                                                 quote_object.api_data['country']))
                except pymysql.err.IntegrityError:
                    print("Found an existing author")

                except pymysql.err.InternalError as err:
                    print("Some internal error")
                    print(err)

                finally:
                    cur.execute("""
                           SELECT author_id FROM authors 
                           WHERE author_name like %s and GR_author_id = %s;""", (quote_object.author['name'], quote_object.author['id']))

                    author_id = cur.fetchone()[0]

            else:
                author_id = None

            # If there is a book, we wanna save it in book's table
            if quote_object.book['name'] is not None:
                try:
                    cur.execute("""
                           INSERT INTO books (book_name, GR_book_id)
                           VALUES (%s, %s);""", (quote_object.book['name'],
                                                 quote_object.book['id']))

                except pymysql.err.IntegrityError:
                    print("Found an existing book")

                except pymysql.err.InternalError as err:
                    print("Some internal error")
                    print(err)

                finally:
                    cur.execute("""
                           SELECT book_id FROM books
                           WHERE book_name like %s;""", quote_object.book['name'])

                    book_id = cur.fetchone()[0]
            else:
                book_id = None

            try:
                cur.execute("""
                       INSERT INTO quotes (quote_content, likes, author_id, book_id)
                       VALUES (%s, %s, %s, %s)
                       ON DUPLICATE KEY UPDATE likes=%s;""", (quote_object.content,
                                                              quote_object.likes,
                                                              author_id, book_id,
                                                              quote_object.likes))
                cur.execute("""
                       SELECT quote_id FROM quotes
                       WHERE quote_content like %s;""", quote_object.content[:100] + '%')

                quote_id = cur.fetchone()[0]

            except pymysql.err.ProgrammingError:
                print(
                    "Error in Syntax (probably because some strange char in content)\
                     when looking for quote_id\nContent:\n")
                print(quote_object.content[:100])

            for tag in quote_object.tags:
                try:
                    cur.execute("""
                           INSERT INTO tags (tag_name)
                           VALUES (%s);""", tag)

                except pymysql.err.IntegrityError:
                    print("Found an existing tag")

                finally:
                    cur.execute("""
                           SELECT tag_id FROM tags
                           WHERE tag_name like %s;""", tag)
                    tag_id = cur.fetchone()[0]

                if quote_id is not None and tag_id is not None:
                    cur.execute("""
                           INSERT INTO quote_tags (quote_id,tag_id)
                           VALUES (%s, %s);""", (str(quote_id), str(tag_id)))
        # I dont think we are using this commit, but we could do a commit for each page,
        #   so If a page has a problem, we would know which info we are lacking (TODO?)
        con.commit()
        con.close()
