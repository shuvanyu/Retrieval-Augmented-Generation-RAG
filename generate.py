from prompt_formatter import prompt_formatter
from read_json import read_list
from import_LLM import import_LLM
from get_answer import get_answer
import torch

def askLLM(query):
    device = 'cuda' if torch.cuda.is_available() else 'cpu'

    tokenizer, model = import_LLM()

    # Get relevant resources
    indices = get_answer(query, device)
    text_chunks = read_list('text_chunks.json')

    # Create a list of context items
    context_items = [text_chunks[i] for i in indices if i != -1]

    # Format prompt with context items
    prompt = prompt_formatter(query, context_items, tokenizer)

    # Open a file in write mode
    with open('prompt.txt', 'w') as file:
        # Append the string to the file
        file.write(prompt)

    # Open the file in read mode
    with open('prompt.txt', 'r') as file:
        # Read the contents of the file
        prompt = file.read()

    input_ids = tokenizer(prompt, return_tensors="pt").to(device)
    # Generate an output of tokens
    outputs = model.generate(**input_ids,
                            temperature=0.2, # lower temperature = more deterministic outputs, higher temperature = more creative outputs
                            do_sample=True, # whether or not to use sampling, see https://huyenchip.com/2024/01/16/sampling.html for more
                            max_new_tokens=1500) # how many new tokens to generate from prompt

    # Turn the output tokens into text
    output_text = tokenizer.decode(outputs[0])

    return output_text.replace(prompt, '')