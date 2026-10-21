# Quotes Scraper using Python

A Python web scraping project that extracts quotes, authors, and tags from [Quotes to Scrape](https://quotes.toscrape.com/) and saves the data into a CSV file.

## Features

- Extracts quotes, author names, and tags.
- Scrapes multiple pages using pagination.
- Saves data into a CSV file.
- Handles request timeouts and connection errors.
- Handles HTTP errors.

## Technologies Used

- Python
- Requests
- BeautifulSoup
- CSV

## Requirements

Install the required libraries:

```bash
pip install requests beautifulsoup4
```

## How to Run

1. Open the project folder.
2. Run the Python script:

   ```bash
   python main.py
   ```

3. The extracted data will be saved in `Quotes.csv`.

## Output

The CSV file contains three columns:

- Quote
- Author
- Tags

The script is configured to scrape up to 10 pages and save all collected data in a single CSV file.

## Learning Outcomes

- HTML parsing with BeautifulSoup
- Using `find()` and `find_all()`
- Extracting nested HTML elements
- Web scraping with Requests
- Pagination
- CSV file handling
- HTTP request error handling

## Disclaimer

This project was created for educational purposes using Quotes to Scrape, a website designed for practicing web scraping.