# Install dependencies

conda install request bs4

# Prompt

```
Code a web scraper in Python using the BeautifulSoup library.

Target Website: https://www.goodreads.com/list/show/18816.Books_You_Must_Read_

Goal: Scrape the names of all the books and their authors from the target page.

Here are the CSS selectors of the data needed:

1. Book Name:#all_votes > table > tbody > tr:nth-child(1) > td:nth-child(3) > a > span

2. Author Name: #all_votes > table > tbody > tr:nth-child(1) > td:nth-child(3) > span:nth-child(4) > div > a > span

Final Output: Save all the Book Names and Author Names in a CSV file.

Additional Instructions: Handle character encoding and remove undesirable symbols in the output CSV.
```
