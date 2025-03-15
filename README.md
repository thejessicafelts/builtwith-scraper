# BuiltWith Technology Scraper

A Python script that scrapes BuiltWith.com pages for technology information used by websites, compiling a unique, sorted list of technologies.

## Overview

This project is designed to quickly and easily compile the technologies a website uses by scraping its BuiltWith.com page. You can list multiple websites in an `endpoints.txt` file (each on a new line) to process them in batch. The script deduplicates the results so that only unique technologies are included in the final output.

## Features

- **Batch Processing:** Add multiple website endpoints via `endpoints.txt`.
- **Data Extraction:** Scrapes technology data from BuiltWith.com pages.
- **Deduplication:** Outputs only unique technology names.
- **Sorted Output:** Produces a sorted list of technologies in `output.txt`.

## Requirements

- Python 3.x
- [requests](https://pypi.org/project/requests/)
- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)

## Setup

1. **Clone or Download the Repository**

   ```bash
   git clone https://github.com/thejessicafelts/builtwith-scraper.git
   cd builtwith-scraper
   ```

2. **Install Dependencies**

   Use pip to install the necessary libraries:

   ```bash
   pip install requests beautifulsoup4
   ```

3. **Prepare Endpoints File**

   Create an `endpoints.txt` file in the project directory. Each line should contain the website endpoint (the part of the URL following `http://builtwith.com/`). For example:

   ```
   example1.com
   example2.com
   example3.com
   ```

## Usage

Run the Python script:

```
python3 script.py
```

The script will:
- Read endpoints from `endpoints.txt`
- Construct full URLs by appending endpoints to the base URL `http://builtwith.com/`
- Scrape technology data from each page
- Deduplicate and sort the technology names
- Write the unique list to `output.txt`

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request for any improvements or bug fixes.