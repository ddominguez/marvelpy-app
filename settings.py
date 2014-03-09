DEBUG = False

MARVEL_API_KEY = ''
MARVEL_PRIVATE_KEY = ''

try:
    from local_settings import *
except ImportError:
    pass
