from bs4 import BeautifulSoup
import requests

# Fetch the page
page_to_scrape = requests.get("https://quotes.toscrape.com/page/2/")

# Parse the page content
soup = BeautifulSoup(page_to_scrape.text, "html.parser")

# Find all quote texts
quotes = soup.findAll("span", attrs={"class": "text"})

# Find all authors
authors = soup.findAll("small", attrs={"class": "author"})

# Check if the number of quotes matches the number of authors
if len(quotes) == len(authors):
    # Print quotes with their respective authors
    for quote, author in zip(quotes, authors):
        print(f"{quote.text} - {author.text}")
else:
    print("Mismatch between the number of quotes and authors.")
