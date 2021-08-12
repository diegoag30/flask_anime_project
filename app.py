from anime import Anime
from flask import Flask, render_template, url_for
from requests import get
from anime import Anime

app = Flask(__name__)

@app.route('/home')
def index():
    
    # Connection to anime api
    animes = get('https://kitsu.io/api/edge/anime?filter[seasonYear]=2020').json()
    anime_info = animes['data']
    anime_list = []
    for anime in anime_info:
        try:
            # Anime Objects creation
            current_anime = Anime(
            anime['attributes']['titles']['en_jp'],
            anime['attributes']['posterImage']['medium'],
            anime['attributes']['status'],
            anime['attributes']['episodeCount']
            )
            anime_list.append(current_anime)
        except KeyError:
            pass

    return render_template('index.html',anime_titles = anime_list)


if __name__== "__main__":
    app.run(debug=True,)