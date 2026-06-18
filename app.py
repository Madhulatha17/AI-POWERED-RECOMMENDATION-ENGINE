from flask import Flask, request, jsonify
from model.recommender import recommend_movies

app = Flask(__name__)

@app.route('/')
def home():
    return "AI Recommendation Engine API is running"

@app.route('/recommend', methods=['GET'])
def recommend():
    movie = request.args.get('movie')

    if not movie:
        return jsonify({"error": "Please provide a movie name"}), 400

    recommendations = recommend_movies(movie)

    return jsonify({
        "input_movie": movie,
        "recommendations": recommendations
    })

if __name__ == '__main__':
    app.run(debug=True)
