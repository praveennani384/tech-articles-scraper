# Tech Articles Scraper

## Overview

The **Tech Articles Scraper** is a Python-based web scraping project that utilizes Selenium to extract data from a series of static HTML pages. This project showcases the ability to automate the extraction of valuable information such as article titles, authors, publication dates, summaries, tags, and contact details.

## Features

- Scrapes data from multiple pages and articles.
- Supports navigation through paginated content.
- Collects and stores extracted information in CSV format.
- Utilizes Selenium WebDriver for browser automation.
- Well-structured HTML templates simulating a tech articles website.

## Technologies Used

- Python
- Selenium
- HTML
- CSS
- CSV

## Directory Structure

```
Article_sample_pages/
│
├── HTML_templates/
│   ├── indexes/                # Contains index pages
│   ├── articles/               # Contains article pages
│   └── css/                    # Contains CSS files
│
├── app.py                      # Main application file for scraping
└── README.md                   # Project documentation
```

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/praveennani384/tech-articles-scraper.git
   ```

2. Navigate to the project directory:

   ```bash
   cd tech-articles-scraper
   ```

3. Install the required packages:

   ```bash
   pip install selenium
   ```

4. Ensure you have the Chrome WebDriver installed and configured in your PATH.

5. Run the application:

   ```bash
   python app.py
   ```

## Output

The scraped data will be saved in a CSV file in the current working directory.

## Author

**K Praveen Kumar**
