# tiktoken is OpenAI’s fast tokenizer used for models like GPT-4, GPT-3.5, etc.
# It helps convert text ⟷ tokens (numbers).
import tiktoken

# This encoder object can now convert text → tokens and tokens → text exactly how GPT-4o expects.
encoder = tiktoken.encoding_for_model('gpt-4o')

# Every tokenizer has a vocabulary — a fixed number of known tokens.
# encoder.n_vocab returns that number.
# For gpt-4o, it's about 200,019 tokens — this includes words, parts of words, symbols, etc.
print("Vocab Size", encoder.n_vocab) # 2,00,019 (200K)


# This converts your sentence into a list of tokens (numbers).
# Each number represents a piece of the sentence — either a full word or part of a word, depending on the tokenizer's logic.
text = "The cat sat on the mat"
tokens = encoder.encode(text)

print("Tokens", tokens) # Tokens [976, 9059, 10139, 402, 290, 2450]

my_tokens = [976, 9059, 10139, 402, 290, 2450]
decoded = encoder.decode([976, 9059, 10139, 402, 290, 2450])
print("Decoded", decoded)