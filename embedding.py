import pandas as pd
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

df=pd.read_csv('data.csv')
df=df[["name","summary"]]

model = SentenceTransformer("all-MiniLM-L6-v2")

game_descriptions = df["summary"].tolist()
game_embeddings = model.encode(game_descriptions, convert_to_numpy=True)

game_embeddings = game_embeddings / np.linalg.norm(game_embeddings, axis=1, keepdims=True)
embedding_dim = game_embeddings.shape[1]
index = faiss.IndexFlatIP(embedding_dim)
index.add(game_embeddings)
faiss.write_index(index, 'index_file.index')