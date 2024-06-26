from function import scrape, extract, send_email, store, read
import time

URL = "https://programmer100.pythonanywhere.com/tours/"


if __name__ == "__main__":
    while True:
        scraped = scrape(URL)
        extracted = extract(scraped)
        print(extracted)
        content = read(extracted)
        if extracted != "No upcoming tours":
            if extracted not in content:
                store(extracted)
                send_email(message="Hey Ed new event was found")
        time.sleep(3)
