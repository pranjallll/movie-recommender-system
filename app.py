import streamlit as st
import pickle
import pandas as pd
import requests

# Function to fetch poster from TMDB API
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=0598b99ea1b962c37acf13e95966b1ea&language=en-US".format(movie_id)
    response = requests.get(url)
    data = response.json()
    return "http://image.tmdb.org/t/p/w500/" + data['poster_path']

# Load movies_dict.pkl locally (must be present in the same folder)
movies_dict = pickle.load(open('movies_dict_small2.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

with open('similarity_small.pkl', 'rb') as f:
    similarity = pickle.load(f)


# Recommendation function
def recommend(movie_title):
    movie_index = movies[movies['title'] == movie_title].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id  # Assumes 'movie_id' exists in your movies_dict.pkl
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

# Streamlit UI
st.title('🎬 Movie Recommender System')

selected_movie_name = st.selectbox(
    'Select a movie:',
    movies['title'].values
)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    cols = st.columns(5)
    for idx, col in enumerate(cols):
        with col:
            st.text(names[idx])
            st.image(posters[idx])

