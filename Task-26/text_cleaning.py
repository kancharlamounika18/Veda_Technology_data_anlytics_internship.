"""Text Cleaning Basics — Veda Technology Data Analytics Internship.

Run from this project directory:
    python text_cleaning.py
"""
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "customer_dataset.csv"
OUTPUT_FILE = BASE_DIR / "cleaned_customer_dataset.csv"


def clean_spaces(value):
    """Remove leading/trailing whitespace and collapse repeated spaces."""
    return " ".join(str(value).strip().split())


def clean_name(value):
    return clean_spaces(value).title()


def clean_email(value):
    return clean_spaces(value).lower().replace(" ", "")


def clean_city(value):
    return clean_spaces(value).title()


def clean_phone(value):
    return "".join(character for character in str(value) if character.isdigit())


def clean_customer_data(input_file=INPUT_FILE, output_file=OUTPUT_FILE):
    data = pd.read_csv(input_file, dtype=str).fillna("")
    data["customer_name"] = data["customer_name"].map(clean_name)
    data["email"] = data["email"].map(clean_email)
    data["city"] = data["city"].map(clean_city)
    data["phone"] = data["phone"].map(clean_phone)
    data.to_csv(output_file, index=False)
    return data


if __name__ == "__main__":
    cleaned_data = clean_customer_data()
    print(f"Cleaned {len(cleaned_data)} customer records.")
    print(f"Saved cleaned file to: {OUTPUT_FILE}")
