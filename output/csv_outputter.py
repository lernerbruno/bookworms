"""A specific class to output information to a csv file
Authors: Bruno Lerner, Doria Philo, Yuri Kaz"""

import csv
import os
from config_file import HEADER
from output import outputter


class CSVOutputter(outputter.Outputter):
    """Used to output the content to a specified file."""

    def __init__(self, file_type, quotes_objects):
        super().__init__(file_type, quotes_objects)

    def write_output(self):
        """Writes the info of each entry to a csv file."""
        with open(self.filename, 'a', newline='', encoding='utf-8') as \
                csv_file:
            csv_writer = csv.writer(csv_file)
            if os.stat(self.filename).st_size == 0:
                # if the csv file needs a headers
                csv_writer.writerow(HEADER)
            for quote in self.quotes_objects:
                csv_writer.writerow(quote.info)