import csv
import os
from config_file import HEADER, OUTPUT_FILENAME


class Outputter:
    """Used to output the content to a specified file."""

    def __init__(self, filename, file_type, quotes_objects):
        self.file_type = file_type
        self.filename = OUTPUT_FILENAME + '.' + self.file_type
        self.quotes_objects = quotes_objects

    def write_file(self):
        """Writes the info of each entry to a file according to the
        specified file type."""
        if self.file_type == 'csv':
            self._write_to_csv()
        if self.file_type == 'txt':
            pass

    def _write_to_csv(self):
        """Writes the info of each entry to a csv file."""
        with open(self.filename, 'a', newline='', encoding='utf-8') as \
                csv_file:
            csv_writer = csv.writer(csv_file)
            if os.stat(self.filename).st_size == 0:  # if the csv file needs
                # a headers
                csv_writer.writerow(HEADER)
            for quote in self.quotes_objects:
                csv_writer.writerow(quote.info)
