import csv
import requests
import os
from PyPDF2 import PdfReader
import io
import argparse

def download_pdf(url, timeout=30):
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        return io.BytesIO(response.content)
    except requests.RequestException as e:
        print(f"Error downloading {url}: {e}")
        return None

def extract_text_from_pdf(pdf_file):
    try:
        reader = PdfReader(pdf_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text
    except Exception as e:
        print(f"Error extracting text: {e}")
        return None

def sanitize_filename(filename):
    return "".join([c for c in filename if c.isalpha() or c.isdigit() or c in (' ', '-', '_')]).rstrip()

def main():
    parser = argparse.ArgumentParser(description='Download PDFs from CSV and extract text.')
    parser.add_argument('input_csv', help='Path to the input CSV file containing PDF links')
    parser.add_argument('output_dir', help='Directory to save the extracted text files')
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)

    with open(args.input_csv, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None)  # Skip the header row
        for row in reader:
            if row:  # Check if the row is not empty
                pdf_url = row[0]
                print(f"Processing: {pdf_url}")
                
                pdf_content = download_pdf(pdf_url)
                if pdf_content:
                    text_content = extract_text_from_pdf(pdf_content)
                    if text_content:
                        filename = sanitize_filename(os.path.basename(pdf_url))
                        output_path = os.path.join(args.output_dir, f"{filename}.txt")
                        with open(output_path, 'w', encoding='utf-8') as txtfile:
                            txtfile.write(text_content)
                        print(f"Saved: {output_path}")
                    else:
                        print(f"Failed to extract text from {pdf_url}")
                else:
                    print(f"Failed to download {pdf_url}")

if __name__ == "__main__":
    main()