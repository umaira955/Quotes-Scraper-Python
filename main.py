import requests
import csv
from bs4 import BeautifulSoup
with open("Quotes.csv" , "w" , newline="" , encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Quote" , "Author" , "Tags"])
    for page_num in range(1, 11):
        if page_num == 1:
            url = "https://quotes.toscrape.com/"
        else:
            url = f"https://quotes.toscrape.com/page/{page_num}"
        try:
            r = requests.get(url , timeout= 30)
            r.raise_for_status()
        except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error (4xx or 5xx): {errh}")
            continue
        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error occurred: {errt}")
            continue
        except requests.exceptions.ConnectionError as errc:
            print(f"Connection Error occurred: {errc}")
            continue
        if r.status_code == 200:
            soup = BeautifulSoup(r.content , "html.parser")
            for Quote in soup.find_all("div" , class_ = "quote"):
                Qote = Quote.find("span").get_text()
                Author = Quote.find("small" , class_ = "author").get_text()
                Tags = Quote.find("div" , class_ = "tags").find_all("a" , class_ = "tag")
                Tags = [Tag.get_text() for Tag in Tags]
                writer.writerow([Qote , Author ,  ", ".join(Tags)])
        else:
            print("Request failed!!")
print("CSV created successfully!!!")