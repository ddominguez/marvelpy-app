import os

# get data environment variables
DEBUG = os.environ.get('FLASK_DEBUG', False)
PORT = int(os.environ.get('PORT', 5000))
MARVEL_API_KEY = os.environ.get('MARVEL_API_KEY', '')
MARVEL_PRIVATE_KEY = os.environ.get('MARVEL_PRIVATE_KEY', '')
