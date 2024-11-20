import json
from datasets import load_dataset

def create_messages(problem, with_answer=False):
    """
    Given a row of the RACE database,
    creates an OpenAI-format chat completion object.
    If with_answer is true, adds the expected answer
    as output of the chatbot.
    """
    prompt = "You are tasked to solve a reading comprehension problem. Each problem consists of a contextual article, followed by a question with four choices, labelled A, B, C, or D. Output only a single token, the letter of the correct answer."
    article = problem["article"]
    question = problem["question"]
    choices = '\n'.join(f"{chr(ord('A') + i)}. {problem['options'][i]}" for i in range(4))
    answer = problem["answer"]
    messages = [
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
    ]
    if with_answer:
        messages.append({"role": "assistant", "content": [
            {
                "type": "text",
                "text": answer,
                }
            ]})
    return messages

if __name__ == "__main__":
    output_file = "race_test.jsonl"
    ds = load_dataset("ehovy/race", "all", streaming=True)
    fw = open(output_file, 'w')

    for dataset in ["train", "test"]:
        for problem in ds[dataset]:
            data = {"messages": create_messages(problem, True), "split": dataset.upper()}
            json.dump(data, fw)
            fw.write('\n')
