from gensim.models import Word2Vec
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

medical_corpus = [
    "The patient was diagnosed with diabetes and hypertension.",
    "MRI scans reveal abnormalities in the brain tissue.",
    "The treatment involves antibiotics and regular monitoring.",
    "Symptoms include fever, fatigue, and muscle pain.",
    "The vaccine is effective against several viral infections.",
    "Doctors recommend physical therapy for recovery.",
    "The clinical trial results were published in the journal.",
    "The surgeon performed a minimally invasive procedure.",
    "The prescription includes pain relievers and anti-inflammatory drugs.",
    "The diagnosis confirmed a rare genetic disorder."
]

tokenized_corpus = [sentence.lower().split() for sentence in medical_corpus]

word2vec_model = Word2Vec(
    sentences=tokenized_corpus,
    vector_size=50,
    window=2,
    min_count=1,
    epochs=1000
)

# query_word = input("Enter a word: ").lower()
query_word = "doctors"

if query_word in word2vec_model.wv:
    similar_words = word2vec_model.wv.most_similar(query_word, topn=5)
    print(f"\nTop 5 words similar to '{query_word}':")
    for rank, (word, similarity_score) in enumerate(similar_words, 1):
        print(f"  {rank}. {word}: {similarity_score}")
else:
    print(f"'{query_word}' was not found in the vocabulary.")

vocabulary = list(word2vec_model.wv.index_to_key)
word_vectors = word2vec_model.wv[vocabulary]

pca = PCA(n_components=2)
reduced_embeddings = pca.fit_transform(word_vectors)

plt.figure(figsize=(20, 8))
plt.scatter(reduced_embeddings[:, 0], reduced_embeddings[:, 1])
for i, word in enumerate(vocabulary):
    plt.annotate(word, xy=(reduced_embeddings[i, 0], reduced_embeddings[i, 1]))
plt.title("Word Embeddings Visualization")
plt.xlabel("PCA 1")
plt.ylabel("PCA 2")
plt.grid(True)
plt.tight_layout()
plt.show()