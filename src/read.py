from os import listdir, rename

import pypdf


def rename_files():
    for file in listdir():
        if file.endswith(".pdf"):
            text = pypdf.PdfReader(file).pages[0].extract_text()
            if text.find("ПОНЕДЕЛЬНИК") != -1:
                rename(file, "monday.pdf")
            if text.find("ВТОРНИК") != -1:
                rename(file, "tuesday.pdf")
            if text.find("СРЕДА") != -1:
                rename(file, "wednesday.pdf")
            if text.find("ЧЕТВЕРГ") != -1:
                rename(file, "thursday.pdf")
            if text.find("ПЯТНИЦА") != -1:
                rename(file, "friday.pdf")
            if text.find("СУББОТА") != -1:
                rename(file, "saturday.pdf")


def print_files():
    for file in listdir():
        if file.endswith(".pdf"):
            text = pypdf.PdfReader(file).pages[0].extract_text()
            if text.find("ПОНЕДЕЛЬНИК") != -1:
                text.find("\n")


print_files()
