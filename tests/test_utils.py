import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock

# Import the class (adjust import path based on your choice above)
from src.read import PDFProcessor  # or from telegram_schedule_bot.utils import PDFProcessor

@pytest.fixture
def pdf_processor():
    """Return a PDFProcessor instance with a test base directory."""
    proc = PDFProcessor()
    # Override base_dir to a temporary directory for testing
    proc.base_dir = Path("/tmp/test_schedule")
    proc.base_dir.mkdir(exist_ok=True)
    yield proc
    # Cleanup after test
    import shutil
    shutil.rmtree(proc.base_dir, ignore_errors=True)

def test_sum_numbers(pdf_processor):
    """Test that sum_numbers correctly adds all integers in a string."""
    assert pdf_processor.sum_numbers("abc 123 def 45") == 168
    assert pdf_processor.sum_numbers("no numbers here") == 0
    assert pdf_processor.sum_numbers("1 2 3") == 6

@patch("src.utils.pypdf.PdfReader")  # adjust patch target based on actual import
def test_extract_text_pdf(mock_pdf_reader, pdf_processor):
    """Test PDF text extraction with mocked pypdf."""
    # Mock the PdfReader and its page
    mock_reader = MagicMock()
    mock_page = MagicMock()
    mock_page.extract_text.return_value = "Sample extracted text"
    mock_reader.pages = [mock_page]
    mock_pdf_reader.return_value = mock_reader

    result = pdf_processor.extract_text_pdf("dummy.pdf")
    assert result == "Sample extracted text"
    mock_pdf_reader.assert_called_once_with("dummy.pdf")

@patch("src.utils.pytesseract.image_to_string")
@patch("src.utils.convert_from_path")
def test_ocr_pdf_to_text(mock_convert, mock_image_to_string, pdf_processor):
    """Test OCR extraction with mocked pytesseract."""
    # Mock pdf2image conversion returning a list of fake images
    mock_image = MagicMock()
    mock_convert.return_value = [mock_image]
    mock_image_to_string.return_value = "OCR text line"

    result = pdf_processor.ocr_pdf_to_text("dummy.pdf")
    assert result == "OCR text line\n"  # note newline after each page
    mock_convert.assert_called_once_with("dummy.pdf", 300)
    mock_image_to_string.assert_called_once_with(mock_image, lang="rus")

def test_parse_schedule_text_no_file(pdf_processor):
    """Test parse_schedule_text when PDF file does not exist."""
    result = pdf_processor.parse_schedule_text("10А", "Понедельник")
    assert "не найден" in result

# Add more tests for rename_files, etc.
