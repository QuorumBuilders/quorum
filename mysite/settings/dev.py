from .base import *
import os
from dotenv import load_dotenv

DEBUG = True
load_dotenv()

REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'].append('rest_framework.renderers.BrowsableAPIRenderer')

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / '../media'

ALLOWED_HOSTS = ['*'] 
CORS_ALLOW_ALL_ORIGINS = True #  use CORS_ALLOWED_ORIGINS = [] in produvtion
CORS_ALLOW_CREDENTIALS = True
CSRF_TRUSTED_ORIGINS = ['https://quorum.pythonanywhere.com'] # change immediately when you have a list of working frontend

# GOOGLE DRIVE API SETTINGS

SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
SERVICE_ACCOUNT_FILE = BASE_DIR / os.getenv('SERVICE_ACCOUNT_FILE_PATH','')
DEFAULT_FOLDER_ID = os.getenv('DEFAULT_FOLDER_ID')