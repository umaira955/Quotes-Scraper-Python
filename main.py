import requests
import csv
from bs4 import BeautifulSoup
seen_quotes = set()

with open("Quotes.csv" , "w" , newline="" , encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Quote" , "Author" , "Tags"])
    count = 0
    url = "https://quotes.toscrape.com/"       
    while url:
        try:
            r = requests.get(url , timeout= 30)
            r.raise_for_status()
        except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error (4xx or 5xx): {errh}")
            break
        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error occurred: {errt}")
            break
        except requests.exceptions.ConnectionError as errc:
            print(f"Connection Error occurred: {errc}")
            break
        soup = BeautifulSoup(r.content , "html.parser")
        for Quote in soup.find_all("div" , class_ = "quote"):
            Quote_tag = Quote.find("span", class_="text")
            Quote_text = Quote_tag.get_text(strip=True) if Quote_tag else None
            Author_tag = Quote.find("small", class_="author")
            Author = Author_tag.get_text(strip=True) if Author_tag else None
            Tags_tag = Quote.find("div", class_="tags")
            Tags = Tags_tag.find_all("a", class_="tag") if Tags_tag else []
            Tags = [Tag.get_text(strip=True) for Tag in Tags]
            if Quote_text not in seen_quotes:
                writer.writerow([Quote_text , Author ,  ", ".join(Tags)])
                seen_quotes.add(Quote_text)
                count += 1
            else:
                continue
        next_page = soup.find("li", class_="next")
        if next_page:
            url = "https://quotes.toscrape.com" + next_page.find("a")["href"]
        else:
            url = None
print(f"Total Quotes = {count}")

import csv

with open("Quotes.csv", mode="r", encoding="utf-8") as file:
    reader = csv.reader(file)
    header = next(reader)

    print(f"Headers: {header}")

    total_rows = 0
    invalid_rows = 0
    quotes = set()

    for row in reader:
        total_rows += 1

        if len(row) != 3:
            invalid_rows += 1

        quotes.add(row[0])

    print(f"Total data rows: {total_rows}")
    print(f"Unique quotes: {len(quotes)}")
    print(f"Invalid rows: {invalid_rows}")
