# BookBot

BookBot is a small command-line program that analyzes a text file. It reports the total word count and lists each letter found in the text, ordered from most frequent to least frequent.

## Requirements

- Python 3

BookBot uses only the Python standard library; no additional packages are required.

## Usage

From the project directory, pass the path to a text file:

```bash
python3 main.py books/frankenstein.txt
```

The report includes the file path, total number of words, and counts for each letter. Letter counts are case-insensitive and include alphabetic characters only.

You can also analyze your own text file:

```bash
python3 main.py path/to/your-book.txt
```

If you omit the file path, BookBot prints a usage message.

## Project files

- `main.py` — command-line entry point and report formatting
- `stats.py` — text loading, word counting, and letter frequency functions
- `books/` — sample books for analysis
