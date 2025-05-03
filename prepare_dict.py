import json


def json_to_text(data):
    # 检查并获取各个属性
    title = data.get("title", "N/A")
    main_category = data.get("main_category", "N/A")
    average_rating = data.get("average_rating", "N/A")
    rating_number = data.get("rating_number", "N/A")
    
    # 检查 features 是否为列表
    features = " ".join(data.get("features", [])) if isinstance(data.get("features"), list) else "N/A"
    
    # 检查 description 是否为列表
    description = " ".join(data.get("description", [])) if isinstance(data.get("description"), list) else "N/A"
    
    # 检查 price 是否为 None
    price = data.get("price", None)
    price_text = f"{price:.2f}" if price is not None else "N/A"
    
    store = data.get("store", "N/A")
    
    # 检查 categories 是否为列表
    categories = ", ".join(data.get("categories", [])) if isinstance(data.get("categories"), list) else "N/A"
    
    # 检查 details 是否为字典
    details = data.get("details", {})
    details_text = ", ".join([f"{key}: {value}" for key, value in details.items()]) if isinstance(details, dict) else "N/A"
    
    parent_asin = data.get("parent_asin", "N/A")

    # 构建输出文本
    text = (
        # f"Title: {title}\n"
        f"Main Category: {main_category}\n"
        f"Store: {store}\n"
        f"Price: ${price_text}\n"
        f"Average Rating: {average_rating}\n"
        f"Rating Number: {rating_number}\n"
        f"Features: {features}\n"
        f"Description: {description}\n"
        f"Categories: {categories}\n"
        f"Details: {details_text}\n"
        f"Parent ASIN: {parent_asin}\n"
    )
    return text





# 处理 JSON 列表并生成字典
def process_json_list(json_list):
    result_dict = {}
    
    for json_str in json_list:
        try:
            # 解析 JSON 字符串
            item = json.loads(json_str)
            # 获取 hi_res URL
            hi_res_url = item['images'][0].get('hi_res')
            if hi_res_url:
                # 提取文件名称作为键
                key = hi_res_url.split('/')[-1].split('.')[0]  # 获取 URL 的最后部分并去掉扩展名
                # 获取标题作为值
                value = json_to_text(item)
                # 添加到字典
                result_dict[key] = value
        except (json.JSONDecodeError, IndexError, KeyError) as e:
            print(f"Error processing JSON: {e}")

    return result_dict

if __name__ == "__main__":
    # 打开文件并读取每一行到列表中
        

    # raw_path = '/home/aiscuser/dataset/amazon/meta_All_Beauty.jsonl'
    # raw_path = '/home/aiscuser/dataset/amazon/meta_Amazon_Fashion.jsonl'  
    # raw_path = '/home/aiscuser/dataset/amazon/meta_Appliances.jsonl'      
    # raw_path = '/home/aiscuser/dataset/amazon/meta_Arts_Crafts_and_Sewing.jsonl'   
    # raw_path = '/home/aiscuser/dataset/amazon/meta_Automotive.jsonl'      
    # raw_path = '/home/aiscuser/dataset/amazon/meta_Baby_Products.jsonl'   
    # raw_path = '/home/aiscuser/dataset/amazon/meta_Beauty_and_Personal_Care.jsonl'
    # raw_path = '/home/aiscuser/dataset/amazon/meta_Books.jsonl'
    # raw_path = '/home/aiscuser/dataset/amazon/meta_CDs_and_Vinyl.jsonl'
    # raw_path = '/home/aiscuser/dataset/amazon/meta_Cell_Phones_and_Accessories.jsonl'
    # raw_path = '/home/aiscuser/dataset/amazon/meta_Clothing_Shoes_and_Jewelry.jsonl'
    # raw_path = '/home/aiscuser/dataset/amazon/meta_Digital_Music.jsonl'
    # raw_path = '/home/aiscuser/dataset/amazon/meta_Electronics.jsonl'
    # raw_path = '/home/aiscuser/dataset/amazon/meta_Gift_Cards.jsonl'
    # raw_path = '/home/aiscuser/dataset/amazon/meta_Grocery_and_Gourmet_Food.jsonl'
    # raw_path = '/home/aiscuser/dataset/amazon/meta_Handmade_Products.jsonl'
    # raw_path = '/home/aiscuser/dataset/amazon/meta_Health_and_Household.jsonl'
    # raw_path = '/home/aiscuser/dataset/amazon/meta_Health_and_Personal_Care.jsonl'
    # raw_path = '/home/aiscuser/dataset/amazon/meta_Home_and_Kitchen.jsonl'
    # raw_path = '/home/aiscuser/dataset/amazon/meta_Industrial_and_Scientific.jsonl'
    # raw_path = '/home/aiscuser/dataset/amazon/meta_Kindle_Store.jsonl'
    # raw_path = '/home/aiscuser/dataset/amazon/meta_Magazine_Subscriptions.jsonl'
    # raw_path = '/home/aiscuser/dataset/amazon/meta_Movies_and_TV.jsonl'
    # raw_path = '/home/aiscuser/dataset/amazon/meta_Musical_Instruments.jsonl'
    # raw_path = '/home/aiscuser/dataset/amazon/meta_Office_Products.jsonl'
    # raw_path = '/home/aiscuser/dataset/amazon/meta_Patio_Lawn_and_Garden.jsonl'
    # raw_path = '/home/aiscuser/dataset/amazon/meta_Pet_Supplies.jsonl'
    # raw_path = '/home/aiscuser/dataset/amazon/meta_Software.jsonl'
    # raw_path = '/home/aiscuser/dataset/amazon/meta_Sports_and_Outdoors.jsonl'
    # raw_path = '/home/aiscuser/dataset/amazon/meta_Subscription_Boxes.jsonl'
    # raw_path = '/home/aiscuser/dataset/amazon/meta_Tools_and_Home_Improvement.jsonl'
    # raw_path = '/home/aiscuser/dataset/amazon/meta_Toys_and_Games.jsonl'
    # raw_path = '/home/aiscuser/dataset/amazon/meta_Video_Games.jsonl'


    raw_paths = [
        # # '/home/aiscuser/dataset/amazon/meta_All_Beauty.jsonl',
        # '/home/aiscuser/dataset/amazon/meta_Amazon_Fashion.jsonl',
        # # '/home/aiscuser/dataset/amazon/meta_Appliances.jsonl',
        # '/home/aiscuser/dataset/amazon/meta_Arts_Crafts_and_Sewing.jsonl',
        # '/home/aiscuser/dataset/amazon/meta_Automotive.jsonl',
        # # '/home/aiscuser/dataset/amazon/meta_Baby_Products.jsonl',
        # '/home/aiscuser/dataset/amazon/meta_Beauty_and_Personal_Care.jsonl',
        # # '/home/aiscuser/dataset/amazon/meta_Books.jsonl',
        # '/home/aiscuser/dataset/amazon/meta_CDs_and_Vinyl.jsonl',
        # '/home/aiscuser/dataset/amazon/meta_Cell_Phones_and_Accessories.jsonl',
        # '/home/aiscuser/dataset/amazon/meta_Clothing_Shoes_and_Jewelry.jsonl',
        # # '/home/aiscuser/dataset/amazon/meta_Digital_Music.jsonl',
        # '/home/aiscuser/dataset/amazon/meta_Electronics.jsonl',
        # # '/home/aiscuser/dataset/amazon/meta_Gift_Cards.jsonl',
        '/home/aiscuser/meta_Grocery_and_Gourmet_Food.jsonl',
        # # '/home/aiscuser/dataset/amazon/meta_Handmade_Products.jsonl',
        # '/home/aiscuser/dataset/amazon/meta_Health_and_Household.jsonl',
        # # '/home/aiscuser/dataset/amazon/meta_Health_and_Personal_Care.jsonl',
        # '/home/aiscuser/dataset/amazon/meta_Home_and_Kitchen.jsonl',
        # '/home/aiscuser/dataset/amazon/meta_Industrial_and_Scientific.jsonl',
        # # '/home/aiscuser/dataset/amazon/meta_Kindle_Store.jsonl',
        # # '/home/aiscuser/dataset/amazon/meta_Magazine_Subscriptions.jsonl',
        # # '/home/aiscuser/dataset/amazon/meta_Movies_and_TV.jsonl',
        # # '/home/aiscuser/dataset/amazon/meta_Musical_Instruments.jsonl',
        # '/home/aiscuser/dataset/amazon/meta_Office_Products.jsonl',
        # '/home/aiscuser/dataset/amazon/meta_Patio_Lawn_and_Garden.jsonl',
        # '/home/aiscuser/dataset/amazon/meta_Pet_Supplies.jsonl',
        # # '/home/aiscuser/dataset/amazon/meta_Software.jsonl',
        # '/home/aiscuser/dataset/amazon/meta_Sports_and_Outdoors.jsonl',
        # # '/home/aiscuser/dataset/amazon/meta_Subscription_Boxes.jsonl',
        # '/home/aiscuser/dataset/amazon/meta_Tools_and_Home_Improvement.jsonl',
        # '/home/aiscuser/dataset/amazon/meta_Toys_and_Games.jsonl',
        # # '/home/aiscuser/dataset/amazon/meta_Video_Games.jsonl',
    ]

###############

    new_paths = [
        # # '/home/aiscuser/dataset/amazon/meta_All_Beauty_dict.json',
        # '/home/aiscuser/dataset/amazon/meta_Amazon_Fashion_dict.json',
        # # '/home/aiscuser/dataset/amazon/meta_Appliances_dict.json',
        # '/home/aiscuser/dataset/amazon/meta_Arts_Crafts_and_Sewing_dict.json',
        # '/home/aiscuser/dataset/amazon/meta_Automotive_dict.json',
        # # '/home/aiscuser/dataset/amazon/meta_Baby_Products_dict.json',
        # '/home/aiscuser/dataset/amazon/meta_Beauty_and_Personal_Care_dict.json',
        # # '/home/aiscuser/dataset/amazon/meta_Books_dict.json',
        # '/home/aiscuser/dataset/amazon/meta_CDs_and_Vinyl_dict.json',
        # '/home/aiscuser/dataset/amazon/meta_Cell_Phones_and_Accessories_dict.json',
        # '/home/aiscuser/dataset/amazon/meta_Clothing_Shoes_and_Jewelry_dict.json',
        # # '/home/aiscuser/dataset/amazon/meta_Digital_Music_dict.json',
        # '/home/aiscuser/dataset/amazon/meta_Electronics_dict.json',
        # # '/home/aiscuser/dataset/amazon/meta_Gift_Cards_dict.json',
        '/home/aiscuser/meta_Grocery_and_Gourmet_Food_dict.json',
        # # '/home/aiscuser/dataset/amazon/meta_Handmade_Products_dict.json',
        # '/home/aiscuser/dataset/amazon/meta_Health_and_Household_dict.json',
        # # '/home/aiscuser/dataset/amazon/meta_Health_and_Personal_Care_dict.json',
        # '/home/aiscuser/dataset/amazon/meta_Home_and_Kitchen_dict.json',
        # '/home/aiscuser/dataset/amazon/meta_Industrial_and_Scientific_dict.json',
        # # '/home/aiscuser/dataset/amazon/meta_Kindle_Store_dict.json',
        # # '/home/aiscuser/dataset/amazon/meta_Magazine_Subscriptions_dict.json',
        # # '/home/aiscuser/dataset/amazon/meta_Movies_and_TV_dict.json',
        # # '/home/aiscuser/dataset/amazon/meta_Musical_Instruments_dict.json',
        # '/home/aiscuser/dataset/amazon/meta_Office_Products_dict.json',
        # '/home/aiscuser/dataset/amazon/meta_Patio_Lawn_and_Garden_dict.json',
        # '/home/aiscuser/dataset/amazon/meta_Pet_Supplies_dict.json',
        # # '/home/aiscuser/dataset/amazon/meta_Software_dict.json',
        # '/home/aiscuser/dataset/amazon/meta_Sports_and_Outdoors_dict.json',
        # # '/home/aiscuser/dataset/amazon/meta_Subscription_Boxes_dict.json',
        # '/home/aiscuser/dataset/amazon/meta_Tools_and_Home_Improvement_dict.json',
        # '/home/aiscuser/dataset/amazon/meta_Toys_and_Games_dict.json',
        # # '/home/aiscuser/dataset/amazon/meta_Video_Games_dict.json',
    ]


    for index in range(len(raw_paths)):


        with open(raw_paths[index], 'r', encoding='utf-8') as file:
            json_list = [line.strip() for line in file]

        result = process_json_list(json_list)
        

        # 将结果字典保存到指定文件
        with open(new_paths[index], 'w', encoding='utf-8') as outfile:
            json.dump(result, outfile, ensure_ascii=False, indent=4)

        # print("Dictionary saved to /blob/weiwei/datasets/Amazon/meta_Subscription_Boxes_dict.json")
