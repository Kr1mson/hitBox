import pandas as pd
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

df=pd.read_csv('data.csv')
df=df[["name","summary"]]
model = SentenceTransformer("all-MiniLM-L6-v2")
loaded_index = faiss.read_index('index_file.index')
def recommend_games(user_query, top_n=5):

    query_embedding = model.encode([user_query], convert_to_numpy=True)
    query_embedding = query_embedding / np.linalg.norm(query_embedding)

    distances, indices = loaded_index.search(query_embedding, top_n)

    recommendations = df.iloc[indices[0]]["name"].tolist()

    return recommendations

user_input = "kung fu styled fighting game"
recommended_games = recommend_games(user_input, top_n=5)

print("Recommended Games:", recommended_games)

