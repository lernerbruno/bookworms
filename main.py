"""The main file of our project.
Authors: Bruno Lerner, Doria Philo, Yuri Kaz"""

from scraper import Scraper
import outputter
from config_file import ROOT_URL, OUTPUT_FILENAME
import argparse


def parsing_args():
    """Organizes and parses arguments from the CLI."""

    parser = argparse.ArgumentParser(description='Insert a description here later') # TODO describe the parser

    parser.add_argument('-csv', action='store_true')

    args = parser.parse_args()
    return args


def main():
    # args = parsing_args() # TODO will return the arguments from CLI when function is done
    scraper_agent = Scraper(ROOT_URL)
    quotes_objects = scraper_agent.scrap()
    file_writer = outputter.Outputter(OUTPUT_FILENAME, 'csv', quotes_objects)
    file_writer.write_file()


if __name__ == '__main__':
    main()
