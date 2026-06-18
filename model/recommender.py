import pandas as pd

movies = pd.read_csv("data/movies.csv")

def recommend_movies(movie_name):
    movie_name = movie_name.lower()

    matches = movies[movies['title'].str.lower().str.contains(movie_name)]

    if matches.empty:
        return ["No recommendations found"]

    genre = matches.iloc[0]['genre']

    recommendations = movies[movies['genre'] == genre]['title'].tolist()

    return recommendations[:5]
