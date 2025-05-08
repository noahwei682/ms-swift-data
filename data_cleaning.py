import os
import json

def get_jpg_filenames(folder_path):
    jpg_filenames = set()  # 使用集合来存储文件名（不带扩展名）
    
    # 遍历文件夹
    for filename in os.listdir(folder_path):
        if filename.endswith('.jpg'):
            # 去掉扩展名
            name_without_extension = os.path.splitext(filename)[0]
            jpg_filenames.add(name_without_extension)

    return jpg_filenames

if __name__ == "__main__":
    folder_paths = [
        '/home/aiscuser/lmms-eval/llava-ov-ewc-ms/msdata/images/images/',
    ]

    file_paths = [      
        "meta_All_Beauty_dict_title_grpo.json",
        "meta_Amazon_Fashion_dict_title_grpo.json",
        "meta_Appliances_dict_title_grpo.json",
        "meta_Arts_Crafts_and_Sewing_dict_title_grpo.json",
        "meta_Automotive_dict_title_grpo.json",
        "meta_Baby_Products_dict_title_grpo.json",
        "meta_Beauty_and_Personal_Care_dict_title_grpo.json",
        "meta_Books_dict_title_grpo.json",
        "meta_CDs_and_Vinyl_dict_title_grpo.json",
        "meta_Cell_Phones_and_Accessories_dict_title_grpo.json",
        "meta_Clothing_Shoes_and_Jewelry_dict_title_grpo.json",
        "meta_Digital_Music_dict_title_grpo.json",
        "meta_Electronics_dict_title_grpo.json",
        "meta_Gift_Cards_dict_title_grpo.json",
        "meta_Grocery_and_Gourmet_Food_dict_title.json",
        "meta_Handmade_Products_dict_title_grpo.json",
        "meta_Health_and_Household_dict_title_grpo.json",
        "meta_Health_and_Personal_Care_dict_title_grpo.json",
        "meta_Home_and_Kitchen_dict_title_grpo.json",
        "meta_Industrial_and_Scientific_dict_title_grpo.json",
        "meta_Kindle_Store_dict_title_grpo.json",
        "meta_Magazine_Subscriptions_dict_title_grpo.json",
        "meta_Movies_and_TV_dict_title_grpo.json",
        "meta_Musical_Instruments_dict_title_grpo.json",
        "meta_Office_Products_dict_title_grpo.json",
        "meta_Patio_Lawn_and_Garden_dict_title_grpo.json",
        "meta_Pet_Supplies_dict_title_grpo.json",
    ]

    for index in range(len(file_paths)):
        print(file_paths[index])
        
        # Read the file line by line and parse each line as a JSON object
        original_dict = {}
        with open(file_paths[index], 'r') as file:
            for line in file:
                try:
                    data = json.loads(line.strip())
                    if 'id' in data:
                        original_dict[data['id']] = data
                except json.JSONDecodeError as e:
                    print(f"Error decoding line: {e}")
                    continue

        # Print original dictionary length
        print(f"Original dict length: {len(original_dict)}")
        
        # Get JPG filenames
        jpg_set = get_jpg_filenames(folder_paths[0])
        
        # Filter dictionary
        filtered_dict = {k: v for k, v in original_dict.items() if k in jpg_set}
        
        # Print filtered dictionary length
        print(f"Filtered dict length: {len(filtered_dict)}")

        # Write filtered dictionary back to file
        with open(file_paths[index], 'w') as file:
            for item in filtered_dict.values():
                file.write(json.dumps(item) + '\n')





# Original dict length: 81049
# Filtered dict length: 81049
# meta_Amazon_Fashion_dict_title_grpo.json
# Original dict length: 527
# Filtered dict length: 527
# meta_Appliances_dict_title_grpo.json
# Original dict length: 63571
# Filtered dict length: 63571
# meta_Arts_Crafts_and_Sewing_dict_title_grpo.json
# Original dict length: 303
# Filtered dict length: 303
# meta_Automotive_dict_title_grpo.json
# Original dict length: 382
# Filtered dict length: 382
# meta_Baby_Products_dict_title_grpo.json
# Original dict length: 174250
# Filtered dict length: 174250
# meta_Beauty_and_Personal_Care_dict_title_grpo.json
# Original dict length: 5314
# Filtered dict length: 5314
# meta_Books_dict_title_grpo.json
# Original dict length: 2498
# Filtered dict length: 2498
# meta_CDs_and_Vinyl_dict_title_grpo.json
# Original dict length: 302
# Filtered dict length: 302
# meta_Cell_Phones_and_Accessories_dict_title_grpo.json
# Original dict length: 590
# Filtered dict length: 590
# meta_Clothing_Shoes_and_Jewelry_dict_title_grpo.json
# Original dict length: 911
# Filtered dict length: 911
# meta_Digital_Music_dict_title_grpo.json
# Original dict length: 25547
# Filtered dict length: 25547
# meta_Electronics_dict_title_grpo.json
# Original dict length: 1852
# Filtered dict length: 1852
# meta_Gift_Cards_dict_title_grpo.json
# Original dict length: 566
# Filtered dict length: 566
# meta_Grocery_and_Gourmet_Food_dict_title.json
# Original dict length: 248
# Filtered dict length: 248
# meta_Handmade_Products_dict_title_grpo.json
# Original dict length: 132688
# Filtered dict length: 132688
# meta_Health_and_Household_dict_title_grpo.json
# Original dict length: 2361
# Filtered dict length: 2361
# meta_Health_and_Personal_Care_dict_title_grpo.json
# Original dict length: 42667
# Filtered dict length: 42667
# meta_Home_and_Kitchen_dict_title_grpo.json
# Original dict length: 1935
# Filtered dict length: 1935
# meta_Industrial_and_Scientific_dict_title_grpo.json
# Original dict length: 501
# Filtered dict length: 501
# meta_Kindle_Store_dict_title_grpo.json
# Original dict length: 8312
# Filtered dict length: 8312
# meta_Magazine_Subscriptions_dict_title_grpo.json
# Original dict length: 1184
# Filtered dict length: 1184
# meta_Movies_and_TV_dict_title_grpo.json
# Original dict length: 186342
# Filtered dict length: 186342
# meta_Musical_Instruments_dict_title_grpo.json
# Original dict length: 158452
# Filtered dict length: 158452
# meta_Office_Products_dict_title_grpo.json
# Original dict length: 350
# Filtered dict length: 350
# meta_Patio_Lawn_and_Garden_dict_title_grpo.json
# Original dict length: 302
# Filtered dict length: 302
# meta_Pet_Supplies_dict_title_grpo.json
# Original dict length: 278
# Filtered dict length: 278
