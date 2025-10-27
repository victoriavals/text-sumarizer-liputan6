import json
import csv
import os
from pathlib import Path

path_input = "C:\\NaufalFirdaus\\CODES\\AI\\sumarizer-ai\\liputan6_data\\canonical\\train"
path_output = "C:\\NaufalFirdaus\\CODES\\AI\\sumarizer-ai\\liputan6_train.csv"

def convert_to_text(list_of_lists):
    """Convert list of list of words to a single text string"""
    sentences = []
    for sentence in list_of_lists:
        sentences.append(' '.join(sentence))
    return ' '.join(sentences)

def process_json_files(input_folder, output_csv):
    """Process all JSON files in folder and convert to CSV"""
    data_rows = []
    
    # Get all JSON files
    json_files = list(Path(input_folder).glob("*.json"))
    print(f"Found {len(json_files)} JSON files")
    
    # Process each JSON file
    for json_file in json_files:
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
                # Convert article and summary to text
                article_text = convert_to_text(data['clean_article'])
                summary_text = convert_to_text(data['clean_summary'])
                
                # Create row
                row = {
                    'id': data['id'],
                    'url': data['url'],
                    'article': article_text,
                    'summary': summary_text,
                    'extractive_summary': str(data['extractive_summary'])
                }
                data_rows.append(row)
                
        except Exception as e:
            print(f"Error processing {json_file}: {e}")
    
    # Write to CSV
    if data_rows:
        fieldnames = ['id', 'url', 'article', 'summary', 'extractive_summary']
        with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data_rows)
        
        print(f"\nSuccessfully converted {len(data_rows)} files to {output_csv}")
    else:
        print("No data to write!")

if __name__ == "__main__":
    process_json_files(path_input, path_output)