import os
import re
from pathlib import Path
from typing import Optional, Union

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
        # Set base directory to parent of src
        self.base_dir = Path(__file__).parent.parent

    def rename_files(self, directory: Optional[Union[str, Path]] = None) -> None:
        """Rename PDF files based on their content."""
        # Convert directory to Path object
        if directory is None:
            dir_path = self.base_dir
        elif isinstance(directory, str):
            dir_path = Path(directory)
        else:
            dir_path = directory

        # Ensure directory exists
        if not dir_path.exists():
            print(f"Directory {dir_path} does not exist.")
            return

        # Scan for PDF files
        for file in os.listdir(str(dir_path)):
            if file.endswith(".pdf"):
                filepath = dir_path / file
                try:
                    # Use string path for pypdf
                    text = pypdf.PdfReader(str(filepath)).pages[0].extract_text()
                    for day_key, new_name in self.days_mapping.items():
                        if day_key in text:
                            new_filepath = dir_path / new_name
                            # Check if we would overwrite an existing file
                            if new_filepath.exists() and new_filepath != filepath:
                                print(
                                    f"Warning: {new_name} already exists. Skipping rename."
                                )
                                break

                            filepath.rename(new_filepath)
                            print(f"Renamed: {file} -> {new_name}")
                            break
                except Exception as e:
                    print(f"Error processing {file}: {e}")

    def extract_text_pdf(self, pdf_path: Union[str, Path]) -> str:
        """Extract text from PDF using pypdf."""
        try:
            # Convert to string if it's a Path
            if isinstance(pdf_path, Path):
                pdf_path_str = str(pdf_path)
            else:
                pdf_path_str = pdf_path

            # Check if file exists
            if not os.path.exists(pdf_path_str):
                print(f"PDF file not found: {pdf_path_str}")
                return ""

            text = pypdf.PdfReader(pdf_path_str).pages[0].extract_text()
            return text
        except Exception as e:
            print(f"Error extracting text from {pdf_path}: {e}")
            return ""

    def ocr_pdf_to_text(
        self, pdf_path: Union[str, Path], dpi: int = 300, lang: str = "rus"
    ) -> str:
        """Extract text from PDF using OCR."""
        try:
            # Convert to string if it's a Path
            if isinstance(pdf_path, Path):
                pdf_path_str = str(pdf_path)
            else:
                pdf_path_str = pdf_path

            # Check if file exists
            if not os.path.exists(pdf_path_str):
                print(f"PDF file not found: {pdf_path_str}")
                return ""

            pages = convert_from_path(pdf_path_str, dpi)
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
        This is a placeholder - implement actual parsing logic here.
        """
        # Look for the PDF file in the parent directory
        pdf_file = self.base_dir / f"{day}.pdf"

        if not pdf_file.exists():
            # Try with .pdf extension if not already there
            if not pdf_file.suffix:
                pdf_file = pdf_file.with_suffix(".pdf")

        if pdf_file.exists():
            try:
                # Try to extract text
                text = self.extract_text_pdf(pdf_file)
                if not text.strip():
                    text = self.ocr_pdf_to_text(pdf_file)

                # Basic parsing - find the class in the text
                lines = text.split("\n")
                schedule_lines = []
                found_class = False

                for line in lines:
                    if class_number in line.upper():
                        found_class = True
                    if found_class:
                        # Add line until we hit another class or empty line
                        if line.strip() and not any(
                            c in line.upper()
                            for c in ["А", "Б", "В", "Г"]
                            if c != class_number[-1]
                        ):
                            schedule_lines.append(line.strip())
                        elif line.strip() == "" and schedule_lines:
                            break

                if schedule_lines:
                    return f"📚 Расписание для {class_number} на {day}:\n" + "\n".join(
                        schedule_lines[:10]
                    )
                else:
                    return f"❌ Не удалось найти расписание для {class_number} на {day}"
            except Exception as e:
                return f"⚠️ Ошибка при чтении расписания: {str(e)}"
        else:
            return f"📄 Файл с расписанием на {day} не найден."
