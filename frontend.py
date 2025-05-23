import streamlit as st
import requests
st.set_page_config(page_title="Hitbox", page_icon="🤖")
st.title("hitbox")
st.subheader('Game recommendation system using \'sentence-transformers/all-MiniLM-L6-v2\' and FAISS for quick semantic search')

user_input = st.chat_input("Describe your favourite game, genre or playstyle...", key="chat_input")
if user_input:
    try:
        response = requests.post(
            "https://recommender-api-s40v.onrender.com/recommend",
            json={"query": user_input, "top_n": 5}
        )
        if response.status_code == 200:
            recommendations = response.json().get("recommendations", [])
            st.markdown(f"### Your Results for \"{user_input}\":")
            box_cols = st.columns(5)
            for i, rec in enumerate(recommendations):
                img_url = rec.get("cover")
                score = rec.get("score")
                with box_cols[i]:
                    st.markdown(f"""
                    <div style="
                        height: 160px;
                        border-radius: 15px;
                        background-image: url('{img_url}');
                        background-size: cover;
                        background-position: center;
                        box-shadow: 0 4px 10px rgba(0,0,0,0.4);
                        display: flex;
                        align-items: flex-end;
                        justify-content: center;
                        color: white;
                        font-weight: bold;
                        font-size: 18px;
                        padding: 6px;
                        border: 2px solid white;
                        ">
                        #{i+1}
                    </div>
                    <div style="
                        text-align: center;
                        color: white;
                        font-size: 14px;
                        margin-top: 4px;
                    ">
                        Similarity: {1 - score:.2f}
                    </div>
                    """, unsafe_allow_html=True)
        else:
            st.error("Error fetching recommendations.")
    except Exception as e:
        st.error(f"Request failed: {e}")
