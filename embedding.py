import pandas as pd
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

df=pd.read_csv('data.csv')

model = SentenceTransformer("all-MiniLM-L6-v2")

# Weighted rating calc
df["total_rating"] = (df["total_rating"] - df["total_rating"].min()) / (df["total_rating"].max() - df["total_rating"].min())
rating_weights = df["total_rating"].values.reshape(-1, 1)

# Type conversion
game_descriptions = df["summary"].fillna("").tolist()
game_genres = df["genres"].fillna("").astype(str).tolist()
game_keywords = df["keywords"].fillna("").astype(str).tolist()

# Encoding
game_summaries_encoded = model.encode(game_descriptions, convert_to_numpy=True)
game_genres_encoded = model.encode(game_genres, convert_to_numpy=True)
game_keywords_encoded = model.encode(game_keywords, convert_to_numpy=True)

# Normalization
game_summaries_encoded /= np.linalg.norm(game_summaries_encoded, axis=1, keepdims=True)
game_genres_encoded /= np.linalg.norm(game_genres_encoded, axis=1, keepdims=True)
game_keywords_encoded /= np.linalg.norm(game_keywords_encoded, axis=1, keepdims=True)

alpha, beta, gamma = 0.4, 0.3, 0.3  # Hyperparams
final_embeddings = (
    alpha * game_summaries_encoded + beta * game_genres_encoded + gamma * game_keywords_encoded
) * rating_weights

embedding_dim = final_embeddings.shape[1]
index = faiss.IndexFlatIP(embedding_dim)
index.add(final_embeddings)
faiss.write_index(index, 'index_file.index') # Save faiss index
print("Faiss index saved")

