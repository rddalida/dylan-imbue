# pip install openpipe

from random import random
from openpipe import OpenAI
import datasets

test_count = 100
model_name = "openpipe:finetune-race-small"

client = OpenAI(
  openpipe={"api_key": "opk_425ad4f76622bee031cb088bc837555994a12b88f6"}
)
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

ds = datasets.load_dataset("ehovy/race", "all")["test"]
ds.shuffle()

correct = 0
ctr = 0

for problem in ds.select(range(test_count)):
    completion = client.chat.completions.create(
        model=model_name,
        messages=create_messages(problem),
        temperature=0,
        openpipe={
            "tags": {
                "prompt_id": "counting",
                "any_key": "any_value"
            }
        }
    )
    expected_answer = problem["answer"]
    model_answer = completion.choices[0].message.content
    if expected_answer == model_answer:
        correct += 1
    ctr += 1
    print(f"#{ctr}: expected {expected_answer}, got {model_answer}")

print(f"Accuracy: {correct / test_count} ({correct}/{test_count})")
 
