# Quotes Scraper using Python

A Python web scraping and data analysis project that extracts quotes, authors, and tags from [Quotes to Scrape](https://quotes.toscrape.com/), stores the data in a CSV file, and performs data cleaning and analysis using Pandas.

## Features

- Extracts quotes, author names, and tags.
- Scrapes multiple pages using pagination.
- Saves scraped data into a CSV file.
- Handles request timeouts and connection errors.
- Handles HTTP errors.
- Identifies and cleans missing values.
- Filters quotes based on tags.
- Groups quotes by author and calculates quote counts.
- Checks for duplicate rows and quotes.
- Exports cleaned data and author-wise quote counts to Excel files.

## Technologies Used

- Python
- Requests
- BeautifulSoup
- Pandas
- CSV
- Excel (openpyxl)

## Requirements

Install the required libraries:

```bash
pip install requests beautifulsoup4 pandas openpyxl
```

## How to Run

1. Clone or download this repository.
2. Open the project folder in VS Code.
3. Install the required libraries:

```bash
pip install requests beautifulsoup4 pandas openpyxl
```

4. Run the web scraping script:

```bash
python main.py
```

5. Run the data analysis and Excel export script:

```bash
python Quote_Scraper_Excel.py
```

The first script scrapes quotes and saves them to `Quotes.csv`. The second script cleans and analyzes the data, then exports the results to Excel files.


## Output Files

| File | Description |
|---|---|
| `Quotes.csv` | Scraped quotes, authors, and tags |
| `Quotes.xlsx` | Cleaned dataset exported to Excel |
| `Quote.xlsx` | Author-wise quote counts |

## Data Analysis with Pandas

The project uses Pandas to:

- Read and analyze CSV data.
- Check missing values.
- Replace missing tags with `"No Tags"`.
- Filter quotes using tag-based conditions.
- Count quotes for each author.
- Check duplicate rows and duplicate quotes.
- Export processed data to Excel.

## Learning Outcomes

- Web scraping with Requests and BeautifulSoup.
- HTML parsing using `find()` and `find_all()`.
- Extracting nested HTML elements.
- Handling pagination and HTTP errors.
- Reading and writing CSV files.
- Data cleaning and filtering with Pandas.
- Grouping and counting data.
- Detecting duplicate records.
- Generating Excel reports.

## Disclaimer

This project was created for educational purposes using [Quotes to Scrape](https://quotes.toscrape.com/), a website designed for practicing web scraping.
