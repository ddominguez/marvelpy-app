import settings
from flask import Flask, request, render_template
from marvelpy import Marvel

app = Flask(__name__)
app.config['DEBUG'] = settings.DEBUG


@app.template_filter('marvel_image')
def marvel_image(o):
    thumbnail = marvel.image(o, 'portrait', 'fantastic')
    return '<img src="%s" />' % thumbnail['url']


@app.route('/')
def index():
    events = marvel.events(params={'orderBy': 'name'}).json()

    # first event is default event
    eventId = request.args.get('id', events['data']['results'][0]['id'])

    # get event
    character = marvel.events(id=eventId).json()
    eventResult = character['data']['results'][0]
    thumbnail = marvel.image(character['data']['results'][0]['thumbnail'], 'standard', 'fantastic')
    thumbnailUrl = thumbnail['url']

    # get comics for this event
    params = {
        'format': 'comic',
        'formatType': 'comic',
        'noVariants': 'false',
        'orderBy': 'onsaleDate',
        'limit': 40,
        'offset': 0
    }
    comics = marvel.events(id=eventId, list_type='comics', params=params)
    comicsResult = comics.json()['data']['results']
    return render_template(
        'index.html',
        attributionHTML=events['attributionHTML'],
        eventResult=eventResult,
        comicsResult=comicsResult,
        thumbnailUrl=thumbnailUrl,
        events=events['data']['results'],
        eventId=int(eventId)
    )

if __name__ == '__main__':
    marvel = Marvel(
        api_key=settings.MARVEL_API_KEY,
        private_key=settings.MARVEL_PRIVATE_KEY
    )
    app.run()
