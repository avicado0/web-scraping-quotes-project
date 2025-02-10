# Project Title: Project Title: Web Scraping and Data Analysis - Quotes Data Extraction

## Description
This project focuses on extracting structured data (quotes, authors, and tags) from the Quotes to Scrape website using Python. The scraped data is cleaned, preprocessed, and analyzed to identify trends in tag usage. The project demonstrates skills in web scraping, data manipulation, and visualization.

## Technologies Used
- Python → Core programming language
- BeautifulSoup → Parsing and extracting HTML content
- Requests → Fetching web pages
- Pandas → Data cleaning and preprocessing
- Matplotlib → Visualizing tag frequencies

## Prerequisites
- Python 3.8 or above.
- Dependencies listed in `requirements.txt`.

## Installation
```bash
# Clone this repository
git clone https://github.com/avicado0/web-scraping-quotes-project

# Navigate to the project directory
cd <repository-name>

```
## How to Run the Project

#### Install Dependencies
Ensure Python and required libraries are installed:
```bash
pip install -r requirements.txt
```
#### Scrape Data
Run the following script to extract quotes, authors, and tags from the website:
```bash
python web_scraper.py
```
- This will generate a CSV file (quotes_data.csv) containing the scraped data.

#### Analyze and Visualize Data
The script automatically analyzes the data and generates a bar chart showing the top 10 most frequent tags. To view the visualization:
```bash
python web_scraper.py
```
- A bar chart will pop up displaying the tag frequencies.

## Project Output
- CSV File : Contains structured data with columns for quotes, authors, and tags.
- Visualization : A bar chart showing the top 10 most frequent tags.
- Insights : Identifies trends in tag usage, providing actionable insights into the dataset.