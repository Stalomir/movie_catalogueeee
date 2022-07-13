from flask import Flask
import requests
import random

API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4Y2FiOGMyMjEzZmM0MjFjYmQ1Yzk3ZDE4OGU2MmRlOCIsInN1YiI6IjYyYmM3Yjk1ZTFmYWVkMWRjNzc2OWMxOSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.gT60CG_IgbCzJG3PMjGMWEuc4eb86-7yIJaGhR-DEv4"

app = Flask(__name__)
app.config["SECRET_KEY"] = 'alamakota'

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    headers = {'Authorization': "Bearer %s" % API_TOKEN}
    r =  requests.get(endpoint, headers=headers)
    return r.json()

def get_picture_urls(picture_api_path, size):
    tmdb_url = "https://image.tmdb.org/t/p/"
    picture_url = f"{tmdb_url}{size}{picture_api_path}"
    return picture_url

def get_movies(how_many, list_type):
    data = get_movie_list(list_type)["results"]
    random.shuffle(data)
    return data[:how_many]

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {'Authorization': "Bearer %s" % API_TOKEN}
    r =  requests.get(endpoint, headers=headers)
    return r.json()

def get_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {'Authorization': "Bearer %s" % API_TOKEN}
    r =  requests.get(endpoint, headers=headers)
    return r.json()["cast"][:6]

def get_movie_images(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    headers = {'Authorization': f"Bearer {API_TOKEN}"}
    r = requests.get(endpoint, headers=headers)
    return r.json()

def get_movie_list(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = { "Authorization": f"Bearer {API_TOKEN}"}
    r = requests.get(endpoint, headers=headers)
    r.raise_for_status()
    return r.json()