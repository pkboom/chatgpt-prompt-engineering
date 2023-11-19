import requests
from bs4 import BeautifulSoup
import csv

# Define the target URL
url = "https://www.goodreads.com/list/show/18816.Books_You_Must_Read_"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

    book_selector = "a.bookTitle span"
    auth_selector = "span[itemprop='author']"

    # Find all book names and author names using CSS selectors
    book_names = soup.select(book_selector)
    auth_names = soup.select(auth_selector)

    # Create a list to store the scraped data
    book_data = []

    # Loop through the book names and author names and store them in the list
    for book_name, author_name in zip(book_names, auth_names):
        book_name_text = book_name.get_text(strip=True)
        auth_name_text = auth_name.get_text(strip=True)

        book_data.append([book_name_text, auth_name_text])

    # Define the CSV file name
    csv_filename = "book_list.csv"

    # Write the data to a CSV file
    with open(csv_filename, "w", newline="", encoding="utf-8") as csv_file:
        csv_writer = csv.writer(csv_file)

        # Write the header row
        csv_writer.writerow(["Book Name", "Author Name"])

        # Write the book data
        csv_writer.writerows(book_data)

    print(f"Data has been scraped and saved to {csv_filename}")

else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
