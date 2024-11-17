# auth_app/settings.py (relevant parts)

# settings.py

from pathlib import Path

# Define BASE_DIR if not already present
BASE_DIR = Path(__file__).resolve().parent.parent

# Applications installed in Django
INSTALLED_APPS = [
    # Default Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Custom app for authentication
    'auth_app',  # Ensure 'auth_app' exists in your Django project
]

# Custom User model
# Ensure a User model exists in auth_app/models.py
AUTH_USER_MODEL = 'auth_app.User'

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # MySQL engine
        'NAME': 'warehouse',                   # Database name
        'USER': 'your_mysql_username',         # MySQL username
        'PASSWORD': 'your_mysql_password',     # MySQL password
        'HOST': 'localhost',                   # MySQL host
        'PORT': '3306',                        # Default MySQL port
    }
}
