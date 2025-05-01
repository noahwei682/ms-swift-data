#!/usr/bin/env python3
import json
import os
import argparse

def convert_format(input_data, image_dir):
    """
    Convert from:
    {
        "id": "71hD-k6kaxL",
        "image": "71hD-k6kaxL.jpg",
        "conversations": [
            {"from": "human", "value": "<image>\nWhat is the specific name of the object in this picture?"},
            {"from": "gpt", "value": "Title: Phantasmagoria: A Puzzle of Flesh\n"}
        ]
    }
    
    To:
    {"messages": [{"role": "user", "content": "<image>What is the specific name of the object in this picture?"}, 
                 {"role": "assistant", "content": "Title: Phantasmagoria: A Puzzle of Flesh"}], 
     "images": ["/home/aiscuser/lmms-eval/msdata/images/images/71hD-k6kaxL.jpg"]}
    """
    result = []
    
    for item in input_data:
        new_item = {
            "messages": [],
            "images": []
        }
        
        # Add image path to images list with the specified prefix
        image_path = os.path.join(image_dir, item['image'])
        new_item["images"].append(image_path)
        
        # Convert conversations to messages
        for conv in item["conversations"]:
            role = "user" if conv["from"] == "human" else "assistant"
            content = conv["value"]
            
            # Clean up the content
            if role == "user" and content.startswith("<image>\n"):
                content = content.replace("<image>\n", "<image>")
            if role == "assistant" and content.endswith("\n"):
                content = content.rstrip("\n")
            
            new_item["messages"].append({
                "role": role,
                "content": content
            })
        
        result.append(new_item)
    
    return result

def process_file(input_path, output_path, image_dir):
    """Process a single file"""
    try:
        # Read input JSON file
        with open(input_path, 'r', encoding='utf-8') as f:
            input_data = json.load(f)
        
        # Convert format
        result = convert_format(input_data, image_dir)
        
        # Create output directory if it doesn't exist
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Write output JSON file
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        
        print(f"Conversion complete. Output written to {output_path}")
        print(f"Converted {len(result)} entries")
        return True
        
    except Exception as e:
        print(f"Error processing {input_path}: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Convert JSON format for dataset")
    parser.add_argument("--input_dir", default="/home/aiscuser/lmms-eval/msdata/msdata/split/split_small", 
                        help="Directory containing input JSON files")
    parser.add_argument("--output_dir", default="/home/aiscuser/lmms-eval/msdata/msdata/split/qwen_file", 
                        help="Directory for output JSON files")
    parser.add_argument("--image_dir", default="/home/aiscuser/lmms-eval/msdata/images/images", 
                        help="Directory containing images")
    parser.add_argument("--prefix", default="qwen_", help="Prefix to add to output filenames")
    
    args = parser.parse_args()
    
    # List of files to process
    file_list = [
        "meta_All_Beauty_details_sftdata_att_train_1800.json",
        "meta_All_Beauty_feature_sftdata_att_train_1800.json",
        "meta_All_Beauty_main_category_sftdata_att_train_1800.json",
        "meta_All_Beauty_price_sftdata_att_train_1800.json",
        "meta_All_Beauty_Store_sftdata_att_train_1800.json",
        "meta_All_Beauty_title_sftdata_att_train_1800.json",
        "meta_Amazon_Fashion_description_sftdata_att_train_180.json",
        "meta_Amazon_Fashion_details_sftdata_att_train_1800.json",
        "meta_Amazon_Fashion_feature_sftdata_att_train_180.json",
        "meta_Amazon_Fashion_main_category_sftdata_att_train_180.json",
        "meta_Amazon_Fashion_price_sftdata_att_train_0.json",
        "meta_Amazon_Fashion_Store_sftdata_att_train_180.json",
        "meta_Amazon_Fashion_title_sftdata_att_train_180.json",
        "meta_Appliances_description_sftdata_att_train_180.json",
        "meta_Appliances_details_sftdata_att_train_1800.json",
        "meta_Appliances_feature_sftdata_att_train_180.json",
        "meta_Appliances_main_category_sftdata_att_train_180.json",
        "meta_Appliances_price_sftdata_att_train_30.json",
        "meta_Appliances_Store_sftdata_att_train_180.json",
        "meta_Appliances_title_sftdata_att_train_1800.json",
        "meta_Arts_Crafts_and_Sewing_description_sftdata_att_train_1800.json",
        "meta_Arts_Crafts_and_Sewing_details_sftdata_att_train_1800.json",
        "meta_Arts_Crafts_and_Sewing_feature_sftdata_att_train_1800.json",
        "meta_Arts_Crafts_and_Sewing_main_category_sftdata_att_train_1800.json",
        "meta_Arts_Crafts_and_Sewing_price_sftdata_att_train_1800.json",
        "meta_Arts_Crafts_and_Sewing_Store_sftdata_att_train_1800.json",
        "meta_Arts_Crafts_and_Sewing_title_sftdata_att_train_180.json",
        "meta_Automotive_description_sftdata_att_train_180.json",
        "meta_Automotive_details_sftdata_att_train_180.json",
        "meta_Automotive_feature_sftdata_att_train_180.json",
        "meta_Automotive_main_category_sftdata_att_train_180.json",
        "meta_Automotive_price_sftdata_att_train_0.json",
        "meta_Automotive_Store_sftdata_att_train_180.json",
        "meta_Automotive_title_sftdata_att_train_180.json",
        "meta_Baby_Products_description_sftdata_att_train_180.json",
        "meta_Baby_Products_details_sftdata_att_train_1800.json",
        "meta_Baby_Products_feature_sftdata_att_train_180.json",
        "meta_Baby_Products_main_category_sftdata_att_train_180.json",
        "meta_Baby_Products_price_sftdata_att_train_180.json",
        "meta_Baby_Products_Store_sftdata_att_train_180.json",
        "meta_Baby_Products_title_sftdata_att_train_1800.json",
        "meta_Video_Games_description_sftdata_att_train_180.json",
        "meta_Video_Games_details_sftdata_att_train_1800.json",
        "meta_Video_Games_feature_sftdata_att_train_180.json",
        "meta_Video_Games_main_category_sftdata_att_train_180.json",
        "meta_Video_Games_price_sftdata_att_train_30.json",
        "meta_Video_Games_Store_sftdata_att_train_180.json",
        "meta_Video_Games_title_sftdata_att_train_1800.json"
    ]
    
    # Count successful conversions
    success_count = 0
    total_count = len(file_list)
    
    # Process each file
    for filename in file_list:
        input_path = os.path.join(args.input_dir, filename)
        output_path = os.path.join(args.output_dir, f"{args.prefix}{filename}")
        
        print(f"Processing {filename}...")
        if process_file(input_path, output_path, args.image_dir):
            success_count += 1
    
    print(f"Conversion complete. Successfully processed {success_count} out of {total_count} files.")
    return 0

if __name__ == "__main__":
    exit(main()) 
