import json
import os
import base64

## 指定输入和输出文件路径
# input_file_path = '/blob/weiwei/datasets/Amazon/meta_Subscription_Boxes_dict.json'

input_file_paths = [
    # '/home/aiscuser/dataset/amazon/meta_All_Beauty_dict.json',
    # '/home/aiscuser/dataset/amazon/meta_Amazon_Fashion_dict.json',
    # '/home/aiscuser/dataset/amazon/meta_Appliances_dict.json',
    # '/home/aiscuser/dataset/amazon/meta_Arts_Crafts_and_Sewing_dict.json',
    # '/home/aiscuser/dataset/amazon/meta_Automotive_dict.json',
    # '/home/aiscuser/dataset/amazon/meta_Baby_Products_dict.json',
    # '/home/aiscuser/dataset/amazon/meta_Beauty_and_Personal_Care_dict.json',
    # '/home/aiscuser/dataset/amazon/meta_Books_dict.json',
    # '/home/aiscuser/dataset/amazon/meta_CDs_and_Vinyl_dict.json',
    # '/home/aiscuser/dataset/amazon/meta_Cell_Phones_and_Accessories_dict.json',
    # '/home/aiscuser/dataset/amazon/meta_Clothing_Shoes_and_Jewelry_dict.json',
    # '/home/aiscuser/dataset/amazon/meta_Digital_Music_dict.json',
    # '/home/aiscuser/dataset/amazon/meta_Electronics_dict.json',
    # '/home/aiscuser/dataset/amazon/meta_Gift_Cards_dict.json',
    # '/home/aiscuser/dataset/amazon/meta_Grocery_and_Gourmet_Food_dict.json',
    # '/home/aiscuser/dataset/amazon/meta_Handmade_Products_dict.json',
    # '/home/aiscuser/dataset/amazon/meta_Health_and_Household_dict.json',
    # '/home/aiscuser/dataset/amazon/meta_Health_and_Personal_Care_dict.json',
    # '/home/aiscuser/dataset/amazon/meta_Home_and_Kitchen_dict.json',
    # '/home/aiscuser/dataset/amazon/meta_Industrial_and_Scientific_dict.json',
    # '/home/aiscuser/dataset/amazon/meta_Kindle_Store_dict.json',
    # '/home/aiscuser/dataset/amazon/meta_Magazine_Subscriptions_dict.json',
    # '/home/aiscuser/dataset/amazon/meta_Movies_and_TV_dict.json',
    # '/home/aiscuser/dataset/amazon/meta_Musical_Instruments_dict.json',
    # '/home/aiscuser/dataset/amazon/meta_Office_Products_dict.json',
    # '/home/aiscuser/dataset/amazon/meta_Patio_Lawn_and_Garden_dict.json',
    # '/home/aiscuser/dataset/amazon/meta_Pet_Supplies_dict.json',
    # '/home/aiscuser/dataset/amazon/meta_Software_dict.json',
    # '/home/aiscuser/dataset/amazon/meta_Sports_and_Outdoors_dict.json',
    # '/home/aiscuser/dataset/amazon/meta_Subscription_Boxes_dict.json',
    # '/home/aiscuser/dataset/amazon/meta_Tools_and_Home_Improvement_dict.json',
    # '/home/aiscuser/dataset/amazon/meta_Toys_and_Games_dict.j   son',
    # '/home/aiscuser/dataset/amazon/meta_Video_Games_dict.json',
    '/home/aiscuser/meta_Grocery_and_Gourmet_Food_dict.json',
]

title_file_path = '/home/aiscuser/meta_Grocery_and_Gourmet_Food_dict_title.json'

# output_file_path = '/blob/weiwei/datasets/Amazon/meta_Subscription_Boxes_exist_gene_ITdata.json'


output_file_paths = [
    # '/home/aiscuser/dataset/amazon/meta_All_Beauty_exist_gene_ITdata_detail.json',
    # '/home/aiscuser/dataset/amazon/meta_Amazon_Fashion_dict.json',
    # '/home/aiscuser/dataset/amazon/meta_Appliances_exist_gene_ITdata_detail.json',
    # '/home/aiscuser/dataset/amazon/meta_Arts_Crafts_and_Sewing_dict.json',
    # '/home/aiscuser/dataset/amazon/meta_Automotive_dict.json',
    # '/home/aiscuser/dataset/amazon/meta_Baby_Products_exist_gene_ITdata_detail.json',
    # '/home/aiscuser/dataset/amazon/meta_Beauty_and_Personal_Care_dict.json',
    # '/home/aiscuser/dataset/amazon/meta_Books_exist_gene_ITdata_detail.json',
    # '/home/aiscuser/dataset/amazon/meta_CDs_and_Vinyl_dict.json',
    # '/home/aiscuser/dataset/amazon/meta_Cell_Phones_and_Accessories_dict.json',
    # '/home/aiscuser/dataset/amazon/meta_Clothing_Shoes_and_Jewelry_dict.json',
    # '/home/aiscuser/dataset/amazon/meta_Digital_Music_exist_gene_ITdata_detail.json',
    # '/home/aiscuser/dataset/amazon/meta_Electronics_dict.json',
    # '/home/aiscuser/dataset/amazon/meta_Gift_Cards_exist_gene_ITdata_detail.json',
    # '/home/aiscuser/dataset/amazon/meta_Grocery_and_Gourmet_Food_dict.json',
    # '/home/aiscuser/dataset/amazon/meta_Handmade_Products_exist_gene_ITdata_detail.json',
    # '/home/aiscuser/dataset/amazon/meta_Health_and_Household_dict.json',
    # '/home/aiscuser/dataset/amazon/meta_Health_and_Personal_Care_exist_gene_ITdata_detail.json',
    # '/home/aiscuser/dataset/amazon/meta_Home_and_Kitchen_dict.json',
    # '/home/aiscuser/dataset/amazon/meta_Industrial_and_Scientific_dict.json',
    # '/home/aiscuser/dataset/amazon/meta_Kindle_Store_exist_gene_ITdata_detail.json',
    # '/home/aiscuser/dataset/amazon/meta_Magazine_Subscriptions_exist_gene_ITdata_detail.json',
    # '/home/aiscuser/dataset/amazon/meta_Movies_and_TV_exist_gene_ITdata_detail.json',
    # '/home/aiscuser/dataset/amazon/meta_Musical_Instruments_exist_gene_ITdata_detail.json',
    # '/home/aiscuser/dataset/amazon/meta_Office_Products_dict.json',
    # '/home/aiscuser/dataset/amazon/meta_Patio_Lawn_and_Garden_dict.json',
    # '/home/aiscuser/dataset/amazon/meta_Pet_Supplies_dict.json',
    # '/home/aiscuser/dataset/amazon/meta_Software_exist_gene_ITdata_detail.json',
    # '/home/aiscuser/dataset/amazon/meta_Sports_and_Outdoors_dict.json',
    # '/home/aiscuser/dataset/amazon/meta_Subscription_Boxes_exist_gene_ITdata_detail.json',
    # '/home/aiscuser/dataset/amazon/meta_Tools_and_Home_Improvement_dict.json',
    # '/home/aiscuser/dataset/amazon/meta_Toys_and_Games_dict.json',
    # '/home/aiscuser/dataset/amazon/meta_Video_Games_exist_gene_ITdata_detail.json',
    '/home/aiscuser/meta_Grocery_and_Gourmet_Food_dict_grpo.json',
]


# 读取 meta_Gift_Cards_dict.json 文件
def read_meta_gift_cards_dict(file_path):
    with open(file_path, 'r', encoding='utf-8') as json_file:
        return json.load(json_file)

# 创建 JSON 列表
def create_json_list(meta_gift_cards_dict, title_dict):
    json_list = []

    for key, value in meta_gift_cards_dict.items():
        image_path = f"/home/aiscuser/lmms-eval/llava-ov-ewc-ms/msdata/images/images/{key}.jpg"
        # 获取标题，如果不存在则使用空字符串
        title_value = title_dict.get(key, "")
        
        # Note: Base64 encoding is left empty as we don't have the actual images
        # If you need to encode real images, you would need to read the file and encode it
        json_item = {
            "id": key,
            "image_path": image_path,
            "image_base64": "",
            "problem": "Based on visual details, infer and output: What is shown in this picture?",
            "solution": f"<think>Looking at the product image to analyze what's shown. I need to identify the product based on visual details in the image.{value}</think>\n\n<answer>{title_value}</answer>",
            "original_question": "What is shown in this picture?",
            "original_answer": title_value
        }
        json_list.append(json_item)

    return json_list

# 写入 JSON 列表到文件，每个 JSON 对象单独一行
def write_json_list_to_file(json_list, file_path):
    with open(file_path, 'w', encoding='utf-8') as json_file:
        for item in json_list:
            json.dump(item, json_file, ensure_ascii=False)
            json_file.write('\n')  # 每个 JSON 对象后换行

# 如果需要读取实际图片并转换为base64，可以使用这个函数
def image_to_base64(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    return ""

if __name__ == "__main__":
    # 读取标题数据
    title_dict = read_meta_gift_cards_dict(title_file_path)

    for index in range(len(input_file_paths)):
        # 读取字典数据
        meta_gift_cards_dict = read_meta_gift_cards_dict(input_file_paths[index])
        
        # 创建 JSON 列表
        json_list = create_json_list(meta_gift_cards_dict, title_dict)
        
        # 写入到输出文件
        write_json_list_to_file(json_list, output_file_paths[index])
        
        print(f"JSON 列表已写入到 {output_file_paths[index]}")
