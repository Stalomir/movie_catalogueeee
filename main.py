from flask import Flask, render_template, request
import tmdb_client
import random

app = Flask(__name__)

@app.route("/")
def homepage():
    selected_list = request.args.get("list_type", "popular")
    query_string=request.query_string
    available_lists = ['now_playing','popular','top_rated','upcoming']
    for list in available_lists:
        if list == selected_list:
            break
    else:
        selected_list = "popular"
    movies = tmdb_client.get_movies(how_many=8, list_type=selected_list)
    return render_template("homepage.html", movies=movies, available_lists=available_lists, selected_list=selected_list, query_string=query_string)

@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    details = tmdb_client.get_single_movie(movie_id)
    cast = tmdb_client.get_movie_cast(movie_id)
    movie_images = tmdb_client.get_movie_images(movie_id)
    selected_backdrop = random.choice(movie_images['backdrops'])
    return render_template("movie_details.html", movie=details, cast=cast, selected_backdrop=selected_backdrop)

@app.context_processor
def utility_processor():
    def tmdb_picture_url(path, size):
        return tmdb_client.get_picture_urls(path, size)
    return {"tmdb_picture_url": tmdb_picture_url}   

if __name__ == '__main__':
    app.run(debug=True)