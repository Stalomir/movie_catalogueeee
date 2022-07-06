from flask import Flask, render_template
import tmdb_client

app = Flask(__name__)

@app.route("/")
def homepage():
    movies = tmdb_client.get_movies(how_many=9)
    return render_template("homepage.html", movies=movies)

@app.context_processor
def utility_processor():
    def tmdb_poster_url(path, size):
        return tmdb_client.get_poster_urls(path, size)
    return {"tmdb_poster_url": tmdb_poster_url}

if __name__ == '__main__':
    app.run(debug=True)