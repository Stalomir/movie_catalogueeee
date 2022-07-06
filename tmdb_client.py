from flask import Flask
import requests
import random

app = Flask(__name__)
app.config["SECRET_KEY"] = 'alamakota'

def get_popular_movies():
    url = "https://api.themoviedb.org/3/movie/popular"
    headers = {'Authorization': "Bearer %s" % "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4Y2FiOGMyMjEzZmM0MjFjYmQ1Yzk3ZDE4OGU2MmRlOCIsInN1YiI6IjYyYmM3Yjk1ZTFmYWVkMWRjNzc2OWMxOSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.gT60CG_IgbCzJG3PMjGMWEuc4eb86-7yIJaGhR-DEv4"}
    r =  requests.get(url, headers=headers)
    return r.json()

def get_poster_urls(poster_api_path, size):
    tmdb_url = "https://image.tmdb.org/t/p/"
    poster_url = f"{tmdb_url}{size}{poster_api_path}"
    return poster_url

def get_movies(how_many):
    data = get_popular_movies()
    random.shuffle(data['results'])
    return data["results"][:how_many]
