
import os
import json

def get_jpg_filenames(folder_path):
    jpg_filenames = set()  # 使用集合来存储文件名（不带扩展名）
    
    # 遍历文件夹
    for filename in os.listdir(folder_path):
        if filename.endswith('.jpg'):
            # 去掉扩展名
            name_without_extension = os.path.splitext(filename)[0]

            # import ipdb; ipdb.set_trace()

            # 仅提取第一个点前面的部分
            # name_before_first_dot = name_without_extension.split('.')[0]
            # jpg_filenames.add(name_before_first_dot)
            jpg_filenames.add(name_without_extension)

    return jpg_filenames

if __name__ == "__main__":


    # folder_paths = [
    #     "/blob/weiwei/datasets/Amazon/meta_Magazine_Subscriptions_pictures",
    #     "/blob/weiwei/datasets/Amazon/meta_Grocery_and_Gourmet_Food_pictures",
    #     "/blob/weiwei/datasets/Amazon/meta_Arts_Crafts_and_Sewing_pictures",
    #     "/blob/weiwei/datasets/Amazon/meta_Sports_and_Outdoors_pictures",
    #     "/blob/weiwei/datasets/Amazon/meta_Cell_Phones_and_Accessories_pictures",
    #     # "/blob/weiwei/datasets/Amazon/meta_Health_and_Personal_Care_pictures",
    #     "/blob/weiwei/datasets/Amazon/meta_All_Beauty_pictures",
    #     "/blob/weiwei/datasets/Amazon/meta_Health_and_Household_pictures",
    #     "/blob/weiwei/datasets/Amazon/meta_Industrial_and_Scientific_pictures",
    #     "/blob/weiwei/datasets/Amazon/meta_Beauty_and_Personal_Care_pictures",
    #     "/blob/weiwei/datasets/Amazon/meta_Electronics_pictures",
    #     "/blob/weiwei/datasets/Amazon/meta_Movies_and_TV_pictures",
    #     "/blob/weiwei/datasets/Amazon/meta_Digital_Music_pictures",
    #     "/blob/weiwei/datasets/Amazon/meta_Patio_Lawn_and_Garden_pictures",
    #     "/blob/weiwei/datasets/Amazon/meta_Appliances_pictures",
    #     "/blob/weiwei/datasets/Amazon/meta_Toys_and_Games_pictures"
    # ]


    # folder_paths = [
    #     '/home/aiscuser/dataset/amazon/meta_All_Beauty_pictures',
    #     '/home/aiscuser/dataset/amazon/meta_Amazon_Fashion_pictures',
    #     '/home/aiscuser/dataset/amazon/meta_Appliances_pictures',
    #     '/home/aiscuser/dataset/amazon/meta_Arts_Crafts_and_Sewing_pictures',
    #     '/home/aiscuser/dataset/amazon/meta_Automotive_pictures',
    #     '/home/aiscuser/dataset/amazon/meta_Baby_Products_pictures',
    #     '/home/aiscuser/dataset/amazon/meta_Beauty_and_Personal_Care_pictures',
    #     '/home/aiscuser/dataset/amazon/meta_Books_pictures',
    #     '/home/aiscuser/dataset/amazon/meta_CDs_and_Vinyl_pictures',
    #     '/home/aiscuser/dataset/amazon/meta_Cell_Phones_and_Accessories_pictures',
    #     '/home/aiscuser/dataset/amazon/meta_Clothing_Shoes_and_Jewelry_pictures',
    #     '/home/aiscuser/dataset/amazon/meta_Digital_Music_pictures',
    #     '/home/aiscuser/dataset/amazon/meta_Electronics_pictures',
    #     '/home/aiscuser/dataset/amazon/meta_Gift_Cards_pictures',
    #     '/home/aiscuser/dataset/amazon/meta_Grocery_and_Gourmet_Food_pictures',
    #     '/home/aiscuser/dataset/amazon/meta_Handmade_Products_pictures',
    #     '/home/aiscuser/dataset/amazon/meta_Health_and_Household_pictures',
    #     '/home/aiscuser/dataset/amazon/meta_Health_and_Personal_Care_pictures',
    #     '/home/aiscuser/dataset/amazon/meta_Home_and_Kitchen_pictures',
    #     '/home/aiscuser/dataset/amazon/meta_Industrial_and_Scientific_pictures',
    #     '/home/aiscuser/dataset/amazon/meta_Kindle_Store_pictures',
    #     '/home/aiscuser/dataset/amazon/meta_Magazine_Subscriptions_pictures',
    #     '/home/aiscuser/dataset/amazon/meta_Movies_and_TV_pictures',
    #     '/home/aiscuser/dataset/amazon/meta_Musical_Instruments_pictures',
    #     '/home/aiscuser/dataset/amazon/meta_Office_Products_pictures',
    #     '/home/aiscuser/dataset/amazon/meta_Patio_Lawn_and_Garden_pictures',
    #     '/home/aiscuser/dataset/amazon/meta_Pet_Supplies_pictures',
    #     '/home/aiscuser/dataset/amazon/meta_Software_pictures',
    #     '/home/aiscuser/dataset/amazon/meta_Sports_and_Outdoors_pictures',
    #     '/home/aiscuser/dataset/amazon/meta_Subscription_Boxes_pictures',
    #     '/home/aiscuser/dataset/amazon/meta_Tools_and_Home_Improvement_pictures',
    #     '/home/aiscuser/dataset/amazon/meta_Toys_and_Games_pictures',
    #     '/home/aiscuser/dataset/amazon/meta_Video_Games_pictures',
    # ]



    folder_paths = [
        '/home/aiscuser/dataset/amazon/images/',
    ]


#############


    # file_paths = [
    #     '/home/aiscuser/dataset/amazon/meta_All_Beauty_dict.json',
    #     '/home/aiscuser/dataset/amazon/meta_Amazon_Fashion_dict.json',
    #     '/home/aiscuser/dataset/amazon/meta_Appliances_dict.json',
    #     '/home/aiscuser/dataset/amazon/meta_Arts_Crafts_and_Sewing_dict.json',
    #     '/home/aiscuser/dataset/amazon/meta_Automotive_dict.json',
    #     '/home/aiscuser/dataset/amazon/meta_Baby_Products_dict.json',
    #     '/home/aiscuser/dataset/amazon/meta_Beauty_and_Personal_Care_dict.json',
    #     '/home/aiscuser/dataset/amazon/meta_Books_dict.json',
    #     '/home/aiscuser/dataset/amazon/meta_CDs_and_Vinyl_dict.json',
    #     '/home/aiscuser/dataset/amazon/meta_Cell_Phones_and_Accessories_dict.json',
    #     '/home/aiscuser/dataset/amazon/meta_Clothing_Shoes_and_Jewelry_dict.json',
    #     '/home/aiscuser/dataset/amazon/meta_Digital_Music_dict.json',
    #     '/home/aiscuser/dataset/amazon/meta_Electronics_dict.json',
    #     '/home/aiscuser/dataset/amazon/meta_Gift_Cards_dict.json',
    #     '/home/aiscuser/dataset/amazon/meta_Grocery_and_Gourmet_Food_dict.json',
    #     '/home/aiscuser/dataset/amazon/meta_Handmade_Products_dict.json',
    #     '/home/aiscuser/dataset/amazon/meta_Health_and_Household_dict.json',
    #     '/home/aiscuser/dataset/amazon/meta_Health_and_Personal_Care_dict.json',
    #     '/home/aiscuser/dataset/amazon/meta_Home_and_Kitchen_dict.json',
    #     '/home/aiscuser/dataset/amazon/meta_Industrial_and_Scientific_dict.json',
    #     '/home/aiscuser/dataset/amazon/meta_Kindle_Store_dict.json',
    #     '/home/aiscuser/dataset/amazon/meta_Magazine_Subscriptions_dict.json',
    #     '/home/aiscuser/dataset/amazon/meta_Movies_and_TV_dict.json',
    #     '/home/aiscuser/dataset/amazon/meta_Musical_Instruments_dict.json',
    #     '/home/aiscuser/dataset/amazon/meta_Office_Products_dict.json',
    #     '/home/aiscuser/dataset/amazon/meta_Patio_Lawn_and_Garden_dict.json',
    #     '/home/aiscuser/dataset/amazon/meta_Pet_Supplies_dict.json',
    #     '/home/aiscuser/dataset/amazon/meta_Software_dict.json',
    #     '/home/aiscuser/dataset/amazon/meta_Sports_and_Outdoors_dict.json',
    #     '/home/aiscuser/dataset/amazon/meta_Subscription_Boxes_dict.json',
    #     '/home/aiscuser/dataset/amazon/meta_Tools_and_Home_Improvement_dict.json',
    #     '/home/aiscuser/dataset/amazon/meta_Toys_and_Games_dict.json',
    #     '/home/aiscuser/dataset/amazon/meta_Video_Games_dict.json',
    # ]



    file_paths = [      
        '/home/aiscuser/dataset/amazon/meta_All_Beauty_dict_description.json',
        '/home/aiscuser/dataset/amazon/meta_All_Beauty_dict_feature.json',
        '/home/aiscuser/dataset/amazon/meta_All_Beauty_dict_main_category.json',
        '/home/aiscuser/dataset/amazon/meta_All_Beauty_dict_price.json',
        '/home/aiscuser/dataset/amazon/meta_All_Beauty_dict_Store.json',
        '/home/aiscuser/dataset/amazon/meta_All_Beauty_dict_title.json',
        '/home/aiscuser/dataset/amazon/meta_Amazon_Fashion_dict_description.json',
        '/home/aiscuser/dataset/amazon/meta_Amazon_Fashion_dict_feature.json',
        '/home/aiscuser/dataset/amazon/meta_Amazon_Fashion_dict_main_category.json',
        '/home/aiscuser/dataset/amazon/meta_Amazon_Fashion_dict_price.json',
        '/home/aiscuser/dataset/amazon/meta_Amazon_Fashion_dict_Store.json',
        '/home/aiscuser/dataset/amazon/meta_Amazon_Fashion_dict_title.json',
        '/home/aiscuser/dataset/amazon/meta_Appliances_dict_description.json',
        '/home/aiscuser/dataset/amazon/meta_Appliances_dict_feature.json',
        '/home/aiscuser/dataset/amazon/meta_Appliances_dict_main_category.json',
        '/home/aiscuser/dataset/amazon/meta_Appliances_dict_price.json',
        '/home/aiscuser/dataset/amazon/meta_Appliances_dict_Store.json',
        '/home/aiscuser/dataset/amazon/meta_Appliances_dict_title.json',
        '/home/aiscuser/dataset/amazon/meta_Arts_Crafts_and_Sewing_dict_description.json',
        '/home/aiscuser/dataset/amazon/meta_Arts_Crafts_and_Sewing_dict_feature.json',
        '/home/aiscuser/dataset/amazon/meta_Arts_Crafts_and_Sewing_dict_main_category.json',
        '/home/aiscuser/dataset/amazon/meta_Arts_Crafts_and_Sewing_dict_price.json',
        '/home/aiscuser/dataset/amazon/meta_Arts_Crafts_and_Sewing_dict_Store.json',
        '/home/aiscuser/dataset/amazon/meta_Arts_Crafts_and_Sewing_dict_title.json',
        '/home/aiscuser/dataset/amazon/meta_Automotive_dict_description.json',
        '/home/aiscuser/dataset/amazon/meta_Automotive_dict_feature.json',
        '/home/aiscuser/dataset/amazon/meta_Automotive_dict_main_category.json',
        '/home/aiscuser/dataset/amazon/meta_Automotive_dict_price.json',
        '/home/aiscuser/dataset/amazon/meta_Automotive_dict_Store.json',
        '/home/aiscuser/dataset/amazon/meta_Automotive_dict_title.json',
        '/home/aiscuser/dataset/amazon/meta_Baby_Products_dict_description.json',
        '/home/aiscuser/dataset/amazon/meta_Baby_Products_dict_description.json',
        '/home/aiscuser/dataset/amazon/meta_Baby_Products_dict_feature.json',
        '/home/aiscuser/dataset/amazon/meta_Baby_Products_dict_main_category.json',
        '/home/aiscuser/dataset/amazon/meta_Baby_Products_dict_price.json',
        '/home/aiscuser/dataset/amazon/meta_Baby_Products_dict_Store.json',
        '/home/aiscuser/dataset/amazon/meta_Baby_Products_dict_title.json',
        '/home/aiscuser/dataset/amazon/meta_Beauty_and_Personal_Care_dict_description.json',
        '/home/aiscuser/dataset/amazon/meta_Beauty_and_Personal_Care_dict_feature.json',
        '/home/aiscuser/dataset/amazon/meta_Beauty_and_Personal_Care_dict_main_category.json',
        '/home/aiscuser/dataset/amazon/meta_Beauty_and_Personal_Care_dict_price.json',
        '/home/aiscuser/dataset/amazon/meta_Beauty_and_Personal_Care_dict_Store.json',
        '/home/aiscuser/dataset/amazon/meta_Beauty_and_Personal_Care_dict_title.json',
        '/home/aiscuser/dataset/amazon/meta_Books_dict_description.json',
        '/home/aiscuser/dataset/amazon/meta_Books_dict_feature.json',
        '/home/aiscuser/dataset/amazon/meta_Books_dict_main_category.json',
        '/home/aiscuser/dataset/amazon/meta_Books_dict_price.json',
        '/home/aiscuser/dataset/amazon/meta_Books_dict_Store.json',
        '/home/aiscuser/dataset/amazon/meta_Books_dict_title.json',
        '/home/aiscuser/dataset/amazon/meta_CDs_and_Vinyl_dict_description.json',
        '/home/aiscuser/dataset/amazon/meta_CDs_and_Vinyl_dict_feature.json',
        '/home/aiscuser/dataset/amazon/meta_CDs_and_Vinyl_dict_main_category.json',
        '/home/aiscuser/dataset/amazon/meta_CDs_and_Vinyl_dict_price.json',
        '/home/aiscuser/dataset/amazon/meta_CDs_and_Vinyl_dict_Store.json',
        '/home/aiscuser/dataset/amazon/meta_CDs_and_Vinyl_dict_title.json',
        '/home/aiscuser/dataset/amazon/meta_Cell_Phones_and_Accessories_dict_description.json',
        '/home/aiscuser/dataset/amazon/meta_Cell_Phones_and_Accessories_dict_feature.json',
        '/home/aiscuser/dataset/amazon/meta_Cell_Phones_and_Accessories_dict_main_category.json',
        '/home/aiscuser/dataset/amazon/meta_Cell_Phones_and_Accessories_dict_price.json',
        '/home/aiscuser/dataset/amazon/meta_Cell_Phones_and_Accessories_dict_Store.json',
        '/home/aiscuser/dataset/amazon/meta_Cell_Phones_and_Accessories_dict_title.json',
        '/home/aiscuser/dataset/amazon/meta_Clothing_Shoes_and_Jewelry_dict_description.json',
        '/home/aiscuser/dataset/amazon/meta_Clothing_Shoes_and_Jewelry_dict_feature.json',
        '/home/aiscuser/dataset/amazon/meta_Clothing_Shoes_and_Jewelry_dict_main_category.json',
        '/home/aiscuser/dataset/amazon/meta_Clothing_Shoes_and_Jewelry_dict_price.json',
        '/home/aiscuser/dataset/amazon/meta_Clothing_Shoes_and_Jewelry_dict_Store.json',
        '/home/aiscuser/dataset/amazon/meta_Clothing_Shoes_and_Jewelry_dict_title.json',
        '/home/aiscuser/dataset/amazon/meta_Digital_Music_dict_description.json',
        '/home/aiscuser/dataset/amazon/meta_Digital_Music_dict_feature.json',
        '/home/aiscuser/dataset/amazon/meta_Digital_Music_dict_main_category.json',
        '/home/aiscuser/dataset/amazon/meta_Digital_Music_dict_price.json',
        '/home/aiscuser/dataset/amazon/meta_Digital_Music_dict_Store.json',
        '/home/aiscuser/dataset/amazon/meta_Digital_Music_dict_title.json',
        '/home/aiscuser/dataset/amazon/meta_Electronics_dict_description.json',
        '/home/aiscuser/dataset/amazon/meta_Electronics_dict_feature.json',
        '/home/aiscuser/dataset/amazon/meta_Electronics_dict_main_category.json',
        '/home/aiscuser/dataset/amazon/meta_Electronics_dict_price.json',
        '/home/aiscuser/dataset/amazon/meta_Electronics_dict_Store.json',
        '/home/aiscuser/dataset/amazon/meta_Electronics_dict_title.json',
        '/home/aiscuser/dataset/amazon/meta_Gift_Cards_dict_description.json',
        '/home/aiscuser/dataset/amazon/meta_Gift_Cards_dict_feature.json',
        '/home/aiscuser/dataset/amazon/meta_Gift_Cards_dict_main_category.json',
        '/home/aiscuser/dataset/amazon/meta_Gift_Cards_dict_price.json',
        '/home/aiscuser/dataset/amazon/meta_Gift_Cards_dict_Store.json',
        '/home/aiscuser/dataset/amazon/meta_Gift_Cards_dict_title.json',
        '/home/aiscuser/dataset/amazon/meta_Grocery_and_Gourmet_Food_dict_description.json',
        '/home/aiscuser/dataset/amazon/meta_Grocery_and_Gourmet_Food_dict_feature.json',
        '/home/aiscuser/dataset/amazon/meta_Grocery_and_Gourmet_Food_dict_main_category.json',
        '/home/aiscuser/dataset/amazon/meta_Grocery_and_Gourmet_Food_dict_price.json',
        '/home/aiscuser/dataset/amazon/meta_Grocery_and_Gourmet_Food_dict_Store.json',
        '/home/aiscuser/dataset/amazon/meta_Grocery_and_Gourmet_Food_dict_title.json',
        '/home/aiscuser/dataset/amazon/meta_Handmade_Products_dict_description.json',
        '/home/aiscuser/dataset/amazon/meta_Handmade_Products_dict_feature.json',
        '/home/aiscuser/dataset/amazon/meta_Handmade_Products_dict_main_category.json',
        '/home/aiscuser/dataset/amazon/meta_Handmade_Products_dict_price.json',
        '/home/aiscuser/dataset/amazon/meta_Handmade_Products_dict_Store.json',
        '/home/aiscuser/dataset/amazon/meta_Handmade_Products_dict_title.json',
        '/home/aiscuser/dataset/amazon/meta_Health_and_Household_dict_description.json',
        '/home/aiscuser/dataset/amazon/meta_Health_and_Household_dict_feature.json',
        '/home/aiscuser/dataset/amazon/meta_Health_and_Household_dict_main_category.json',
        '/home/aiscuser/dataset/amazon/meta_Health_and_Household_dict_price.json',
        '/home/aiscuser/dataset/amazon/meta_Health_and_Household_dict_Store.json',
        '/home/aiscuser/dataset/amazon/meta_Health_and_Household_dict_title.json',
        '/home/aiscuser/dataset/amazon/meta_Health_and_Personal_Care_dict_description.json',
        '/home/aiscuser/dataset/amazon/meta_Health_and_Personal_Care_dict_feature.json',
        '/home/aiscuser/dataset/amazon/meta_Health_and_Personal_Care_dict_main_category.json',
        '/home/aiscuser/dataset/amazon/meta_Health_and_Personal_Care_dict_price.json',
        '/home/aiscuser/dataset/amazon/meta_Health_and_Personal_Care_dict_Store.json',
        '/home/aiscuser/dataset/amazon/meta_Health_and_Personal_Care_dict_title.json',
        '/home/aiscuser/dataset/amazon/meta_Home_and_Kitchen_dict_description.json',
        '/home/aiscuser/dataset/amazon/meta_Home_and_Kitchen_dict_feature.json',
        '/home/aiscuser/dataset/amazon/meta_Home_and_Kitchen_dict_main_category.json',
        '/home/aiscuser/dataset/amazon/meta_Home_and_Kitchen_dict_price.json',
        '/home/aiscuser/dataset/amazon/meta_Home_and_Kitchen_dict_Store.json',
        '/home/aiscuser/dataset/amazon/meta_Home_and_Kitchen_dict_title.json',
        '/home/aiscuser/dataset/amazon/meta_Industrial_and_Scientific_dict_description.json',
        '/home/aiscuser/dataset/amazon/meta_Industrial_and_Scientific_dict_feature.json',
        '/home/aiscuser/dataset/amazon/meta_Industrial_and_Scientific_dict_main_category.json',
        '/home/aiscuser/dataset/amazon/meta_Industrial_and_Scientific_dict_price.json',
        '/home/aiscuser/dataset/amazon/meta_Industrial_and_Scientific_dict_Store.json',
        '/home/aiscuser/dataset/amazon/meta_Industrial_and_Scientific_dict_title.json',
        '/home/aiscuser/dataset/amazon/meta_Kindle_Store_dict_description.json',
        '/home/aiscuser/dataset/amazon/meta_Kindle_Store_dict_feature.json',
        '/home/aiscuser/dataset/amazon/meta_Kindle_Store_dict_main_category.json',
        '/home/aiscuser/dataset/amazon/meta_Kindle_Store_dict_price.json',
        '/home/aiscuser/dataset/amazon/meta_Kindle_Store_dict_Store.json',
        '/home/aiscuser/dataset/amazon/meta_Kindle_Store_dict_title.json',
        '/home/aiscuser/dataset/amazon/meta_Magazine_Subscriptions_dict_description.json',
        '/home/aiscuser/dataset/amazon/meta_Magazine_Subscriptions_dict_feature.json',
        '/home/aiscuser/dataset/amazon/meta_Magazine_Subscriptions_dict_main_category.json',
        '/home/aiscuser/dataset/amazon/meta_Magazine_Subscriptions_dict_price.json',
        '/home/aiscuser/dataset/amazon/meta_Magazine_Subscriptions_dict_Store.json',
        '/home/aiscuser/dataset/amazon/meta_Magazine_Subscriptions_dict_title.json',
        '/home/aiscuser/dataset/amazon/meta_Movies_and_TV_dict_description.json',
        '/home/aiscuser/dataset/amazon/meta_Movies_and_TV_dict_feature.json',
        '/home/aiscuser/dataset/amazon/meta_Movies_and_TV_dict_main_category.json',
        '/home/aiscuser/dataset/amazon/meta_Movies_and_TV_dict_price.json',
        '/home/aiscuser/dataset/amazon/meta_Movies_and_TV_dict_Store.json',
        '/home/aiscuser/dataset/amazon/meta_Movies_and_TV_dict_title.json',
        '/home/aiscuser/dataset/amazon/meta_Musical_Instruments_dict_description.json',
        '/home/aiscuser/dataset/amazon/meta_Musical_Instruments_dict_feature.json',
        '/home/aiscuser/dataset/amazon/meta_Musical_Instruments_dict_main_category.json',
        '/home/aiscuser/dataset/amazon/meta_Musical_Instruments_dict_price.json',
        '/home/aiscuser/dataset/amazon/meta_Musical_Instruments_dict_Store.json',
        '/home/aiscuser/dataset/amazon/meta_Musical_Instruments_dict_title.json',
        '/home/aiscuser/dataset/amazon/meta_Office_Products_dict_description.json',
        '/home/aiscuser/dataset/amazon/meta_Office_Products_dict_feature.json',
        '/home/aiscuser/dataset/amazon/meta_Office_Products_dict_main_category.json',
        '/home/aiscuser/dataset/amazon/meta_Office_Products_dict_price.json',
        '/home/aiscuser/dataset/amazon/meta_Office_Products_dict_Store.json',
        '/home/aiscuser/dataset/amazon/meta_Office_Products_dict_title.json',
        '/home/aiscuser/dataset/amazon/meta_Patio_Lawn_and_Garden_dict_description.json',
        '/home/aiscuser/dataset/amazon/meta_Patio_Lawn_and_Garden_dict_feature.json',
        '/home/aiscuser/dataset/amazon/meta_Patio_Lawn_and_Garden_dict_main_category.json',
        '/home/aiscuser/dataset/amazon/meta_Patio_Lawn_and_Garden_dict_price.json',
        '/home/aiscuser/dataset/amazon/meta_Patio_Lawn_and_Garden_dict_Store.json',
        '/home/aiscuser/dataset/amazon/meta_Patio_Lawn_and_Garden_dict_title.json',
        '/home/aiscuser/dataset/amazon/meta_Pet_Supplies_dict_description.json',
        '/home/aiscuser/dataset/amazon/meta_Pet_Supplies_dict_feature.json',
        '/home/aiscuser/dataset/amazon/meta_Pet_Supplies_dict_main_category.json',
        '/home/aiscuser/dataset/amazon/meta_Pet_Supplies_dict_price.json',
        '/home/aiscuser/dataset/amazon/meta_Pet_Supplies_dict_Store.json',
        '/home/aiscuser/dataset/amazon/meta_Pet_Supplies_dict_title.json',
        '/home/aiscuser/dataset/amazon/meta_Software_dict_description.json',
        '/home/aiscuser/dataset/amazon/meta_Software_dict_feature.json',
        '/home/aiscuser/dataset/amazon/meta_Software_dict_main_category.json',
        '/home/aiscuser/dataset/amazon/meta_Software_dict_price.json',
        '/home/aiscuser/dataset/amazon/meta_Software_dict_Store.json',
        '/home/aiscuser/dataset/amazon/meta_Software_dict_title.json',
        '/home/aiscuser/dataset/amazon/meta_Sports_and_Outdoors_dict_description.json',
        '/home/aiscuser/dataset/amazon/meta_Sports_and_Outdoors_dict_feature.json',
        '/home/aiscuser/dataset/amazon/meta_Sports_and_Outdoors_dict_main_category.json',
        '/home/aiscuser/dataset/amazon/meta_Sports_and_Outdoors_dict_price.json',
        '/home/aiscuser/dataset/amazon/meta_Sports_and_Outdoors_dict_Store.json',
        '/home/aiscuser/dataset/amazon/meta_Sports_and_Outdoors_dict_title.json',
        '/home/aiscuser/dataset/amazon/meta_Subscription_Boxes_dict_description.json',
        '/home/aiscuser/dataset/amazon/meta_Subscription_Boxes_dict_feature.json',
        '/home/aiscuser/dataset/amazon/meta_Subscription_Boxes_dict_main_category.json',
        '/home/aiscuser/dataset/amazon/meta_Subscription_Boxes_dict_price.json',
        '/home/aiscuser/dataset/amazon/meta_Subscription_Boxes_dict_Store.json',
        '/home/aiscuser/dataset/amazon/meta_Subscription_Boxes_dict_title.json',
        '/home/aiscuser/dataset/amazon/meta_Tools_and_Home_Improvement_dict_description.json',
        '/home/aiscuser/dataset/amazon/meta_Tools_and_Home_Improvement_dict_feature.json',
        '/home/aiscuser/dataset/amazon/meta_Tools_and_Home_Improvement_dict_main_category.json',
        '/home/aiscuser/dataset/amazon/meta_Tools_and_Home_Improvement_dict_price.json',
        '/home/aiscuser/dataset/amazon/meta_Tools_and_Home_Improvement_dict_Store.json',
        '/home/aiscuser/dataset/amazon/meta_Tools_and_Home_Improvement_dict_title.json',
        '/home/aiscuser/dataset/amazon/meta_Toys_and_Games_dict_description.json',
        '/home/aiscuser/dataset/amazon/meta_Toys_and_Games_dict_feature.json',
        '/home/aiscuser/dataset/amazon/meta_Toys_and_Games_dict_main_category.json',
        '/home/aiscuser/dataset/amazon/meta_Toys_and_Games_dict_price.json',
        '/home/aiscuser/dataset/amazon/meta_Toys_and_Games_dict_Store.json',
        '/home/aiscuser/dataset/amazon/meta_Toys_and_Games_dict_title.json',
        '/home/aiscuser/dataset/amazon/meta_Video_Games_dict_description.json',
        '/home/aiscuser/dataset/amazon/meta_Video_Games_dict_feature.json',
        '/home/aiscuser/dataset/amazon/meta_Video_Games_dict_main_category.json',
        '/home/aiscuser/dataset/amazon/meta_Video_Games_dict_price.json',
        '/home/aiscuser/dataset/amazon/meta_Video_Games_dict_Store.json',
        '/home/aiscuser/dataset/amazon/meta_Video_Games_dict_title.json',
    ]









    for index in range(len(file_paths)):

        print(file_paths[index])
        
        with open(file_paths[index], 'r') as file:
            original_dict = json.load(file)

        # # 打印原始字典的所有键
        # print("Original dict keys:")
        # for key in original_dict.keys():
        #     print(key)

        # import ipdb; ipdb.set_trace()
        jpg_set = get_jpg_filenames(folder_paths[0])
        # print(jpg_set)

        # import ipdb; ipdb.set_trace()
        # 打印原始字典的长度
        print(f"Original dict length: {len(original_dict)}")
        
        # 过滤字典
        filtered_dict = {k: v for k, v in original_dict.items() if k in jpg_set}

        # 打印过滤后字典的长度
        print(f"Filtered dict length: {len(filtered_dict)}")

        # 将过滤后的字典写回文件
        with open(file_paths[index], 'w') as file:
            json.dump(filtered_dict, file, indent=4)





# /home/aiscuser/dataset/amazon/meta_All_Beauty_dict_description.json
# Original dict length: 81049
# Filtered dict length: 81049
# /home/aiscuser/dataset/amazon/meta_All_Beauty_dict_feature.json
# Original dict length: 81049
# Filtered dict length: 81049
# /home/aiscuser/dataset/amazon/meta_All_Beauty_dict_main_category.json
# Original dict length: 81049
# Filtered dict length: 81049
# /home/aiscuser/dataset/amazon/meta_All_Beauty_dict_price.json
# Original dict length: 81049
# Filtered dict length: 81049
# /home/aiscuser/dataset/amazon/meta_All_Beauty_dict_Store.json
# Original dict length: 81049
# Filtered dict length: 81049
# /home/aiscuser/dataset/amazon/meta_All_Beauty_dict_title.json
# Original dict length: 81049
# Filtered dict length: 81049
# /home/aiscuser/dataset/amazon/meta_Amazon_Fashion_dict_description.json
# Original dict length: 527
# Filtered dict length: 527
# /home/aiscuser/dataset/amazon/meta_Amazon_Fashion_dict_feature.json
# Original dict length: 527
# Filtered dict length: 527
# /home/aiscuser/dataset/amazon/meta_Amazon_Fashion_dict_main_category.json
# Original dict length: 527
# Filtered dict length: 527
# /home/aiscuser/dataset/amazon/meta_Amazon_Fashion_dict_price.json
# Original dict length: 527
# Filtered dict length: 527
# /home/aiscuser/dataset/amazon/meta_Amazon_Fashion_dict_Store.json
# Original dict length: 527
# Filtered dict length: 527
# /home/aiscuser/dataset/amazon/meta_Amazon_Fashion_dict_title.json
# Original dict length: 527
# Filtered dict length: 527
# /home/aiscuser/dataset/amazon/meta_Appliances_dict_description.json
# Original dict length: 63571
# Filtered dict length: 63571
# /home/aiscuser/dataset/amazon/meta_Appliances_dict_feature.json
# Original dict length: 63571
# Filtered dict length: 63571
# /home/aiscuser/dataset/amazon/meta_Appliances_dict_main_category.json
# Original dict length: 63571
# Filtered dict length: 63571
# /home/aiscuser/dataset/amazon/meta_Appliances_dict_price.json
# Original dict length: 63571
# Filtered dict length: 63571
# /home/aiscuser/dataset/amazon/meta_Appliances_dict_Store.json
# Original dict length: 63571
# Filtered dict length: 63571
# /home/aiscuser/dataset/amazon/meta_Appliances_dict_title.json
# Original dict length: 63571
# Filtered dict length: 63571
# /home/aiscuser/dataset/amazon/meta_Arts_Crafts_and_Sewing_dict_description.json
# Original dict length: 303
# Filtered dict length: 303
# /home/aiscuser/dataset/amazon/meta_Arts_Crafts_and_Sewing_dict_feature.json
# Original dict length: 303
# Filtered dict length: 303
# /home/aiscuser/dataset/amazon/meta_Arts_Crafts_and_Sewing_dict_main_category.json
# Original dict length: 303
# Filtered dict length: 303
# /home/aiscuser/dataset/amazon/meta_Arts_Crafts_and_Sewing_dict_price.json
# Original dict length: 303
# Filtered dict length: 303
# /home/aiscuser/dataset/amazon/meta_Arts_Crafts_and_Sewing_dict_Store.json
# Original dict length: 303
# Filtered dict length: 303
# /home/aiscuser/dataset/amazon/meta_Arts_Crafts_and_Sewing_dict_title.json
# Original dict length: 303
# Filtered dict length: 303
# /home/aiscuser/dataset/amazon/meta_Automotive_dict_description.json
# Original dict length: 382
# Filtered dict length: 382
# /home/aiscuser/dataset/amazon/meta_Automotive_dict_feature.json
# Original dict length: 382
# Filtered dict length: 382
# /home/aiscuser/dataset/amazon/meta_Automotive_dict_main_category.json
# Original dict length: 382
# Filtered dict length: 382
# /home/aiscuser/dataset/amazon/meta_Automotive_dict_price.json
# Original dict length: 382
# Filtered dict length: 382
# /home/aiscuser/dataset/amazon/meta_Automotive_dict_Store.json
# Original dict length: 382
# Filtered dict length: 382
# /home/aiscuser/dataset/amazon/meta_Automotive_dict_title.json
# Original dict length: 382
# Filtered dict length: 382
# /home/aiscuser/dataset/amazon/meta_Baby_Products_dict_description.json
# Original dict length: 174250
# Filtered dict length: 174250
# /home/aiscuser/dataset/amazon/meta_Baby_Products_dict_description.json
# Original dict length: 174250
# Filtered dict length: 174250
# /home/aiscuser/dataset/amazon/meta_Baby_Products_dict_feature.json
# Original dict length: 174250
# Filtered dict length: 174250
# /home/aiscuser/dataset/amazon/meta_Baby_Products_dict_main_category.json
# Original dict length: 174250
# Filtered dict length: 174250
# /home/aiscuser/dataset/amazon/meta_Baby_Products_dict_price.json
# Original dict length: 174250
# Filtered dict length: 174250
# /home/aiscuser/dataset/amazon/meta_Baby_Products_dict_Store.json
# Original dict length: 174250
# Filtered dict length: 174250
# /home/aiscuser/dataset/amazon/meta_Baby_Products_dict_title.json
# Original dict length: 174250
# Filtered dict length: 174250
# /home/aiscuser/dataset/amazon/meta_Beauty_and_Personal_Care_dict_description.json
# Original dict length: 5314
# Filtered dict length: 5314
# /home/aiscuser/dataset/amazon/meta_Beauty_and_Personal_Care_dict_feature.json
# Original dict length: 5314
# Filtered dict length: 5314
# /home/aiscuser/dataset/amazon/meta_Beauty_and_Personal_Care_dict_main_category.json
# Original dict length: 5314
# Filtered dict length: 5314
# /home/aiscuser/dataset/amazon/meta_Beauty_and_Personal_Care_dict_price.json
# Original dict length: 5314
# Filtered dict length: 5314
# /home/aiscuser/dataset/amazon/meta_Beauty_and_Personal_Care_dict_Store.json
# Original dict length: 5314
# Filtered dict length: 5314
# /home/aiscuser/dataset/amazon/meta_Beauty_and_Personal_Care_dict_title.json
# Original dict length: 5314
# Filtered dict length: 5314
# /home/aiscuser/dataset/amazon/meta_Books_dict_description.json
# Original dict length: 2522
# Filtered dict length: 2498
# /home/aiscuser/dataset/amazon/meta_Books_dict_feature.json
# Original dict length: 2522
# Filtered dict length: 2498
# /home/aiscuser/dataset/amazon/meta_Books_dict_main_category.json
# Original dict length: 2522
# Filtered dict length: 2498
# /home/aiscuser/dataset/amazon/meta_Books_dict_price.json
# Original dict length: 2522
# Filtered dict length: 2498
# /home/aiscuser/dataset/amazon/meta_Books_dict_Store.json
# Original dict length: 2522
# Filtered dict length: 2498
# /home/aiscuser/dataset/amazon/meta_Books_dict_title.json
# Original dict length: 2522
# Filtered dict length: 2498
# /home/aiscuser/dataset/amazon/meta_CDs_and_Vinyl_dict_description.json
# Original dict length: 317946
# Filtered dict length: 302
# /home/aiscuser/dataset/amazon/meta_CDs_and_Vinyl_dict_feature.json
# Original dict length: 317946
# Filtered dict length: 302
# /home/aiscuser/dataset/amazon/meta_CDs_and_Vinyl_dict_main_category.json
# Original dict length: 317946
# Filtered dict length: 302
# /home/aiscuser/dataset/amazon/meta_CDs_and_Vinyl_dict_price.json
# Original dict length: 317946
# Filtered dict length: 302
# /home/aiscuser/dataset/amazon/meta_CDs_and_Vinyl_dict_Store.json
# Original dict length: 317946
# Filtered dict length: 302
# /home/aiscuser/dataset/amazon/meta_CDs_and_Vinyl_dict_title.json
# Original dict length: 317946
# Filtered dict length: 302
# /home/aiscuser/dataset/amazon/meta_Cell_Phones_and_Accessories_dict_description.json
# Original dict length: 963241
# Filtered dict length: 590
# /home/aiscuser/dataset/amazon/meta_Cell_Phones_and_Accessories_dict_feature.json
# Original dict length: 963241
# Filtered dict length: 590
# /home/aiscuser/dataset/amazon/meta_Cell_Phones_and_Accessories_dict_main_category.json
# Original dict length: 963241
# Filtered dict length: 590
# /home/aiscuser/dataset/amazon/meta_Cell_Phones_and_Accessories_dict_price.json
# Original dict length: 963241
# Filtered dict length: 590
# /home/aiscuser/dataset/amazon/meta_Cell_Phones_and_Accessories_dict_Store.json
# Original dict length: 963241
# Filtered dict length: 590
# /home/aiscuser/dataset/amazon/meta_Cell_Phones_and_Accessories_dict_title.json
# Original dict length: 963241
# Filtered dict length: 590
# /home/aiscuser/dataset/amazon/meta_Clothing_Shoes_and_Jewelry_dict_description.json
# Original dict length: 4690882
# Filtered dict length: 911
# /home/aiscuser/dataset/amazon/meta_Clothing_Shoes_and_Jewelry_dict_feature.json
# Original dict length: 4690882
# Filtered dict length: 911
# /home/aiscuser/dataset/amazon/meta_Clothing_Shoes_and_Jewelry_dict_main_category.json
# Original dict length: 4690882
# Filtered dict length: 911
# /home/aiscuser/dataset/amazon/meta_Clothing_Shoes_and_Jewelry_dict_price.json
# Original dict length: 4690882
# Filtered dict length: 911
# /home/aiscuser/dataset/amazon/meta_Clothing_Shoes_and_Jewelry_dict_Store.json
# Original dict length: 4690882
# Filtered dict length: 911
# /home/aiscuser/dataset/amazon/meta_Clothing_Shoes_and_Jewelry_dict_title.json
# Original dict length: 4690882
# Filtered dict length: 911
# /home/aiscuser/dataset/amazon/meta_Digital_Music_dict_description.json
# Original dict length: 25606
# Filtered dict length: 25547
# /home/aiscuser/dataset/amazon/meta_Digital_Music_dict_feature.json
# Original dict length: 25606
# Filtered dict length: 25547
# /home/aiscuser/dataset/amazon/meta_Digital_Music_dict_main_category.json
# Original dict length: 25606
# Filtered dict length: 25547
# /home/aiscuser/dataset/amazon/meta_Digital_Music_dict_price.json
# Original dict length: 25606
# Filtered dict length: 25547
# /home/aiscuser/dataset/amazon/meta_Digital_Music_dict_Store.json
# Original dict length: 25606
# Filtered dict length: 25547
# /home/aiscuser/dataset/amazon/meta_Digital_Music_dict_title.json
# Original dict length: 25606
# Filtered dict length: 25547
# /home/aiscuser/dataset/amazon/meta_Electronics_dict_description.json
# Original dict length: 1091662
# Filtered dict length: 1852
# /home/aiscuser/dataset/amazon/meta_Electronics_dict_feature.json
# Original dict length: 1091662
# Filtered dict length: 1852
# /home/aiscuser/dataset/amazon/meta_Electronics_dict_main_category.json
# Original dict length: 1091662
# Filtered dict length: 1852
# /home/aiscuser/dataset/amazon/meta_Electronics_dict_price.json
# Original dict length: 1091662
# Filtered dict length: 1852
# /home/aiscuser/dataset/amazon/meta_Electronics_dict_Store.json
# Original dict length: 1091662
# Filtered dict length: 1852
# /home/aiscuser/dataset/amazon/meta_Electronics_dict_title.json
# Original dict length: 1091662
# Filtered dict length: 1852
# /home/aiscuser/dataset/amazon/meta_Gift_Cards_dict_description.json
# Original dict length: 567
# Filtered dict length: 566
# /home/aiscuser/dataset/amazon/meta_Gift_Cards_dict_feature.json
# Original dict length: 567
# Filtered dict length: 566
# /home/aiscuser/dataset/amazon/meta_Gift_Cards_dict_main_category.json
# Original dict length: 567
# Filtered dict length: 566
# /home/aiscuser/dataset/amazon/meta_Gift_Cards_dict_price.json
# Original dict length: 567
# Filtered dict length: 566
# /home/aiscuser/dataset/amazon/meta_Gift_Cards_dict_Store.json
# Original dict length: 567
# Filtered dict length: 566
# /home/aiscuser/dataset/amazon/meta_Gift_Cards_dict_title.json
# Original dict length: 567
# Filtered dict length: 566
# /home/aiscuser/dataset/amazon/meta_Grocery_and_Gourmet_Food_dict_description.json
# Original dict length: 448765
# Filtered dict length: 248
# /home/aiscuser/dataset/amazon/meta_Grocery_and_Gourmet_Food_dict_feature.json
# Original dict length: 448765
# Filtered dict length: 248
# /home/aiscuser/dataset/amazon/meta_Grocery_and_Gourmet_Food_dict_main_category.json
# Original dict length: 448765
# Filtered dict length: 248
# /home/aiscuser/dataset/amazon/meta_Grocery_and_Gourmet_Food_dict_price.json
# Original dict length: 448765
# Filtered dict length: 248
# /home/aiscuser/dataset/amazon/meta_Grocery_and_Gourmet_Food_dict_Store.json
# Original dict length: 448765
# Filtered dict length: 248
# /home/aiscuser/dataset/amazon/meta_Grocery_and_Gourmet_Food_dict_title.json
# Original dict length: 448765
# Filtered dict length: 248
# /home/aiscuser/dataset/amazon/meta_Handmade_Products_dict_description.json
# Original dict length: 136093
# Filtered dict length: 132688
# /home/aiscuser/dataset/amazon/meta_Handmade_Products_dict_feature.json
# Original dict length: 136093
# Filtered dict length: 132688
# /home/aiscuser/dataset/amazon/meta_Handmade_Products_dict_main_category.json
# Original dict length: 136093
# Filtered dict length: 132688
# /home/aiscuser/dataset/amazon/meta_Handmade_Products_dict_price.json
# Original dict length: 136093
# Filtered dict length: 132688
# /home/aiscuser/dataset/amazon/meta_Handmade_Products_dict_Store.json
# Original dict length: 136093
# Filtered dict length: 132688
# /home/aiscuser/dataset/amazon/meta_Handmade_Products_dict_title.json
# Original dict length: 136093
# Filtered dict length: 132688
# /home/aiscuser/dataset/amazon/meta_Health_and_Household_dict_description.json
# Original dict length: 595486
# Filtered dict length: 2361
# /home/aiscuser/dataset/amazon/meta_Health_and_Household_dict_feature.json
# Original dict length: 595486
# Filtered dict length: 2361
# /home/aiscuser/dataset/amazon/meta_Health_and_Household_dict_main_category.json
# Original dict length: 595486
# Filtered dict length: 2361
# /home/aiscuser/dataset/amazon/meta_Health_and_Household_dict_price.json
# Original dict length: 595486
# Filtered dict length: 2361
# /home/aiscuser/dataset/amazon/meta_Health_and_Household_dict_Store.json
# Original dict length: 595486
# Filtered dict length: 2361
# /home/aiscuser/dataset/amazon/meta_Health_and_Household_dict_title.json
# Original dict length: 595486
# Filtered dict length: 2361
# /home/aiscuser/dataset/amazon/meta_Health_and_Personal_Care_dict_description.json
# Original dict length: 43768
# Filtered dict length: 42667
# /home/aiscuser/dataset/amazon/meta_Health_and_Personal_Care_dict_feature.json
# Original dict length: 43768
# Filtered dict length: 42667
# /home/aiscuser/dataset/amazon/meta_Health_and_Personal_Care_dict_main_category.json
# Original dict length: 43768
# Filtered dict length: 42667
# /home/aiscuser/dataset/amazon/meta_Health_and_Personal_Care_dict_price.json
# Original dict length: 43768
# Filtered dict length: 42667
# /home/aiscuser/dataset/amazon/meta_Health_and_Personal_Care_dict_Store.json
# Original dict length: 43768
# Filtered dict length: 42667
# /home/aiscuser/dataset/amazon/meta_Health_and_Personal_Care_dict_title.json
# Original dict length: 43768
# Filtered dict length: 42667
# /home/aiscuser/dataset/amazon/meta_Home_and_Kitchen_dict_description.json
# Original dict length: 2976745
# Filtered dict length: 1935
# /home/aiscuser/dataset/amazon/meta_Home_and_Kitchen_dict_feature.json
# Original dict length: 2976745
# Filtered dict length: 1935
# /home/aiscuser/dataset/amazon/meta_Home_and_Kitchen_dict_main_category.json
# Original dict length: 2976745
# Filtered dict length: 1935
# /home/aiscuser/dataset/amazon/meta_Home_and_Kitchen_dict_price.json
# Original dict length: 2976745
# Filtered dict length: 1935
# /home/aiscuser/dataset/amazon/meta_Home_and_Kitchen_dict_Store.json
# Original dict length: 2976745
# Filtered dict length: 1935
# /home/aiscuser/dataset/amazon/meta_Home_and_Kitchen_dict_title.json
# Original dict length: 2976745
# Filtered dict length: 1935
# /home/aiscuser/dataset/amazon/meta_Industrial_and_Scientific_dict_description.json
# Original dict length: 305274
# Filtered dict length: 501
# /home/aiscuser/dataset/amazon/meta_Industrial_and_Scientific_dict_feature.json
# Original dict length: 305274
# Filtered dict length: 501
# /home/aiscuser/dataset/amazon/meta_Industrial_and_Scientific_dict_main_category.json
# Original dict length: 305274
# Filtered dict length: 501
# /home/aiscuser/dataset/amazon/meta_Industrial_and_Scientific_dict_price.json
# Original dict length: 305274
# Filtered dict length: 501
# /home/aiscuser/dataset/amazon/meta_Industrial_and_Scientific_dict_Store.json
# Original dict length: 305274
# Filtered dict length: 501
# /home/aiscuser/dataset/amazon/meta_Industrial_and_Scientific_dict_title.json
# Original dict length: 305274
# Filtered dict length: 501
# /home/aiscuser/dataset/amazon/meta_Kindle_Store_dict_description.json
# Original dict length: 8314
# Filtered dict length: 8312
# /home/aiscuser/dataset/amazon/meta_Kindle_Store_dict_feature.json
# Original dict length: 8314
# Filtered dict length: 8312
# /home/aiscuser/dataset/amazon/meta_Kindle_Store_dict_main_category.json
# Original dict length: 8314
# Filtered dict length: 8312
# /home/aiscuser/dataset/amazon/meta_Kindle_Store_dict_price.json
# Original dict length: 8314
# Filtered dict length: 8312
# /home/aiscuser/dataset/amazon/meta_Kindle_Store_dict_Store.json
# Original dict length: 8314
# Filtered dict length: 8312
# /home/aiscuser/dataset/amazon/meta_Kindle_Store_dict_title.json
# Original dict length: 8314
# Filtered dict length: 8312
# /home/aiscuser/dataset/amazon/meta_Magazine_Subscriptions_dict_description.json
# Original dict length: 1184
# Filtered dict length: 1184
# /home/aiscuser/dataset/amazon/meta_Magazine_Subscriptions_dict_feature.json
# Original dict length: 1184
# Filtered dict length: 1184
# /home/aiscuser/dataset/amazon/meta_Magazine_Subscriptions_dict_main_category.json
# Original dict length: 1184
# Filtered dict length: 1184
# /home/aiscuser/dataset/amazon/meta_Magazine_Subscriptions_dict_price.json
# Original dict length: 1184
# Filtered dict length: 1184
# /home/aiscuser/dataset/amazon/meta_Magazine_Subscriptions_dict_Store.json
# Original dict length: 1184
# Filtered dict length: 1184
# /home/aiscuser/dataset/amazon/meta_Magazine_Subscriptions_dict_title.json
# Original dict length: 1184
# Filtered dict length: 1184
# /home/aiscuser/dataset/amazon/meta_Movies_and_TV_dict_description.json
# Original dict length: 186453
# Filtered dict length: 186342
# /home/aiscuser/dataset/amazon/meta_Movies_and_TV_dict_feature.json
# Original dict length: 186453
# Filtered dict length: 186342
# /home/aiscuser/dataset/amazon/meta_Movies_and_TV_dict_main_category.json
# Original dict length: 186453
# Filtered dict length: 186342
# /home/aiscuser/dataset/amazon/meta_Movies_and_TV_dict_price.json
# Original dict length: 186453
# Filtered dict length: 186342
# /home/aiscuser/dataset/amazon/meta_Movies_and_TV_dict_Store.json
# Original dict length: 186453
# Filtered dict length: 186342
# /home/aiscuser/dataset/amazon/meta_Movies_and_TV_dict_title.json
# Original dict length: 186453
# Filtered dict length: 186342
# /home/aiscuser/dataset/amazon/meta_Musical_Instruments_dict_description.json
# Original dict length: 164220
# Filtered dict length: 158452
# /home/aiscuser/dataset/amazon/meta_Musical_Instruments_dict_feature.json
# Original dict length: 164220
# Filtered dict length: 158452
# /home/aiscuser/dataset/amazon/meta_Musical_Instruments_dict_main_category.json
# Original dict length: 164220
# Filtered dict length: 158452
# /home/aiscuser/dataset/amazon/meta_Musical_Instruments_dict_price.json
# Original dict length: 164220
# Filtered dict length: 158452
# /home/aiscuser/dataset/amazon/meta_Musical_Instruments_dict_Store.json
# Original dict length: 164220
# Filtered dict length: 158452
# /home/aiscuser/dataset/amazon/meta_Musical_Instruments_dict_title.json
# Original dict length: 164220
# Filtered dict length: 158452
# /home/aiscuser/dataset/amazon/meta_Office_Products_dict_description.json
# Original dict length: 543578
# Filtered dict length: 350
# /home/aiscuser/dataset/amazon/meta_Office_Products_dict_feature.json
# Original dict length: 543578
# Filtered dict length: 350
# /home/aiscuser/dataset/amazon/meta_Office_Products_dict_main_category.json
# Original dict length: 543578
# Filtered dict length: 350
# /home/aiscuser/dataset/amazon/meta_Office_Products_dict_price.json
# Original dict length: 543578
# Filtered dict length: 350
# /home/aiscuser/dataset/amazon/meta_Office_Products_dict_Store.json
# Original dict length: 543578
# Filtered dict length: 350
# /home/aiscuser/dataset/amazon/meta_Office_Products_dict_title.json
# Original dict length: 543578
# Filtered dict length: 350
# /home/aiscuser/dataset/amazon/meta_Patio_Lawn_and_Garden_dict_description.json
# Original dict length: 651705
# Filtered dict length: 302
# /home/aiscuser/dataset/amazon/meta_Patio_Lawn_and_Garden_dict_feature.json
# Original dict length: 651705
# Filtered dict length: 302
# /home/aiscuser/dataset/amazon/meta_Patio_Lawn_and_Garden_dict_main_category.json
# Original dict length: 651705
# Filtered dict length: 302
# /home/aiscuser/dataset/amazon/meta_Patio_Lawn_and_Garden_dict_price.json
# Original dict length: 651705
# Filtered dict length: 302
# /home/aiscuser/dataset/amazon/meta_Patio_Lawn_and_Garden_dict_Store.json
# Original dict length: 651705
# Filtered dict length: 302
# /home/aiscuser/dataset/amazon/meta_Patio_Lawn_and_Garden_dict_title.json
# Original dict length: 651705
# Filtered dict length: 302
# /home/aiscuser/dataset/amazon/meta_Pet_Supplies_dict_description.json
# Original dict length: 377364
# Filtered dict length: 278
# /home/aiscuser/dataset/amazon/meta_Pet_Supplies_dict_feature.json
# Original dict length: 377364
# Filtered dict length: 278
# /home/aiscuser/dataset/amazon/meta_Pet_Supplies_dict_main_category.json
# Original dict length: 377364
# Filtered dict length: 278
# /home/aiscuser/dataset/amazon/meta_Pet_Supplies_dict_price.json
# Original dict length: 377364
# Filtered dict length: 278
# /home/aiscuser/dataset/amazon/meta_Pet_Supplies_dict_Store.json
# Original dict length: 377364
# Filtered dict length: 278
# /home/aiscuser/dataset/amazon/meta_Pet_Supplies_dict_title.json
# Original dict length: 377364
# Filtered dict length: 278
# /home/aiscuser/dataset/amazon/meta_Software_dict_description.json
# Original dict length: 7765
# Filtered dict length: 7745
# /home/aiscuser/dataset/amazon/meta_Software_dict_feature.json
# Original dict length: 7765
# Filtered dict length: 7745
# /home/aiscuser/dataset/amazon/meta_Software_dict_main_category.json
# Original dict length: 7765
# Filtered dict length: 7745
# /home/aiscuser/dataset/amazon/meta_Software_dict_price.json
# Original dict length: 7765
# Filtered dict length: 7745
# /home/aiscuser/dataset/amazon/meta_Software_dict_Store.json
# Original dict length: 7765
# Filtered dict length: 7745
# /home/aiscuser/dataset/amazon/meta_Software_dict_title.json
# Original dict length: 7765
# Filtered dict length: 7745
# /home/aiscuser/dataset/amazon/meta_Sports_and_Outdoors_dict_description.json
# Original dict length: 1150673
# Filtered dict length: 513
# /home/aiscuser/dataset/amazon/meta_Sports_and_Outdoors_dict_feature.json
# Original dict length: 1150673
# Filtered dict length: 513
# /home/aiscuser/dataset/amazon/meta_Sports_and_Outdoors_dict_main_category.json
# Original dict length: 1150673
# Filtered dict length: 513
# /home/aiscuser/dataset/amazon/meta_Sports_and_Outdoors_dict_price.json
# Original dict length: 1150673
# Filtered dict length: 513
# /home/aiscuser/dataset/amazon/meta_Sports_and_Outdoors_dict_Store.json
# Original dict length: 1150673
# Filtered dict length: 513
# /home/aiscuser/dataset/amazon/meta_Sports_and_Outdoors_dict_title.json
# Original dict length: 1150673
# Filtered dict length: 513
# /home/aiscuser/dataset/amazon/meta_Subscription_Boxes_dict_description.json
# Original dict length: 413
# Filtered dict length: 410
# /home/aiscuser/dataset/amazon/meta_Subscription_Boxes_dict_feature.json
# Original dict length: 413
# Filtered dict length: 410
# /home/aiscuser/dataset/amazon/meta_Subscription_Boxes_dict_main_category.json
# Original dict length: 413
# Filtered dict length: 410
# /home/aiscuser/dataset/amazon/meta_Subscription_Boxes_dict_price.json
# Original dict length: 413
# Filtered dict length: 410
# /home/aiscuser/dataset/amazon/meta_Subscription_Boxes_dict_Store.json
# Original dict length: 413
# Filtered dict length: 410
# /home/aiscuser/dataset/amazon/meta_Subscription_Boxes_dict_title.json
# Original dict length: 413
# Filtered dict length: 410
# /home/aiscuser/dataset/amazon/meta_Tools_and_Home_Improvement_dict_description.json
# Original dict length: 1136421
# Filtered dict length: 1030
# /home/aiscuser/dataset/amazon/meta_Tools_and_Home_Improvement_dict_feature.json
# Original dict length: 1136421
# Filtered dict length: 1030
# /home/aiscuser/dataset/amazon/meta_Tools_and_Home_Improvement_dict_main_category.json
# Original dict length: 1136421
# Filtered dict length: 1030
# /home/aiscuser/dataset/amazon/meta_Tools_and_Home_Improvement_dict_price.json
# Original dict length: 1136421
# Filtered dict length: 1030
# /home/aiscuser/dataset/amazon/meta_Tools_and_Home_Improvement_dict_Store.json
# Original dict length: 1136421
# Filtered dict length: 1030
# /home/aiscuser/dataset/amazon/meta_Tools_and_Home_Improvement_dict_title.json
# Original dict length: 1136421
# Filtered dict length: 1030
# /home/aiscuser/dataset/amazon/meta_Toys_and_Games_dict_description.json
# Original dict length: 703820
# Filtered dict length: 386
# /home/aiscuser/dataset/amazon/meta_Toys_and_Games_dict_feature.json
# Original dict length: 703820
# Filtered dict length: 386
# /home/aiscuser/dataset/amazon/meta_Toys_and_Games_dict_main_category.json
# Original dict length: 703820
# Filtered dict length: 386
# /home/aiscuser/dataset/amazon/meta_Toys_and_Games_dict_price.json
# Original dict length: 703820
# Filtered dict length: 386
# /home/aiscuser/dataset/amazon/meta_Toys_and_Games_dict_Store.json
# Original dict length: 703820
# Filtered dict length: 386
# /home/aiscuser/dataset/amazon/meta_Toys_and_Games_dict_title.json
# Original dict length: 703820
# Filtered dict length: 386
# /home/aiscuser/dataset/amazon/meta_Video_Games_dict_description.json
# Original dict length: 90188
# Filtered dict length: 89037
# /home/aiscuser/dataset/amazon/meta_Video_Games_dict_feature.json
# Original dict length: 90188
# Filtered dict length: 89037
# /home/aiscuser/dataset/amazon/meta_Video_Games_dict_main_category.json
# Original dict length: 90188
# Filtered dict length: 89037
# /home/aiscuser/dataset/amazon/meta_Video_Games_dict_price.json
# Original dict length: 90188
# Filtered dict length: 89037
# /home/aiscuser/dataset/amazon/meta_Video_Games_dict_Store.json
# Original dict length: 90188
# Filtered dict length: 89037
# /home/aiscuser/dataset/amazon/meta_Video_Games_dict_title.json
# Original dict length: 90188
# Filtered dict length: 89037
