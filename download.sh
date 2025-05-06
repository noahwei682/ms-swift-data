pip install huggingface_hub
export HF_TOKEN=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
huggingface-cli login --token $HF_TOKEN

huggingface-cli download wei682/amazon-grpo --repo-type dataset --local-dir ./msdata/grpo_v1
