from flask import Flask, render_template, url_for
from requests import get
app = Flask(__name__)

@app.route('/home')
def index():
    animes = get('https://kitsu.io/api/edge/anime?filter[seasonYear]=2020').json()
    animes = animes['data']
    titles =[]
    for anime in animes:
        try:
            titles.append(anime['attributes']['titles']['en_jp'])
        except KeyError:
            pass

    ## return animes['data'][0]['attributes']['titles']['en_jp']
    return render_template('index.html',anime_titles = titles)


if __name__== "__main__":
    app.run(debug=True,)