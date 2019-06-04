"""A specific class to output information to a database
Authors: Bruno Lerner, Doria Philo, Yuri Kaz"""

from output import outputter


class DBOutputter(outputter.Outputter):
    """Used to output the content to a database."""

    def __init__(self, quotes_objects):
        super().__init__(quotes_objects)

    def create_db(self):
        pass

    def write_output(self):
        pass

