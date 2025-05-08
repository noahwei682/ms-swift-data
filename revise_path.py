#!/usr/bin/env python3
import json
import os

def process_merged_data(file_path='/cpfs01/shared/llm_ddd/zhangyulong/sa_work/msdata/wei682/amazon-qwen-file/merged_data.json'):
    """
    Read and process the merged_data.json file.
    
    Args:
        file_path (str): Path to the merged_data.json file
    """
    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return
    
    # Read the JSON file
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError:
        print(f"Error: '{file_path}' contains invalid JSON.")
        return
    except Exception as e:
        print(f"Error reading file: {e}")
        return
    
    # Print the number of records in the file
    print(f"Successfully loaded {len(data)} records from {file_path}")
    
    # Update image paths
    old_prefix = "/home/aiscuser/lmms-eval/llava-ov-ewc-ms/msdata/images/images/"
    new_prefix = "/cpfs01/shared/llm_ddd/zhangyulong/sa_work/msdata/images/images/"
    
    updated_count = 0
    for item in data:
        if "image_path" in item and item["image_path"].startswith(old_prefix):
            item["image_path"] = item["image_path"].replace(old_prefix, new_prefix)
            updated_count += 1
    
    print(f"\nUpdated {updated_count} image paths from '{old_prefix}' to '{new_prefix}'")
    
    # Save the updated data to a new file
    output_file = '/cpfs01/shared/llm_ddd/zhangyulong/sa_work/msdata/wei682/amazon-qwen-file/updated_merged_data.json'   
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    
    print(f"Saved updated data to {output_file}")
    
    # Print sample of the data structure
    if data:
        print("\nSample data structure:")
        for key in data[0].keys():
            print(f"- {key}")
    
    # Analyze records
    print("\nData analysis:")
    
    # Count records with and without solutions
    with_solution = sum(1 for item in data if "solution" in item and item["solution"])
    print(f"Records with solution: {with_solution}")
    print(f"Records without solution: {len(data) - with_solution}")
    
    # Print first few titles
    print("\nSample titles:")
    for i, item in enumerate(data[:5]):  # First 5 records
        original_answer = item.get("original_answer", "N/A")
        print(f"{i+1}. {original_answer.strip()}")
    
    return data

if __name__ == "__main__":
    # Process the merged data file
    data = process_merged_data()
    
    # Additional processing could be added here
    print("\nScript completed successfully.") 
