import scraper
import outputter

ROOT_URL = 'https://www.goodreads.com/quotes/recently_added'


def main():
    scraper_agent = scraper.Scraper(ROOT_URL)
    quotes_objects = scraper_agent.scrap()
    file_path = r'C:\Users\Doria\Documents\ITC\bookworms\books_quotes.csv'
    file_writer = outputter.Outputter(file_path, 'csv', quotes_objects)
    file_writer._write_file()



if __name__ == '__main__':
    # put asserts here
    main()
