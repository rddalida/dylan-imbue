from random import random
from openpipe import OpenAI
import os
import datasets

API_KEY = os.environ["OPENPIPE_API_KEY"] if "OPENPIPE_API_KEY" in os.environ else input("Enter OpenPipe API key: ")

client = OpenAI(
  openpipe={"api_key": API_KEY}
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

def test_race_model(test_rows, model_name="openpipe:finetune-race-small", verbose=False):
    """
    Tests an openpipe model on the RACE dataset.
    test_rows - a dataset with the same format as the RACE dataset
                i.e. each row has keys "article", "question", "options", and "answer"
    model_name - name of the model in openpipe
    verbose - if True, prints result of every test
    """
    test_count = len(test_rows)

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
        if verbose:
            print(f"Test #{ctr}: expected {expected_answer}, got {model_answer}")

    print(f"Finished all {test_count} tests, got {correct} right")

    results = {
        "accuracy": correct / test_count,
        "correct_count": correct,
        "test_count": test_count
    }

    return results
 
if __name__ == "__main__":
    ds = datasets.load_dataset("ehovy/race", "all")["test"]
    ds.shuffle()
    tests = ds.select(range(100))
    print(test_race_model(tests, "openpipe:finetune-race-small", True))
