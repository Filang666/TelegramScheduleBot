from typing import List

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from read import PDFProcessor


class ScheduleParser:
    def __init__(self, base_url: str = "https://sortavala-school1.ru/life/schedule1/"):
        self.base_url = base_url
        self.pdf_processor = PDFProcessor()

    def parse_urls(self) -> List[str]:
        """Parse URLs from the schedule page."""
        url_list = []

        # Use headless mode for better performance
        options = Options()
        options.add_argument("--headless")

        browser = webdriver.Firefox(options=options)
        try:
            browser.get(self.base_url)
            soup = BeautifulSoup(browser.page_source, "html.parser")

            all_publications = soup.find_all(
                "a", class_="mr-1 sf-link sf-link-theme sf-link-dashed"
            )

            for article in all_publications:
                href = article.get("href", "")
                if href:
                    url_list.append(f"https://sortavala-school1.ru{href}")
        finally:
            browser.quit()

        return url_list

    def download_files(self, url_list: List[str], download_dir: str = ".") -> None:
        """Download files from URLs."""
        for url in url_list:
            try:
                response = requests.get(url, timeout=10)
                response.raise_for_status()

                filename = url.split("/")[-1]
                filepath = f"{download_dir}/{filename}"

                with open(filepath, "wb") as file:
                    file.write(response.content)

                print(f"Downloaded: {filename}")
            except Exception as e:
                print(f"Error downloading {url}: {e}")

        # Rename files after downloading
        self.pdf_processor.rename_files(download_dir)

    def parse_and_download(self) -> None:
        """Parse URLs and download files in one operation."""
        url_list = self.parse_urls()
        if url_list:
            self.download_files(url_list)
        else:
            print("No URLs found to download.")
