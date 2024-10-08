import argparse
from scraper.Scraper import GabScraper

def main():
    parser = argparse.ArgumentParser(description="Scrape Gabs from Gab.com")
    parser.add_argument('query', type=str, help="Search query for Gab posts")
    parser.add_argument('filename', type=str, help="Filename to save the results (with .zip extension)")
    args = parser.parse_args()

    GabScraper(args.query, args.filename)

if __name__ == "__main__":
    main()
