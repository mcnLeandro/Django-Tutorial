BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-=t(_zi8cx_a=1up1v2+c!*t_=ngm9g1@(p)@z86mt*4l!ug=9h'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_first_db',
        'USER': 'root',
        'PASSWORD': '',
    }
}

DEBUG = True
