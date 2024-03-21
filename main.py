from function import scrape, extract


URL = "https://programmer100.pythonanywhere.com/tours/"


if __name__ == "__main__":
    scraped = scrape(URL)
    extracted = extract(scraped)
    print(extracted)
