from flask import Flask, request, jsonify
import pandas as pd
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss
from flask_cors import CORS

print("Loading data and model...")
df = pd.read_csv('data.csv')

model = SentenceTransformer("all-MiniLM-L6-v2")
loaded_index = faiss.read_index('index_file.index')

app = Flask(__name__)
CORS(app)
@app.route('/recommend', methods=['POST'])
def recommend_games():
    user_query = request.json.get("query")
    top_n = request.json.get("top_n", 5) #default 5

    if not user_query:
        return jsonify({"error": "Query not provided."}), 400

    query_embedding = model.encode([user_query], convert_to_numpy=True)
    query_embedding = query_embedding / np.linalg.norm(query_embedding)

    distances, indices = loaded_index.search(query_embedding, top_n)

    recommendations = df.iloc[indices[0]]["name"].tolist()
    
    return jsonify({"recommendations": recommendations})

if __name__ == '__main__':
    app.run(debug=True)