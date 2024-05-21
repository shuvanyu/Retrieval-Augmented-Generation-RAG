# Gemma 7-B as the LLM
from huggingface_hub import notebook_login
import os
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

def import_LLM():
    # Authenticate with Hugging Face using the token from the environment variable
    notebook_login(os.getenv("HF_TOKEN"))

    tokenizer = AutoTokenizer.from_pretrained("google/gemma-7b-it")
    model = AutoModelForCausalLM.from_pretrained(
        "google/gemma-7b-it",
        device_map="auto",
        torch_dtype=torch.float16,
        revision="float16",
    )

    return tokenizer, model