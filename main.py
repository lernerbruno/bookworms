import scraper

ROOT_URL = 'https://www.goodreads.com/quotes/recently_added'

def main():
    scraper_agent = scraper.Scraper(ROOT_URL)
    scraper_agent.scrap()

if __name__ == '__main__':
    # put asserts here
    main()
