import pytest
from unittest.mock import patch, MagicMock
from bot.utils import extract_text_from_pdf, ocr_image

def test_extract_text_from_pdf():
    """Test PDF text extraction with mocked PyPDF."""
    mock_pdf_reader = MagicMock()
    mock_page = MagicMock()
    mock_page.extract_text.return_value = "Sample text"
    mock_pdf_reader.pages = [mock_page]

    with patch('bot.utils.PdfReader', return_value=mock_pdf_reader):
        result = extract_text_from_pdf("dummy_path")
        assert result == "Sample text"

@pytest.mark.asyncio
async def test_ocr_image():
    """Test OCR with mocked pytesseract."""
    mock_image = MagicMock()
    with patch('bot.utils.pytesseract.image_to_string', return_value="OCR result") as mock_ocr:
        result = await ocr_image(mock_image)  # if async
        assert result == "OCR result"
        mock_ocr.assert_called_once_with(mock_image)
