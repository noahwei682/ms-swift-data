import json
import glob
import os

def merge_json_files():
    # Get all JSON files in the current directory
    json_files = glob.glob('/home/aiscuser/lmms-eval/llava-ov-ewc-ms/msdata/split_small_small_qwen/qwen_*.json')
    
    # Initialize an empty list to store all data
    all_data = []
    
    # Process each JSON file
    for file_path in json_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if isinstance(data, list):
                    all_data.extend(data)
                else:
                    print(f"Warning: {file_path} does not contain a JSON list")
        except Exception as e:
            print(f"Error processing {file_path}: {str(e)}")
    
    # Write the merged data to a new file
    output_file = '/home/aiscuser/lmms-eval/llava-ov-ewc-ms/msdata/split_small_small_qwen/merged_data.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_data, f, ensure_ascii=False, indent=2)
    
    print(f"Successfully merged {len(json_files)} files into {output_file}")
    print(f"Total number of items in merged file: {len(all_data)}")

if __name__ == "__main__":
    merge_json_files() 
