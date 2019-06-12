"""The main file of our project.
Authors: Bruno Lerner, Doria Philo, Yuri Kaz"""

from scraper import Scraper
from output import csv_outputter, db_outputter
from config_file import Configurations


def main():
    Configurations.parsing_args()
    Configurations.parsing_confs()

    scraper_agent = Scraper()
    quotes_objects = scraper_agent.scrap()

    if Configurations.args.format == 'csv':
        output_writer = csv_outputter.CSVOutputter(quotes_objects)
    if Configurations.args.format == 'db':
        output_writer = db_outputter.DBOutputter(quotes_objects)

    output_writer.write_output()


if __name__ == '__main__':
    main()
