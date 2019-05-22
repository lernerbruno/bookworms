import csv
import os


class Outputter:
    HEADER = ['content', 'author', 'book_name', 'book_link',
              'likes', 'tags']

    def __init__(self, filename, file_type, quotes_objects):
        self.file_type = file_type
        self.filename = filename
        self.quotes_objects = quotes_objects

    def _write_file(self):
        """Writes the info of each quote to a file according to input."""
        if self.file_type == 'csv':
            self._write_to_csv()
        if self.file_type == 'txt':
            pass

    def _write_to_csv(self):
        """Writes the info of the quotes to a csv file."""
        with open(self.filename, 'a', newline='', encoding='utf-8') as \
                csv_file:
            csv_writer = csv.writer(csv_file)
            if os.stat(self.filename).st_size == 0:  # if the csv file needs
                # a headers
                csv_writer.writerow(self.HEADER)
            for quote in self.quotes_objects:
                csv_writer.writerow(quote.info)
