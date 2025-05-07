import json
import os
import sys

# List of JSON files to be merged
json_files = [
    'meta_All_Beauty_dict_title_grpo.json',
    'meta_Amazon_Fashion_dict_title_grpo.json',
    'meta_Appliances_dict_title_grpo.json',
    'meta_Arts_Crafts_and_Sewing_dict_title_grpo.json',
    'meta_Automotive_dict_title_grpo.json',
    'meta_Baby_Products_dict_title_grpo.json',
    'meta_Beauty_and_Personal_Care_dict_title_grpo.json',
    'meta_Books_dict_title_grpo.json',
    'meta_CDs_and_Vinyl_dict_title_grpo.json',
    'meta_Cell_Phones_and_Accessories_dict_title_grpo.json',
    'meta_Clothing_Shoes_and_Jewelry_dict_title_grpo.json',
    'meta_Digital_Music_dict_title_grpo.json',
    'meta_Electronics_dict_title_grpo.json',
    'meta_Gift_Cards_dict_title_grpo.json',
    'meta_Grocery_and_Gourmet_Food_dict_title.json',
    'meta_Handmade_Products_dict_title_grpo.json',
    'meta_Health_and_Household_dict_title_grpo.json',
    'meta_Health_and_Personal_Care_dict_title_grpo.json',
    'meta_Home_and_Kitchen_dict_title_grpo.json',
    'meta_Industrial_and_Scientific_dict_title_grpo.json',
    'meta_Kindle_Store_dict_title_grpo.json',
    'meta_Magazine_Subscriptions_dict_title_grpo.json',
    'meta_Movies_and_TV_dict_title_grpo.json',
    'meta_Musical_Instruments_dict_title_grpo.json',
    'meta_Office_Products_dict_title_grpo.json',
    'meta_Patio_Lawn_and_Garden_dict_title_grpo.json',
    'meta_Pet_Supplies_dict_title_grpo.json',
]

# Directory containing the JSON files
directory = '/home/aiscuser/lmms-eval/llava-ov-ewc-ms/msdata/grpo_v1/'

# Initialize an empty list to hold all data
merged_data = []

# Iterate through each file and append its data to the merged_data list
for file_name in json_files:
    file_path = os.path.join(directory, file_name)
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            # Process the file as JSONL (each line is a separate JSON object)
            file_data = []
            line_count = 0
            for line in file:
                line = line.strip()
                if not line:  # Skip empty lines
                    continue
                    
                line_count += 1
                try:
                    obj = json.loads(line)
                    file_data.append(obj)
                except json.JSONDecodeError as e:
                    print(f'ERROR: Could not parse line {line_count} in {file_name}: {e}')
                    print(f'Problematic line: {line[:100]}...' if len(line) > 100 else line)
            
            print(f'Successfully loaded {len(file_data)} items from {file_name}')
            merged_data.extend(file_data)
            
    except FileNotFoundError:
        print(f'Warning: File not found: {file_path}')
        continue
    except Exception as e:
        print(f'Unexpected error with {file_name}: {e}')
        continue

if not merged_data:
    print("No data was successfully loaded. Exiting without creating output file.")
    sys.exit(1)

# Write the merged data to a new JSON file
output_file = os.path.join(directory, 'merged_data.json')
with open(output_file, 'w', encoding='utf-8') as file:
    json.dump(merged_data, file, ensure_ascii=False, indent=4)

print(f'Merged data written to {output_file}')
print(f'Total items in merged data: {len(merged_data)}')
