"""A file containing the Config class and its methods.
Authors: Bruno Lerner, Doria Philo, Yuri Kaz"""

import argparse


class Configurations:
    """Used to hold every config for the whole project to run."""

    @classmethod
    def parsing_args(cls):
        """Organizes and parses arguments from the CLI."""

        parser = argparse.ArgumentParser(description='Insert a description here later')  # TODO describe the parser

        # optional args
        parser.add_argument('-s', '--show_output', action='store_true', help='Prints results in CLI.')
        parser.add_argument('-o', '--output_filename', default='books_quotes',
                            help='Define an output file. If existent, appends.')
        parser.add_argument('-max_pg', type=int, default=5, choices=range(1, 101),
                            help='Define a maximum number of pages to scrape.')  # there is a maximum # of pgs available to scrape
        parser.add_argument('-f', '--format', choices=['csv', 'db'], default='csv',
                            help='Stores results in a file in the entered format.')  # TODO we can take out the default later

        args = parser.parse_args()
        cls.args = args

    @classmethod
    def parsing_confs(cls):
        """Organizes and parses arguments from the CLI."""
        cls.host = 'https://www.goodreads.com'
        cls.root_url = cls.host + '/quotes/recently_added'
        cls.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)' \
                         ' AppleWebKit/537.36(KHTML, like Gecko) Chrome/74.0.3729.131' \
                         ' Safari/537.36'
        cls.pg_indicator = '?page='
        cls.start_page = 1
        cls.header = ['content', 'author', 'book', 'likes', 'tags', 'img_url']
