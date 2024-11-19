import json
import pandas as pd

prompt = "You are tasked to solve a reading comprehension problem. Each problem consists of a contextual article, followed by a question with four choices, labelled A, B, C, or D. Output only a single token, the letter of the correct answer."
output_file = "race_openai.jsonl"

training_data = []

fw = open(output_file, 'w')

import pandas as pd

splits = {'test': 'all/test-00000-of-00001.parquet', 'train': 'all/train-00000-of-00001.parquet', 'validation': 'all/validation-00000-of-00001.parquet'}
df = pd.read_parquet("hf://datasets/ehovy/race/" + splits["test"])
print(df)

with open("race.json") as f:
    d = json.load(f)
    # print(d["rows"][0])
    for r in d["rows"]:
        problem = r["row"]
        article = problem["article"]
        question = problem["question"]
        choices = '\n'.join(f"{chr(ord('A') + i)}. {problem['options'][i]}" for i in range(4))
        # if problem == d["rows"][0]["row"]:
            # print(choices)
        data = {"messages": [
            {"role": "system", "content": [
                 {
                     "type": "text",
                     "text": prompt,
                 }
            ]},
            {
            "role": "user", "content": [
                {
                    "type": "text",
                    "text": "\n\n".join([article, question, choices])
                }
            ]}
        ]}
        if r == d["rows"][0]:
            print(data)
        json.dump(data, fw)
        fw.write('\n')
