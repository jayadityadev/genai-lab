import string
import nltk
from nltk.tokenize import word_tokenize
from gensim.downloader import load
from transformers import pipeline

nltk.download('punkt_tab')

print("Loading pre-trained GloVe model (100 dimensions)...")
glove_model = load("glove-wiki-gigaword-100")

print("Loading GPT-2 text generation model...")
text_generator = pipeline("text-generation", model="gpt2")


def replace_keyword_with_similar(prompt, keyword, word_vectors, topn=1):
    """Replace a target keyword in the prompt with its most similar word from GloVe."""
    tokens = word_tokenize(prompt)
    enriched_tokens = []

    for token in tokens:
        cleaned_token = token.lower().strip(string.punctuation)
        if cleaned_token == keyword.lower():
            try:
                similar_words = word_vectors.most_similar(cleaned_token, topn=topn)
                if similar_words:
                    replacement = similar_words[0][0]
                    print(f"Replacing '{token}' -> '{replacement}'")
                    enriched_tokens.append(replacement)
                    continue
            except KeyError:
                print(f"'{keyword}' not found in vocabulary, using original word.")
        enriched_tokens.append(token)

    enriched_prompt = " ".join(enriched_tokens)
    print(f"\nEnriched Prompt: {enriched_prompt}")
    return enriched_prompt


def generate_response(prompt, max_length=100):
    """Generate a text response for the given prompt using GPT-2."""
    try:
        response = text_generator(prompt, max_length=max_length, num_return_sequences=1)
        return response[0]['generated_text']
    except Exception as e:
        print(f"Error generating response: {e}")
        return None


original_prompt = "write an essay on natural disaster"
target_keyword = "disaster"

print(f"\nOriginal Prompt: {original_prompt}")

enriched_prompt = replace_keyword_with_similar(original_prompt, target_keyword, glove_model)

print("\nGenerating response for original prompt...")
original_response = generate_response(original_prompt)
print(original_response)

print("\nGenerating response for enriched prompt...")
enriched_response = generate_response(enriched_prompt)
print(enriched_response)

print("\n--- Comparison of Responses ---")
print(f"Original prompt response length : {len(original_response)}")
print(f"Enriched prompt response length : {len(enriched_response)}")
print(f"Original prompt sentence count  : {original_response.count('.')}")
print(f"Enriched prompt sentence count  : {enriched_response.count('.')}")