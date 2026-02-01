import os
import sys
from pathlib import Path
from typing import List

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from read import PDFProcessor


class ScheduleParser:
    def __init__(self, base_url: str = "https://sortavala-school1.ru/life/schedule1/"):
        self.base_url = base_url
        self.pdf_processor = PDFProcessor()
        # Set download directory to parent of src
        self.download_dir = Path(__file__).parent.parent

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
                    full_url = f"https://sortavala-school1.ru{href}"
                    url_list.append(full_url)

            print(f"Found {len(url_list)} schedule files")
        except Exception as e:
            print(f"Error parsing URLs: {e}")
        finally:
            browser.quit()

        return url_list

    def download_files(self, url_list: List[str], download_dir: Path = None) -> None:
        """Download files from URLs."""
        if download_dir is None:
            download_dir = self.download_dir

        if not download_dir.exists():
            download_dir.mkdir(parents=True)

        downloaded_files = []
        for url in url_list:
            try:
                response = requests.get(url, timeout=30)
                response.raise_for_status()

                filename = url.split("/")[-1]
                if not filename.lower().endswith(".pdf"):
                    filename += ".pdf"

                filepath = download_dir / filename

                with open(filepath, "wb") as file:
                    file.write(response.content)

                downloaded_files.append(filename)
                print(f"✅ Downloaded: {filename}")
            except Exception as e:
                print(f"❌ Error downloading {url}: {e}")

        # Rename files after downloading - pass Path object as string
        if downloaded_files:
            print("Renaming files based on content...")
            self.pdf_processor.rename_files(str(download_dir))
        else:
            print("No files were downloaded.")

    def parse_and_download(self) -> List[str]:
        """Parse URLs and download files in one operation."""
        print("Starting schedule parsing...")
        url_list = self.parse_urls()

        if url_list:
            self.download_files(url_list)
            return url_list
        else:
            print("No URLs found to download.")
            return []


def main():
    """Command-line entry point for schedule parser."""
    parser = ScheduleParser()
    parser.parse_and_download()
