# code directly taken from https://docs.openpipe.ai/api-reference/post-unstablefinetunecreate
import requests

url = "https://api.openpipe.ai/api/v1/unstable/finetune/create"

payload = {
    "datasetId": "476d7c11-48ef-4e59-be41-5892fb47e508",
    "slug": "finetune-race",
    "baseModel": "meta-llama/Meta-Llama-3.1-8B-Instruct",
    "overrides": {
        "batch_size": "auto",
        "learning_rate_multiplier": 123,
        "num_epochs": 123,
        "preference_tuning_variant": "DPO",
        "preference_tuning_learning_rate_multiplier": 123,
        "preference_tuning_num_epochs": 123,
        "preference_tuning_training_beta": 123,
        "preference_tuning_adapter_weight": 123,
        "is_sft_enabled": True,
        "is_preference_tuning_enabled": True
    }
}
headers = {
    "Authorization": "Bearer opk_425ad4f76622bee031cb088bc837555994a12b88f6",
    "Content-Type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)
