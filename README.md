# RACE Fine-Tuner

Fine-tunes a model that answers multiple-choice questions in the RACE reading comprehension dataset using OpenPipe.

Consists of three main files:

- **finetuner.py**: API call for finetuning llama-8b on the RACE dataset using OpenPipe. There are three pre-done training sets, all taken from RACE:
   - dataset\_id\_tiny: 10 train + 2 test, picked 12 entries by hand
   - dataset\_id\_small: 878 train + 50 test, uniform sample ~1% of data
    - dataset\_id\_all: all 92.8k entries
  
   I have generated these on OpenPipe. If you want access to the datasets on OpenPipe, message me - I'd have to add you to the project in OpenPipe. (Can't add them to the repo - too large!)
- **tester.py**: Tests accuracy of an OpenPipe model on the RACE dataset. To test functionality of the tester, chooses 100 random entries from the testing dataset, checks if model matches with answer.
- **race/openai_formatter.py**: Formats entries in the RACE dataset as OpenAI chat completion objects. The resulting output file can be dropped directly into OpenPipe as a dataset.

To run finetuner and tester, set an environment variable `OPENPIPE_API_KEY` with your openpipe key, otherwise it'll ask you for one.
