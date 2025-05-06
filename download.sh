pip install huggingface_hub
export HF_TOKEN=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
huggingface-cli login --token $HF_TOKEN

huggingface-cli download wei682/amazon-grpo --repo-type dataset --local-dir ./msdata/grpo_v1
# huggingface-cli download wei682/amazon-grpo --repo-type dataset --local-dir ./cpfs01/shared/llm_ddd/zhangyulong/sa_work/msdata/grpo_data
