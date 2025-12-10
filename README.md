# Flash Card Generator

A Django web application for generating flash cards from text input. The application uses an LLM (Large Language Model) to automatically create question-answer pairs from any text, making it easy to create study materials for learning.

## Features

- **Text to Flash Cards**: Simply paste or type any text, and the application will automatically generate flash cards with questions and answers
- **Interactive Learning**: View and navigate through flash cards with an intuitive interface
  - Click on a flash card to flip between question and answer
  - Navigate between cards using previous/next buttons
  - See your progress with a card counter (e.g., "3 of 10")
- **AnkiDroid Integration**: Generated flash cards are automatically saved in a format compatible with AnkiDroid
  - The file path is displayed below the flash cards for easy access
  - Import the file directly into AnkiDroid for spaced repetition learning

## How It Works

1. Enter your text in the "Input Text" field on the left side and the endpoint in "LLM Endpoint" (llama.cpp or other)
2. Click "Generate Flash Cards" (or press Enter)
3. The system processes your text and generates flash cards
4. View and learn from the flash cards on the right side
5. The flash cards are automatically saved to a file that can be imported into AnkiDroid

## Usage

### Generating Flash Cards

1. Start the Django development server:
   ```bash
   python manage.py runserver
   ```

2. Open your browser and navigate to `http://127.0.0.1:8000/`

3. Enter your text in the input field and click "Generate Flash Cards"

4. Use the navigation buttons to browse through the generated flash cards

### Importing to AnkiDroid

1. After generating flash cards, the file path will be displayed below the flash cards area
2. Copy the file path or locate the `flash_cards.txt` file in your project directory
3. Open AnkiDroid on your Android device
4. Import the file using AnkiDroid's import feature
5. The flash cards will be available for spaced repetition learning

## Configuration

The application uses environment variables for configuration:

- `FLASHCARD_LLM_ENDPOINT`: The LLM API endpoint (default: `http://127.0.0.1:8011/chat/completions`)
- `FLASHCARD_LLM_MODEL`: The model name to use
- `FLASHCARD_LLM_TIMEOUT`: Request timeout in seconds (default: `30`)

## File Format

The generated flash cards are saved in `flash_cards.txt` with the following format:
- First line: Questions separated by semicolons, each enclosed in quotes
- Second line: Answers separated by semicolons, each enclosed in quotes

This format is compatible with AnkiDroid's import functionality.

## Requirements

- Python 3.12+
- Django 5.2.8+
- requests library

## Installation

1. Create a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install django requests
   ```

3. Run migrations (if needed):
   ```bash
   python manage.py migrate
   ```

4. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Project Structure

```
django/
├── chat/              # Main application
│   ├── views.py      # View logic and LLM integration
│   ├── prompts.py    # System prompts for LLM
│   └── urls.py       # URL routing
├── flashcard/        # Django project configuration
├── templates/        # HTML templates
│   └── chat/
│       └── index.html
└── flash_cards.txt   # Generated flash cards file
```

## License

This project is open source and available for educational and personal use.

