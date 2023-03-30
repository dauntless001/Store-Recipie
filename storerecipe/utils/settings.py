import os

def get_app_settings():
    return os.environ.get('DJANGO_SETTINGS_MODULE', 'storerecipe.settings.dev')