import os
import argparse
from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            reader = PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"
        return text
    except Exception as e:
        print(f"Error extracting text from {pdf_path}: {e}")
        return None

def sanitize_filename(filename):
    return "".join([c for c in filename if c.isalpha() or c.isdigit() or c in (' ', '-', '_')]).rstrip()

def main():
    parser = argparse.ArgumentParser(description='Extract text from PDFs in a folder and save as .txt files.')
    parser.add_argument('input_dir', help='Directory containing the PDF files')
    parser.add_argument('output_dir', help='Directory to save the extracted text files')
    args = parser.parse_args()

    # Ensure output directory exists
    os.makedirs(args.output_dir, exist_ok=True)

    # Process all PDF files in the input directory
    for filename in os.listdir(args.input_dir):
        if filename.lower().endswith('.pdf'):
            pdf_path = os.path.join(args.input_dir, filename)
            print(f"Processing: {pdf_path}")
            
            text_content = extract_text_from_pdf(pdf_path)
            if text_content:
                # Create a sanitized filename for the output .txt file
                txt_filename = sanitize_filename(os.path.splitext(filename)[0]) + ".txt"
                output_path = os.path.join(args.output_dir, txt_filename)
                
                # Write the extracted text to a .txt file
                with open(output_path, 'w', encoding='utf-8') as txtfile:
                    txtfile.write(text_content)
                print(f"Saved: {output_path}")
            else:
                print(f"Failed to extract text from {pdf_path}")

if __name__ == "__main__":
    main()