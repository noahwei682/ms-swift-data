pip install huggingface_hub
export HF_TOKEN=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
huggingface-cli login --token $HF_TOKEN

huggingface-cli upload amazon-grpo meta_All_Beauty_dict_title_grpo.json --repo-type dataset
huggingface-cli upload amazon-grpo meta_Amazon_Fashion_dict_title_grpo.json --repo-type dataset
huggingface-cli upload amazon-grpo meta_Appliances_dict_title_grpo.json --repo-type dataset
huggingface-cli upload amazon-grpo meta_Arts_Crafts_and_Sewing_dict_title_grpo.json --repo-type dataset
huggingface-cli upload amazon-grpo meta_Automotive_dict_title_grpo.json --repo-type dataset
huggingface-cli upload amazon-grpo meta_Baby_Products_dict_title_grpo.json --repo-type dataset
huggingface-cli upload amazon-grpo meta_Beauty_and_Personal_Care_dict_title_grpo.json --repo-type dataset
huggingface-cli upload amazon-grpo meta_Books_dict_title_grpo.json --repo-type dataset
huggingface-cli upload amazon-grpo meta_CDs_and_Vinyl_dict_title_grpo.json --repo-type dataset
huggingface-cli upload amazon-grpo meta_Cell_Phones_and_Accessories_dict_title_grpo.json --repo-type dataset
huggingface-cli upload amazon-grpo meta_Clothing_Shoes_and_Jewelry_dict_title_grpo.json --repo-type dataset
huggingface-cli upload amazon-grpo meta_Digital_Music_dict_title_grpo.json --repo-type dataset
huggingface-cli upload amazon-grpo meta_Electronics_dict_title_grpo.json --repo-type dataset
huggingface-cli upload amazon-grpo meta_Gift_Cards_dict_title_grpo.json --repo-type dataset
huggingface-cli upload amazon-grpo meta_Grocery_and_Gourmet_Food_dict_title.json --repo-type dataset
huggingface-cli upload amazon-grpo meta_Handmade_Products_dict_title_grpo.json --repo-type dataset
huggingface-cli upload amazon-grpo meta_Health_and_Household_dict_title_grpo.json --repo-type dataset
huggingface-cli upload amazon-grpo meta_Health_and_Personal_Care_dict_title_grpo.json --repo-type dataset
huggingface-cli upload amazon-grpo meta_Home_and_Kitchen_dict_title_grpo.json --repo-type dataset
huggingface-cli upload amazon-grpo meta_Industrial_and_Scientific_dict_title_grpo.json --repo-type dataset
huggingface-cli upload amazon-grpo meta_Kindle_Store_dict_title_grpo.json --repo-type dataset
huggingface-cli upload amazon-grpo meta_Magazine_Subscriptions_dict_title_grpo.json --repo-type dataset
huggingface-cli upload amazon-grpo meta_Movies_and_TV_dict_title_grpo.json --repo-type dataset
huggingface-cli upload amazon-grpo meta_Musical_Instruments_dict_title_grpo.json --repo-type dataset
huggingface-cli upload amazon-grpo meta_Office_Products_dict_title_grpo.json --repo-type dataset
huggingface-cli upload amazon-grpo meta_Patio_Lawn_and_Garden_dict_title_grpo.json --repo-type dataset
huggingface-cli upload amazon-grpo meta_Pet_Supplies_dict_title_grpo.json --repo-type dataset

