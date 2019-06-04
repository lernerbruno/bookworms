"""A specific class to output information to a database
Authors: Bruno Lerner, Doria Philo, Yuri Kaz"""

from output import outputter


class DBOutputter(outputter.Outputter):
    """Used to output the content to a database."""

    def __init__(self, file_type, quotes_objects):
        super().__init__(file_type, quotes_objects)

    def create_output(self):
        pass
