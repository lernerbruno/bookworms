"""A specific class to output information to a csv file
Authors: Bruno Lerner, Doria Philo, Yuri Kaz"""

import csv
import os
from output import outputter
from config_file import Configurations


class CSVOutputter(outputter.Outputter):
    """Used to output the content to a specified file."""

    def __init__(self, quotes_objects):
        super().__init__(quotes_objects)
        self.filename = Configurations.args.output_filename + '.csv'

    def write_output(self):
        """Writes the info of each entry to a csv file."""
        with open(self.filename, 'a', newline='', encoding='utf-8') as \
                csv_file:
            csv_writer = csv.writer(csv_file)
            if os.stat(self.filename).st_size == 0:
                # if the csv file needs a headers
                csv_writer.writerow(Configurations.header)
            for quote in self.quotes_objects:
                csv_writer.writerow(quote.info)
