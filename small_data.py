import json
import os
import shutil
from pathlib import Path

def process_json_file(input_file, output_dir):
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    data_list = []
    try:
        # Read the file line by line
        with open(input_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line:  # Skip empty lines
                    try:
                        json_obj = json.loads(line)
                        data_list.append(json_obj)
                    except json.JSONDecodeError as e:
                        print(f"Warning: Skipping invalid JSON line in {input_file}: {str(e)}")
                        continue
    except Exception as e:
        print(f"Error reading file {input_file}: {str(e)}")
        return
    
    if not data_list:
        print(f"Warning: No valid JSON data found in {input_file}. Skipping...")
        return
    
    # Process the data based on length
    if len(data_list) > 6000:
        data_list = data_list[:6000]
        print(f"Truncated {input_file} from {len(data_list)} to 6000 items")
    else:
        print(f"Keeping {input_file} as is with {len(data_list)} items")
    
    # Create output file path
    output_file = os.path.join(output_dir, os.path.basename(input_file))
    
    # Write the processed data
    with open(output_file, 'w', encoding='utf-8') as f:
        for item in data_list:
            f.write(json.dumps(item, ensure_ascii=False) + '\n')
    
    print(f"Processed {input_file} -> {output_file}")

def main():
    # Input directory (current directory)
    input_dir = "."
    
    # Output directory
    output_dir = "/home/aiscuser/grpo_data/small"
    
    # Process all JSON files in the current directory
    for file in os.listdir(input_dir):
        if file.endswith('.json'):
            input_file = os.path.join(input_dir, file)
            process_json_file(input_file, output_dir)

if __name__ == "__main__":
    main() 
