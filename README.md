# top_movies
This Python script scrapes movie titles from a webpage listing the best movies and prints them
# Movie Scraper 🎥

A Python script that scrapes movie titles from a webpage and displays them in reverse order. Perfect for movie enthusiasts who want to explore a curated list of the best films!

## How It Works

1. **Fetches Data**: 
   - Retrieves the webpage content using the `requests` library.

2. **Extracts Movie Titles**:
   - Parses the HTML to find all `<h2>` tags, which are assumed to contain the movie titles.

3. **Reverses the List**:
   - Displays the movies in reverse order, from the lowest-ranked to the highest-ranked.

## Requirements

- Python 3.x
- Installed libraries:
  - `requests`
  - `beautifulsoup4`

Install the required libraries using:
```bash
pip install bs4

## How to Run the Script
Clone or download the repository.
Open the script in your Python IDE or text editor.
Run the script:
```bash
python movies.py
