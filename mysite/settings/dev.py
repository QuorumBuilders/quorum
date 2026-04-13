from .base import *


REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'].append('rest_framework.renderers.BrowsableAPIRenderer')

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

ALLOWED_HOSTS = ['*'] 
CORS_ALLOW_ALL_ORIGINS = True #  use CORS_ALLOWED_ORIGINS = [] in produvtion
CORS_ALLOW_CREDENTIALS = True
CSRF_TRUSTED_ORIGINS = ['*'] # change immediately when you have a list of working frontend
