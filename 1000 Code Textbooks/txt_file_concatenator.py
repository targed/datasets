import os
import argparse

def concatenate_txt_files(input_dir, output_file):
    # Get all .txt files in the input directory
    txt_files = [f for f in os.listdir(input_dir) if f.endswith('.txt')]
    
    # Sort the files to ensure consistent order
    txt_files.sort()
    
    # Open the output file in write mode
    with open(output_file, 'w', encoding='utf-8') as outfile:
        # Iterate through each .txt file
        for filename in txt_files:
            filepath = os.path.join(input_dir, filename)
            
            # Write the filename as a header
            outfile.write(f"\n\n--- {filename} ---\n\n")
            
            # Open each file and append its content to the output file
            with open(filepath, 'r', encoding='utf-8') as infile:
                outfile.write(infile.read())
            
            # Add a separator between files
            outfile.write("\n\n" + "="*50 + "\n\n")

def main():
    parser = argparse.ArgumentParser(description='Concatenate all .txt files in a directory into one file.')
    parser.add_argument('input_dir', help='Directory containing the .txt files')
    parser.add_argument('output_file', help='Path to the output concatenated file')
    args = parser.parse_args()

    try:
        concatenate_txt_files(args.input_dir, args.output_file)
        print(f"Successfully concatenated all .txt files from {args.input_dir} into {args.output_file}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()