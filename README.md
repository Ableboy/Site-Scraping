# News Site Scraping

## Description

This project extracts news articles from various websites for analysis or aggregation, storing the data in a structured format.

## Libraries Used

- Requests
- BeautifulSoup
- pprint

# Key Features

- Scrape headlines, articles, author names, and publication dates from multiple pages.
- Store the data in a structured format (CSV, JSON, database).
- Handle pagination and dynamic content loading.
- Filter and sort articles based on specific criteria (e.g., votes, points).

## Use Case

Creates a centralized repository of news articles for research, analysis, or personal use.

## Installation
``` bash
# Clone the repository
git clone https://github.com/Ableboy/Site-Scraping.git

# Navigate into the project directory
cd Site-Scraping

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt
```

## Usage
Open a terminal and navigate to the project directory.
Run the script to scrape news articles:

```bash
python scrape_news.py
```

The script will scrape the news site, process the data, and print the top articles with more than 100 points.

## Contributing

We welcome contributions! If you would like to contribute to this project, please follow these steps:

1. Fork the Repository: Click the "Fork" button at the top right of this repository's page on GitHub.

2. Clone Your Fork: Clone your forked repository to your local machine using:
```bash
git clone https://github.com/Ableboy/Site-Scraping.git
```

3. Create a Branch: Create a new branch for your feature or bug fix:
```bash
git checkout -b feature-name
```

4. Make Your Changes: Make your changes in the code.

5. Commit Your Changes: Commit your changes with a clear message:
```bash
git commit -m 'Add new feature'
```

6. Push to Your Fork: Push your changes to your forked repository:
```bash
git push origin feature-name
```

7. Create a Pull Request: Open a pull request on the original repository, describing your changes.


## License
MIT License

