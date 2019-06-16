"""A file containing the Outputter class and its methods.
Authors: Bruno Lerner, Doria Philo, Yuri Kaz"""

import abc


class Outputter:
    """Abstract class that has some subclasses for outputting the content scrapped."""

    def __init__(self, quotes_objects):
        self.quotes_objects = quotes_objects

    @abc.abstractmethod
    def write_output(self):
        """This is an abstract method that will create the output accordingly to the type"""
