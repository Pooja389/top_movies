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
pip install requests beautifulsoup4
```

## How to Run the Script

1. Clone or download the repository.
2. Open the script in your Python IDE or text editor.
3. Run the script:
   ```bash
   python movie_scraper.py
   ```

## Notes

- The script currently scrapes movies from [Empire's Best Movies List](https://www.empireonline.com/movies/features/best-movies-2/).
- Ensure the webpage structure hasn't changed, as the script relies on specific HTML tags (`<h2>`) to extract titles.

## License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute this project as per the license terms.

## Disclaimer
Web scraping terms and conditions of the source website should be reviewed and respected. Ensure your usage complies with their policies.

