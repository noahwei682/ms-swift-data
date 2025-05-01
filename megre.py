import json
import os

# List of JSON files to be merged
json_files = [
    'qwen_meta_All_Beauty_details_sftdata_att_train_1800.json',
    'qwen_meta_All_Beauty_feature_sftdata_att_train_1800.json',
    'qwen_meta_All_Beauty_main_category_sftdata_att_train_1800.json',
    'qwen_meta_All_Beauty_price_sftdata_att_train_1800.json',
    'qwen_meta_All_Beauty_Store_sftdata_att_train_1800.json',
    'qwen_meta_All_Beauty_title_sftdata_att_train_1800.json',
    'qwen_meta_Amazon_Fashion_description_sftdata_att_train_180.json',
    'qwen_meta_Amazon_Fashion_details_sftdata_att_train_1800.json',
    'qwen_meta_Amazon_Fashion_feature_sftdata_att_train_180.json',
    'qwen_meta_Amazon_Fashion_main_category_sftdata_att_train_180.json',
    'qwen_meta_Amazon_Fashion_price_sftdata_att_train_0.json',
    'qwen_meta_Amazon_Fashion_Store_sftdata_att_train_180.json',
    'qwen_meta_Amazon_Fashion_title_sftdata_att_train_180.json',
    'qwen_meta_Appliances_description_sftdata_att_train_180.json',
    'qwen_meta_Appliances_details_sftdata_att_train_1800.json',
    'qwen_meta_Appliances_feature_sftdata_att_train_180.json',
    'qwen_meta_Appliances_main_category_sftdata_att_train_180.json',
    'qwen_meta_Appliances_price_sftdata_att_train_30.json',
    'qwen_meta_Appliances_Store_sftdata_att_train_180.json',
    'qwen_meta_Appliances_title_sftdata_att_train_1800.json',
    'qwen_meta_Arts_Crafts_and_Sewing_description_sftdata_att_train_1800.json',
    'qwen_meta_Arts_Crafts_and_Sewing_details_sftdata_att_train_1800.json',
    'qwen_meta_Arts_Crafts_and_Sewing_feature_sftdata_att_train_1800.json',
    'qwen_meta_Arts_Crafts_and_Sewing_main_category_sftdata_att_train_1800.json',
    'qwen_meta_Arts_Crafts_and_Sewing_price_sftdata_att_train_1800.json',
    'qwen_meta_Arts_Crafts_and_Sewing_Store_sftdata_att_train_1800.json',
    'qwen_meta_Arts_Crafts_and_Sewing_title_sftdata_att_train_180.json',
    'qwen_meta_Automotive_description_sftdata_att_train_180.json',
    'qwen_meta_Automotive_details_sftdata_att_train_180.json',
    'qwen_meta_Automotive_feature_sftdata_att_train_180.json',
    'qwen_meta_Automotive_main_category_sftdata_att_train_180.json',
    'qwen_meta_Automotive_price_sftdata_att_train_0.json',
    'qwen_meta_Automotive_Store_sftdata_att_train_180.json',
    'qwen_meta_Automotive_title_sftdata_att_train_180.json',
    'qwen_meta_Baby_Products_description_sftdata_att_train_180.json',
    'qwen_meta_Baby_Products_details_sftdata_att_train_1800.json',
    'qwen_meta_Baby_Products_feature_sftdata_att_train_180.json',
    'qwen_meta_Baby_Products_main_category_sftdata_att_train_180.json',
    'qwen_meta_Baby_Products_price_sftdata_att_train_180.json',
    'qwen_meta_Baby_Products_Store_sftdata_att_train_180.json',
    'qwen_meta_Baby_Products_title_sftdata_att_train_1800.json',
    'qwen_meta_Video_Games_description_sftdata_att_train_180.json',
    'qwen_meta_Video_Games_details_sftdata_att_train_1800.json',
    'qwen_meta_Video_Games_feature_sftdata_att_train_180.json',
    'qwen_meta_Video_Games_main_category_sftdata_att_train_180.json',
    'qwen_meta_Video_Games_price_sftdata_att_train_30.json',
    'qwen_meta_Video_Games_Store_sftdata_att_train_180.json',
    'qwen_meta_Video_Games_title_sftdata_att_train_1800.json'
]

# Directory containing the JSON files
directory = '/home/aiscuser/lmms-eval/msdata/msdata/split/qwen_file/'

# Initialize an empty list to hold all data
merged_data = []

# Iterate through each file and append its data to the merged_data list
for file_name in json_files:
    file_path = os.path.join(directory, file_name)
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        merged_data.extend(data)

# Write the merged data to a new JSON file
output_file = os.path.join(directory, 'merged_data.json')
with open(output_file, 'w', encoding='utf-8') as file:
    json.dump(merged_data, file, ensure_ascii=False, indent=4)

print(f'Merged data written to {output_file}')
