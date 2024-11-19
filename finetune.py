import datasets
import requests

url = "https://api.openpipe.ai/api/v1/unstable/finetune/create"

payload = {
    "datasetId": "",
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
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)
