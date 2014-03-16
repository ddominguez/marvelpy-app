import settings
from flask import Flask, render_template
from marvelpy import Marvel

app = Flask(__name__)
app.config['DEBUG'] = settings.DEBUG


@app.template_filter('marvel_image')
def marvel_image(o):
    thumbnail = marvel.image(o, 'portrait', 'fantastic')
    return '<img src="%s" />' % thumbnail['url']


@app.route('/')
def index():
    # Age of Apocalypse!
    character = marvel.events(id=227)
    data = character.json()
    eventResult = data['data']['results'][0]
    thumbnail = marvel.image(data['data']['results'][0]['thumbnail'], 'standard', 'fantastic')
    thumbnailUrl = thumbnail['url']

    # get comics for this event
    params = {
        'format': 'comic',
        'formatType': 'comic',
        'noVariants': 'false',
        'orderBy': 'onsaleDate',
        'limit': eventResult['comics']['available'],
        'offset': 0
    }
    comics = marvel.events(id=227, list_type='comics', params=params)
    comicsResult = comics.json()['data']['results']
    return render_template(
        'index.html',
        attributionHTML=data['attributionHTML'],
        eventResult=eventResult,
        comicsResult=comicsResult,
        thumbnailUrl=thumbnailUrl
    )

if __name__ == '__main__':
    marvel = Marvel(
        api_key=settings.MARVEL_API_KEY,
        private_key=settings.MARVEL_PRIVATE_KEY
    )
    app.run()
