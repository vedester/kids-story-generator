# backend/core/settings.py

from pathlib import Path
import os
from dotenv import load_dotenv
load_dotenv()

# Google API Key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Base Directory
BASE_DIR = Path(__file__).resolve().parent.parent

# --- CHANGE 1: SECRET KEY ---
# Use an environment variable for safety. If not found, fall back to the insecure one (for local dev only)
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure--juk4!rk@7!3^1etnn^=2l*r7rdh888j4aw_q43!ka2+jdy$vw')

# --- CHANGE 2: DEBUG MODE ---
# Keep False for production. (If you have issues, temporarily set to True to see errors)
DEBUG = False

# --- CHANGE 3: ALLOWED HOSTS ---
# Only allow your specific Render URL and localhost
ALLOWED_HOSTS = [
    'kids-story-generator-backend.onrender.com', # Your Render URL (Check exact spelling!)
    'localhost', 
    '127.0.0.1'
]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'stories',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # 'whitenoise.middleware.WhiteNoiseMiddlewar',  # OPTIONAL: Add this if you want Admin panel CSS to work
    'whitenoise.middleware.WhiteNoiseMiddleware', # OPTIONAL: Add this if you want Admin panel CSS to work
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# OPTIONAL: Makes static files smaller and faster
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# --- CHANGE 4: CORS SETTINGS ---
# Disable "Allow All" and only allow your Vercel Frontend
CORS_ALLOW_ALL_ORIGINS = False 

CORS_ALLOWED_ORIGINS = [
    "https://kids-story-generator-five.vercel.app", # Your EXACT Vercel URL
    "http://localhost:3000", # Keep this for local testing
]