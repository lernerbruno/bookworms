import scraper
import outputter

ROOT_URL = 'https://www.goodreads.com/quotes/recently_added'


def main():
    scraper_agent = scraper.Scraper(ROOT_URL)
    quotes_objects = scraper_agent.scrap()
    filename = 'books_quotes.csv'
    file_writer = outputter.Outputter(filename, 'csv', quotes_objects)
    # file_writer._write_file()


if __name__ == '__main__':
    # put asserts here
    main()
