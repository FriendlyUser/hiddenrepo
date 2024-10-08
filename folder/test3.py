#!/usr/bin/env python
"""A standalone Django application script."""
import os
import sys
from pathlib import Path
from django.contrib import admin
from django.conf import settings
from django.core.management import execute_from_command_line
from django.urls import path, include
from django.core.management import call_command
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.apps import AppConfig
from django.urls import URLPattern

# Configuration
BASE_DIR = Path(__file__).resolve().parent
SECRET_KEY = 'django-insecure-0k)yw!*8k^c!r%ce&tnqs9in0le)gq**-#my+*hu8$28$jl+sh'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'class',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'main'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
WSGI_APPLICATION = 'main'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

if not settings.configured:
    settings.configure(
        DEBUG=DEBUG,
        SECRET_KEY=SECRET_KEY,
        ALLOWED_HOSTS=ALLOWED_HOSTS,
        INSTALLED_APPS=INSTALLED_APPS,
        MIDDLEWARE=MIDDLEWARE,
        ROOT_URLCONF=ROOT_URLCONF,
        TEMPLATES=TEMPLATES,
        WSGI_APPLICATION=WSGI_APPLICATION,
        DATABASES=DATABASES,
        AUTH_PASSWORD_VALIDATORS=AUTH_PASSWORD_VALIDATORS,
    )

# AppConfig
class ClassConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'class'


# Views
def home(request: HttpRequest) -> HttpResponse:
    return render(request, 'home.html')


def info(request: HttpRequest) -> HttpResponse:
    return render(request, 'info.html')


# URL Configuration
urlpatterns: list[URLPattern] = [
    # path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('info', info, name='info')
]


def main():
    """Run administrative tasks and verify core functionality."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main')
    try:
        call_command('migrate')
        call_command('runserver', '0.0.0.0:8000')
    except Exception as exc:
        print(f"Error during setup and server execution: {exc}")
    sys.exit(0)


if __name__ == '__main__':
    main()
