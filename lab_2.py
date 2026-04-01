import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from gensim.downloader import load

print("Loading pre-trained GloVe model (50 dimensions)...")
glove_model = load("glove-wiki-gigaword-50")

tech_words = [
    "computer", "algorithm", "software", "hardware", "code",
    "cloud", "database", "network", "cybersecurity", "encryption"
]

def reduce_dimensions(embeddings):
    pca = PCA(n_components=2)
    reduced = pca.fit_transform(embeddings)
    return reduced

def visualize(words, reduced_embeddings):
    plt.figure(figsize=(10, 6))
    for i, word in enumerate(words):
        x, y = reduced_embeddings[i]
        plt.scatter(x, y, marker='o', color='blue')
        plt.text(x + 0.02, y + 0.02, word, fontsize=12)
    plt.show()

def generate_similar_words(word, topn=5):
    print(f"\nTop {topn} words similar to '{word}':")
    similar_words = glove_model.most_similar(word, topn=topn)
    for word, similarity in similar_words:
        print(f"  {word}: {similarity}")

embeddings = [glove_model[word] for word in tech_words]
reduced_embeddings = reduce_dimensions(embeddings)
visualize(tech_words, reduced_embeddings)
generate_similar_words("hardware")