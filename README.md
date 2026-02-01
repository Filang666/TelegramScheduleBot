# Telegram Schedule Bot

A Telegram bot for managing and distributing school schedules. The bot automatically downloads schedule PDFs from a school website, processes them, and provides schedule information to users via Telegram.

## Features

- 📅 Automatic schedule downloading from school website
- 🔍 PDF processing with OCR support
- 🤖 Interactive Telegram interface
- 👨‍💼 Admin panel for bot management
- 📊 Class and day-based schedule lookup
- 🚀 Easy deployment and configuration

## Installation

### From Source

1. Clone the repository:
```bash
git clone https://github.com/Filang666/telegram-schedule-bot.git
cd telegram-schedule-bot

    Install dependencies:

bash

pip install -e .[dev]  # For development
# or
pip install -e .       # For basic installation

    Configure the bot:

bash

cp .env.example .env
# Edit .env with your bot token and admin IDs

Configuration

Create a .env file in the project root:
env

TOKEN=your_telegram_bot_token_here
ADMINS=123456789,987654321  # Telegram user IDs of admins

Usage
Running the bot:
bash

# Using the installed script
schedule-bot

# Or from source
python -m src.aiogram_run

Parsing schedules manually:
bash

schedule-parser

Project Structure
text

telegram-schedule-bot/
├── .env                    # Environment variables
├── setup.py               # Package setup
├── requirements.txt       # Dependencies
├── README.md             # This file
├── LICENSE               # MIT License
└── src/                  # Source code
    ├── __init__.py       # Package initialization
    ├── create_bot.py     # Bot configuration
    ├── keyboards/
    │   └── keyboard.py   # Keyboard layouts
    ├── handlers/
    │   └── start.py      # Command handlers
    ├── read.py           # PDF processing
    ├── parsing.py        # Web parsing
    ├── filters/
    │   └── filters.py    # Admin filters
    └── aiogram_run.py    # Bot application runner

Development
Installing development dependencies:
bash

pip install -e .[dev]

Code formatting:
bash

black src/
isort src/
flake8 src/

Requirements

    Python 3.9+

    Tesseract OCR (for PDF text extraction)

    Firefox/GeckoDriver (for web scraping)

    Telegram Bot API token

License

MIT License - see LICENSE file for details.
Author

.nixnix - timurovichroman@gmail.com
Repository

https://github.com/Filang666/telegram-schedule-bot
text


## **Installation:**

1. **Install the package in development mode:**
```bash
pip install -e .

    Run the bot:

bash

schedule-bot

    Parse schedules:

bash

schedule-parser
