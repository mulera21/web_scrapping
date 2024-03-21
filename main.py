from function import scrape, extract, send_email


URL = "https://programmer100.pythonanywhere.com/tours/"


if __name__ == "__main__":
    scraped = scrape(URL)
    extracted = extract(scraped)
    print(extracted)
    if extracted != "No upcoming tours":
        send_email()
