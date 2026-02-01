import os
import re
from collections import deque
from os import listdir, rename
from posixpath import pardir
from random import shuffle

import pypdf
import pytesseract
from pdf2image import convert_from_path
from typing_extensions import List

pytesseract.pytesseract.tesseract_cmd = r"/usr/bin/tesseract-ocr"


def rename_files():
    for file in listdir():
        if file.endswith(".pdf"):
            text = pypdf.PdfReader(file).pages[0].extract_text()
            if text.find("ПОНЕДЕЛЬНИК") != -1:
                rename(file, "Понедельник.pdf")
            if text.find("ВТОРНИК") != -1:
                rename(file, "Вторник.pdf")
            if text.find("СРЕДА") != -1:
                rename(file, "Среда.pdf")
            if text.find("ЧЕТВЕРГ") != -1:
                rename(file, "Четверг.pdf")
            if text.find("ПЯТНИЦА") != -1:
                rename(file, "Пятница.pdf")
            if text.find("СУББОТА") != -1:
                rename(file, "Суббота.pdf")


def extract_text_pdf(pdf_path):
    text = pypdf.PdfReader(pdf_path).pages[0].extract_text()
    return text


def ocr_pdf_to_text(pdf_path):
    pages = convert_from_path(pdf_path, 300)

    extracted_text = ""
    for page_num, page in enumerate(pages):
        text = pytesseract.image_to_string(page, lang="rus")
        extracted_text += text

    return extracted_text


def sum_numbers(input_string):
    numbers_as_strings = re.findall(r"[0-9]+", input_string)

    total_sum = sum(int(num) for num in numbers_as_strings)
    return total_sum


# im tired i dont know how to solve this problem i tryed ocr pdf extract text but this schedule soooo broken machine cant solve this
