from function import scrape, extract, send_email, store


URL = "https://programmer100.pythonanywhere.com/tours/"


if __name__ == "__main__":
    scraped = scrape(URL)
    extracted = extract(scraped)
    print(extracted)
    store(extracted)
    if extracted != "No upcoming tours":
        if extracted not in "data.txt":
            send_email()
