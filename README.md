# TDnet Fiscal Report Scraper

This Python script scrapes fiscal reports of Japanese listed companies from the TDnet website for a specified date or today's date, and uploads them to a specified vector store for use by ChatGPT's assistant.

## Features

- Scrape fiscal reports for a given date or today's date.
- Upload reports to a specified vector store.
- Command-line argument for specifying the date.

## Requirements

- Required Python libraries (listed in `requirements.txt`)

## Setup

1. **Clone the repository**

    ```bash
    git clone https://github.com/koheiapril20/tdnet-vector-uploader.git
    cd tdnet-scraper
    ```

2. **Create and activate a virtual environment**

    ```bash
    python -m venv venv
    source venv/bin/activate  # macOS/Linux
    venv\Scripts\activate     # Windows
    ```

3. **Install dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Create a `.env` file in the project root**

    ```plaintext
    OPENAI_API_KEY=your_openai_api_key
    OPENAI_TARGET_VS_ID=your_target_vector_store_id
    ```

## Usage

### With a specified date

```bash
python main.py 20240620
```

### Without a specified date (defaults to today)

```bash
python main.py
```

