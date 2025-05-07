pip install huggingface_hub
export HF_TOKEN=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
huggingface-cli login --token $HF_TOKEN

mkdir ./msdata/split_small
huggingface-cli download wei682/split_small --repo-type dataset --local-dir ./msdata/split_small
# huggingface-cli download wei682/amazon-grpo --repo-type dataset --local-dir /cpfs01/shared/llm_ddd/zhangyulong/sa_work/msdata/grpo_data


mkdir ./wei682/split_small_small
huggingface-cli download wei682/split_small_small --repo-type dataset --local-dir ./msdata/split_small_small
