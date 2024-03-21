import requests
import selectorlib


URL = "https://programmer100.pythonanywhere.com/tours/"


def scrape(url):
    """scrape the page source from URL"""
    response = requests.get(url)
    source = response.text
    return source


if __name__ == "__main__":
   print(scrape(URL))
