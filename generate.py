# -*- coding: utf-8 -*-
"""AI_Assessment.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wJQ3b4Ull7nFC5kkxeEs2Yta74wrHwWr
"""

# generate.py

from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

def load_model():
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    model = GPT2LMHeadModel.from_pretrained("gpt2")
    model.eval()
    return tokenizer, model

def generate_text(prompt, tokenizer, model, max_length=50, top_k=50, temperature=0.7):
    input_ids = tokenizer.encode(prompt, return_tensors='pt')
    with torch.no_grad():
        output = model.generate(
            input_ids,
            max_length=max_length,
            do_sample=True,
            top_k=top_k,
            temperature=temperature,
            no_repeat_ngram_size=2,
            pad_token_id=tokenizer.eos_token_id
        )
    return tokenizer.decode(output[0], skip_special_tokens=True)


if __name__ == "__main__":
    prompt = "Once upon a time"
    tokenizer, model = load_model()

    temp_07 = generate_text(prompt, tokenizer, model, temperature=0.7)
    temp_10 = generate_text(prompt, tokenizer, model, temperature=1.0)

    # Print both outputs
    print("\n--- Output with Temperature 0.7 ---\n", temp_07)
    print("\n--- Output with Temperature 1.0 ---\n", temp_10)

        # Save to a file
    with open("generated_outputs.txt", "w") as f:
        f.write("--- Prompt ---\n")
        f.write(prompt + "\n\n")
        f.write("--- Output with Temperature 0.7 ---\n")
        f.write(temp_07 + "\n\n")
        f.write("--- Output with Temperature 1.0 ---\n")
        f.write(temp_10 + "\n")

    # Download in Colab
    from google.colab import files
    files.download("generated_outputs.txt")