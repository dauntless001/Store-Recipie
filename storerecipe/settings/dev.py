from storerecipe.settings.base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure--afk7x1tdtgslsb5(3cq*vylx)+u=x+lf@iex7*#7v@ydte7&&"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


DATABASES["default"] =  {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "storerecipe.db",
}

STATIC_URL = 'static/'
STATICFILE_DIRS = BASE_DIR / 'storerecipe/assets'
STATIC_ROOT = BASE_DIR / 'assets'

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'