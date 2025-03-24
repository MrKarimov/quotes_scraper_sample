
# Quotes Scraper Sample

This Python script scrapes **Authors** and their corresponding **Quotes** from the website [Quotes to Scrape](https://quotes.toscrape.com) and saves the extracted data into a clean, two-column CSV file.

## Features:
- Extracts **Author** and **Quote** data
- Handles multiple pages (first 10 pages)
- Outputs structured CSV file using **Pandas**
- UTF-8 encoding for better compatibility with Excel

## Requirements:
- Python 3.x
- requests
- beautifulsoup4
- pandas

## Installation:
```bash
pip install requests beautifulsoup4 pandas
```

## Usage:
```bash
python scraper_sample.py
```

## Output:
The scraped data will be saved to:

```
quotes.csv
```

The CSV file contains two columns:

| Author          | Quote                                                                                                           |
|-----------------|-----------------------------------------------------------------------------------------------------------------|
| Albert Einstein | “The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.” |
| J.K. Rowling    | “It is our choices, Harry, that show what we truly are, far more than our abilities.”                            |

---

**This script is provided as a sample for web scraping tasks, specifically focusing on clean table output.**
