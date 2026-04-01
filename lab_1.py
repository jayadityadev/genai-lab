from gensim.downloader import load

print("Loading pre-trained GloVe model (50 dimensions)...")
glove_model = load("glove-wiki-gigaword-50")

def explore_word_relationships():
    # Analogy: king - man + woman = ?
    result = glove_model.most_similar(positive=['king', 'woman'], negative=['man'], topn=1)
    print("\nking - man + woman =", result[0][0])
    print("Similarity:", result[0][1])

    # Analogy: paris - france + italy = ?
    result = glove_model.most_similar(positive=['paris', 'italy'], negative=['france'], topn=1)
    print("\nparis - france + italy =", result[0][0])
    print("Similarity:", result[0][1])

    # Top 5 words similar to 'programming'
    programming_similar = glove_model.most_similar(positive=['programming'], topn=5)
    print("\nTop 5 words similar to 'programming':")
    for word, similarity in programming_similar:
        print(f"  {word}: {similarity}")

explore_word_relationships()