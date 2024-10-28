import csv
from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Function to load movie data from the CSV file
def load_movies():
    movies = []
    with open('movies.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            movies.append({'title': row['title'], 'genre': row['genre'], 'language': row['language']})
    return movies

# Load movie data from the CSV file
sample_movies = load_movies()

# Sample data for books (hardcoded for now)
sample_books = [
    {'title': 'To Kill a Mockingbird', 'genre': 'Fiction', 'language': 'English'},
    {'title': 'El amor en los tiempos del cólera', 'genre': 'Romance', 'language': 'Spanish'},
    {'title': 'The Great Gatsby', 'genre': 'Fiction', 'language': 'English'},
    {'title': 'Les Misérables', 'genre': 'Historical', 'language': 'French'}
]

@app.route('/')
def home():
    return render_template('survey.html')

@app.route('/submit-survey', methods=['POST'])
def submit_survey():
    # Get form data
    age = request.form.get('age')
    genre = request.form.get('genre')
    language = request.form.get('language')

    # Filter sample data based on user input
    filtered_books = [book for book in sample_books if genre.lower() in book['genre'].lower() and language.lower() in book['language'].lower()]
    filtered_movies = [movie for movie in sample_movies if genre.lower() in movie['genre'].lower() and language.lower() in movie['language'].lower()]

    # Render recommendations template with filtered data
    return render_template('recommendations.html', books=filtered_books, movies=filtered_movies)

if __name__ == '__main__':
    app.run(debug=True)
