"""A file containing the Outputter class and its methods.
Authors: Bruno Lerner, Doria Philo, Yuri Kaz"""

from config_file import OUTPUT_FILENAME
import abc


class Outputter:
    """Used to output the content to a specified file."""

    def __init__(self, output_filename, file_type, quotes_objects):
        self.file_type = file_type
        self.filename = output_filename + '.' + self.file_type
        self.quotes_objects = quotes_objects

    @abc.abstractmethod
    def write_output(self):
        """This is an abstract method that will create the output accordingly to the type"""