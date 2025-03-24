import requests
from bs4 import BeautifulSoup
import pandas as pd

# Initialize lists to store authors and quotes
authors = []
quotes = []

# Iterate over all pages of the website
for page in range(1, 11):  # The website has 10 pages
    url = f"https://quotes.toscrape.com/page/{page}/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find all quote containers
    quote_divs = soup.find_all("div", class_="quote")
    
    for quote_div in quote_divs:
        text = quote_div.find("span", class_="text").get_text(strip=True)
        author = quote_div.find("small", class_="author").get_text(strip=True)
        
        quotes.append(text)
        authors.append(author)

# Create a DataFrame from the lists
df = pd.DataFrame({
    "Author": authors,
    "Quote": quotes
})

# Save the DataFrame as CSV (UTF-8 encoding for compatibility)
df.to_csv("quotes.csv", index=False, encoding="utf-8-sig")

print("✅ Successfully saved as quotes.csv!")

