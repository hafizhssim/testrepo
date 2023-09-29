import tiktoken

encoding = tiktoken.get_encoding("cl100k_base")
encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")

# encoding.encode("tiktoken is great!")

def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

# count the tokens for a file

def num_tokens_from_file(file_path: str, encoding_name: str) -> int:
    """Returns the number of tokens in a file."""
    with open(file_path, "r") as f:
        file_text = f.read()
    return num_tokens_from_string(file_text, encoding_name)


# stories_2.txt

print(num_tokens_from_file("stories_2.txt", "cl100k_base"))