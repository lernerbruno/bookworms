"""The main file of our project.
Authors: Bruno Lerner, Doria Philo, Yuri Kaz"""

from scraper import Scraper
from output import outputter
from config_file import ROOT_URL
import argparse


def parsing_args():
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
    return args
from output import outputter
from config_file import ROOT_URL, OUTPUT_FILENAME


def main():
    # unpacking args
    args = parsing_args()
    output_file_format = args.format
    end_page = args.max_pg
    output_filename = args.output_filename

    # main program
    scraper_agent = Scraper(ROOT_URL, end_page)
    quotes_objects = scraper_agent.scrap()
    file_writer = outputter.Outputter(output_filename, output_file_format, quotes_objects)
    file_writer.write_file()


if __name__ == '__main__':
    main()
