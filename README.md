# Book Scraper

This Python script scrapes book information from the 'https://books.toscrape.com/' website and saves it to a CSV file. This is a result of the GoIT Python Web Scraping Marathon by [Yuriy Kuchma](https://github.com/Krabaton).

## Requirements

- Python 3.x
- requests library
- BeautifulSoup library

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/II-777/py-book-scraper
   ```
2. Change into the project directory:

   ```shell
   cd py-book-scraper
   ```
3. Install the required libraries:

   ```shell
    pip install -r requirements.txt
   ```

## Usage

1. Run the script:

   ```shell
    python3 main.py
   ```

The script will scrape book information from the website "https://books.toscrape.com/" and save it to a file named "books.csv" in the same directory.

## The CSV file will contain the following fields for each book:

        - Title
        - Link
        - Picture
        - Price
        - Rating

## License

This project is licensed under the MIT License.
