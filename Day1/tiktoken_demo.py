# tiktoen is the tokenzier library used by the LLM model. 
# It is used to convert text into tokens and vice versa. 
# The library is used to tokenize the input text and convert it into a format that can be processed by the model.

# To get OpenAI's tiktoken package for Python, run the standard installation command in your terminal or command prompt
# `pip install tiktoken`

import tiktoken

# Load the tokenizer for the specific model you are using. 
# For example, if you are using the "gpt-4o" model, you can load its tokenizer as follows:
encoder = tiktoken.encoding_for_model("gpt-4o")

text = "Hello, how are you?"

# Break the text into tokens using the encoder
tokens = encoder.encode(text)

# Print the tokens
print(f"Text: {text}")
print(f"Tokens ids: {tokens}")
print(f"Number of tokens: {len(tokens)}")

# lets which token is assigned to which word in the text.
for token_id in tokens:
    token_str = encoder.decode([token_id])
    print(f"Token ID: {token_id}, Token String: '{token_str}'")