# code directly taken from https://docs.openpipe.ai/api-reference/post-unstablefinetunecreate
import requests

url = "https://api.openpipe.ai/api/v1/unstable/finetune/create"

dataset_id_tiny = "e231526d-09da-4cf8-9713-08bd68eebea7"
dataset_id_small = "ee5e8326-b4cf-498c-911d-89f61c61650a"
dataset_id_all = "476d7c11-48ef-4e59-be41-5892fb47e508"

payload = {
    "datasetId": dataset_id_small,
    "slug": "finetune-race-small",
    "baseModel": "meta-llama/Meta-Llama-3.1-8B-Instruct",
    "overrides": {
        "batch_size": "auto",
        "learning_rate_multiplier": 1.2,
        "num_epochs": 7,
        # "preference_tuning_variant": "DPO",
        # "preference_tuning_learning_rate_multiplier": 2,
        # "preference_tuning_num_epochs": 2,
        # "preference_tuning_training_beta": 2,
        # "preference_tuning_adapter_weight": 2,
        # "is_sft_enabled": True,
        # "is_preference_tuning_enabled": True
    }
}
headers = {
    "Authorization": "Bearer opk_425ad4f76622bee031cb088bc837555994a12b88f6",
    "Content-Type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)
