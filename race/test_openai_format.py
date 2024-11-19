import json
from datasets import load_dataset

prompt = "You are tasked to solve a reading comprehension problem. Each problem consists of a contextual article, followed by a question with four choices, labelled A, B, C, or D. Output only a single token, the letter of the correct answer."
output_file = "race_openai.jsonl"

training_data = []

fw = open(output_file, 'w')

ds = load_dataset("ehovy/race", "all", streaming=True)
print(ds["train"])

for dataset in ["train", "test"]:
    for problem in ds[dataset]:
        article = problem["article"]
        question = problem["question"]
        choices = '\n'.join(f"{chr(ord('A') + i)}. {problem['options'][i]}" for i in range(4))
        answer = problem["answer"]
        # if problem == d["rows"][0]["row"]:
            # print(choices)
        data = {"messages": [
            {"role": "system", "content": [
                {
                    "type": "text",
                    "text": prompt,
                    }
                ]},
            {"role": "user", "content": [
                {
                    "type": "text",
                    "text": "\n\n".join([article, question, choices]),
                    }
                ]},
            {"role": "assistant", "content": [
                {
                    "type": "text",
                    "text": answer,
                    }
                ]},
            ],
                "split": dataset.upper()}
        json.dump(data, fw)
        fw.write('\n')
