import re
import csv
import argparse

def extract_pdf_links(markdown_content):
    # Regular expression to find links ending with .pdf
    pdf_pattern = r'\[.*?\]\((.*?\.pdf)\)'
    pdf_links = re.findall(pdf_pattern, markdown_content)
    return pdf_links

def save_to_csv(pdf_links, output_file):
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['PDF Links'])  # Header
        for link in pdf_links:
            writer.writerow([link])

def main():
    parser = argparse.ArgumentParser(description='Extract PDF links from a markdown file and save to CSV.')
    parser.add_argument('input_file', help='Path to the input markdown file')
    parser.add_argument('output_file', help='Path to the output CSV file')
    args = parser.parse_args()

    try:
        with open(args.input_file, 'r', encoding='utf-8') as file:
            markdown_content = file.read()

        pdf_links = extract_pdf_links(markdown_content)
        save_to_csv(pdf_links, args.output_file)

        print(f"Successfully extracted {len(pdf_links)} PDF links and saved to {args.output_file}")

    except FileNotFoundError:
        print(f"Error: The file {args.input_file} was not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()