import os
from dotenv import load_dotenv

# Load .env file variables
load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG') == 'True'

# For database example (if you want to load from env)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.getenv('DATABASE_NAME', 'db.sqlite3'),
    }
}
