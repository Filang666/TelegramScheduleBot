import requests
from bs4 import BeautifulSoup
from selenium import webdriver as wd

from read import rename_files

url_list = []


def parse_url(url_list=[]):
    browser = wd.Firefox()
    browser.get("https://sortavala-school1.ru/life/schedule1/")
    soup = BeautifulSoup(browser.page_source, "html.parser")
    all_publications = soup.find_all(
        "a", class_="mr-1 sf-link sf-link-theme sf-link-dashed"
    )
    for article in all_publications:
        url_list.append("https://sortavala-school1.ru" + str(article["href"]))
    browser.quit()
    return url_list


def download_files(url_list):
    for url in url_list:
        response = requests.get(url)
        with open(f"{url.split('/')[-1]}", "wb") as file:
            file.write(response.content)
            rename_files()
