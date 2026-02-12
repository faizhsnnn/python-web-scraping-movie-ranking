# Python Web Scraping – Movie Ranking Extraction

## Overview

This project demonstrates automated data extraction from a live website using Python, BeautifulSoup, and requests.

The script retrieves a ranked movie list from an online publication, parses structured HTML elements, filters relevant entries, and exports the cleaned dataset into a CSV file using pandas.

Built as part of #90DaysOfCode, this project reinforces backend automation and structured data processing techniques.

---

## Technologies Used

- Python
- requests
- BeautifulSoup (bs4)
- lxml parser
- pandas

---

## Key Concepts Demonstrated

- HTTP request handling with custom headers
- HTML parsing using BeautifulSoup
- Element filtering and text extraction
- Structured data transformation
- List manipulation and ordering
- Exporting structured data to CSV format
- Backend automation scripting

---

## Workflow

1. Send HTTP request with user-agent header.
2. Parse response HTML using BeautifulSoup.
3. Extract relevant `<h2>` elements.
4. Filter only ranked movie entries.
5. Reverse list order for logical ranking.
6. Convert extracted data into a DataFrame.
7. Export results to `movies.csv`.

---

## Project Structure
```
python-web-scraping-movie-ranking/
│
├── main.py
│ └── Web scraping and CSV export logic
│
├── movies.csv
│ └── Generated output file
│
└── README.md
```
---

## Installation

```
pip install requests beautifulsoup4 lxml pandas
```
---
## Run the Script
```
python main.py
```
---
## Output

A CSV file named movies.csv containing the extracted movie rankings.

Why This Matters

Web scraping and structured data extraction are foundational skills for:

Data analysis

Automation workflows

ETL pipelines

Backend data collection systems

This project reflects practical automation use cases rather than theoretical exercises.

---
## Author

Faiz Hasan

Python Automation & Backend Developer
