"""The main file of our project.
Authors: Bruno Lerner, Doria Philo, Yuri Kaz"""

from scraper import Scraper
import outputter
from config_file import ROOT_URL, OUTPUT_FILENAME


def main():
    scraper_agent = Scraper(ROOT_URL)
    quotes_objects = scraper_agent.scrap()
    file_writer = outputter.Outputter(OUTPUT_FILENAME, 'csv', quotes_objects)
    file_writer.write_file()


if __name__ == '__main__':
    main()
