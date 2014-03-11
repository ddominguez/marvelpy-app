import settings
from flask import Flask, render_template
from marvelpy import Marvel

app = Flask(__name__)
app.config['DEBUG'] = settings.DEBUG


@app.route('/')
def index():
    # Gambit!
    character = marvel.characters(id=1009313)
    data = character.json()
    result = data['data']['results'][0]
    return render_template(
        'index.html',
        attributionHTML=data['attributionHTML'],
        result=result
    )

if __name__ == '__main__':
    marvel = Marvel(
        api_key=settings.MARVEL_API_KEY,
        private_key=settings.MARVEL_PRIVATE_KEY
    )
    app.run()
