import os
import re
from typing import Optional

import pypdf
import pytesseract
from pdf2image import convert_from_path


class PDFProcessor:
    def __init__(self, tesseract_path: str = r"/usr/bin/tesseract-ocr"):
        pytesseract.pytesseract.tesseract_cmd = tesseract_path
        self.days_mapping = {
            "ПОНЕДЕЛЬНИК": "Понедельник.pdf",
            "ВТОРНИК": "Вторник.pdf",
            "СРЕДА": "Среда.pdf",
            "ЧЕТВЕРГ": "Четверг.pdf",
            "ПЯТНИЦА": "Пятница.pdf",
            "СУББОТА": "Суббота.pdf",
        }

    def rename_files(self, directory: str = ".") -> None:
        """Rename PDF files based on their content."""
        for file in os.listdir(directory):
            if file.endswith(".pdf"):
                filepath = os.path.join(directory, file)
                try:
                    text = pypdf.PdfReader(filepath).pages[0].extract_text()
                    for day_key, new_name in self.days_mapping.items():
                        if day_key in text:
                            os.rename(filepath, os.path.join(directory, new_name))
                            break
                except Exception as e:
                    print(f"Error processing {file}: {e}")

    def extract_text_pdf(self, pdf_path: str) -> str:
        """Extract text from PDF using pypdf."""
        try:
            text = pypdf.PdfReader(pdf_path).pages[0].extract_text()
            return text
        except Exception as e:
            print(f"Error extracting text from {pdf_path}: {e}")
            return ""

    def ocr_pdf_to_text(self, pdf_path: str, dpi: int = 300, lang: str = "rus") -> str:
        """Extract text from PDF using OCR."""
        try:
            pages = convert_from_path(pdf_path, dpi)
            extracted_text = ""

            for page in pages:
                text = pytesseract.image_to_string(page, lang=lang)
                extracted_text += text + "\n"

            return extracted_text
        except Exception as e:
            print(f"Error performing OCR on {pdf_path}: {e}")
            return ""

    def sum_numbers(self, input_string: str) -> int:
        """Sum all numbers found in a string."""
        numbers_as_strings = re.findall(r"[0-9]+", input_string)
        return sum(int(num) for num in numbers_as_strings)

    def parse_schedule_text(self, class_number: str, day: str) -> str:
        """
        Parse schedule text for a specific class and day.
        Note: This is a placeholder - you'll need to implement the actual parsing logic.
        """
        # TODO: Implement actual schedule parsing logic
        return f"Расписание для {class_number} на {day}\n[Здесь будет расписание]"
