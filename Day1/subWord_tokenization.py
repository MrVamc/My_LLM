# The tokenizer splits words into subwords.
import tiktoken

encoder = tiktoken.encoding_for_model("gpt-4o")
words = ["unhappiness", "happiness", "unhappy", "happy", "unhappily", "happily"]

for word in words:
    # Tokenize the word into subwords
    tokens = encoder.encode(word)
    pieces = [encoder.decode([token_id]) for token_id in tokens]
    print(f"Word: {word} -> Tokens: {tokens} -> Pieces: {pieces} -> Number of tokens: {len(tokens)}")

# The 75% rule: tokens vs words
# This is useful for estimating costs and context window limits

paragraph = (
    "Large Language Models are neural networks trained on massive amounts of text. "
    "They predict the next token, one at a time, to generate human-like responses. "
    "This is the foundation of ChatGPT, Claude, and every modern AI assistant."
)

word_count = len(paragraph.split())
token_count = len(encoder.encode(paragraph))

print(f"Words:  {word_count}")
print(f"Tokens: {token_count}")
print(f"Ratio:  1 token = roughly {word_count / token_count:.2f} words")
print()
print("Rule of thumb: 100 tokens = roughly 75 words")
print("Remember this when we talk about context windows and API pricing.")