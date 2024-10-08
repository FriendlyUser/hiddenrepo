#!/usr/bin/env python
import os
import sys
from django.conf import settings
from django.core.management import execute_from_command_line
from django.core.asgi import get_asgi_application
from django.urls import path
from django.http import JsonResponse
from django.apps import AppConfig
from django.contrib import admin
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.db import models
from django.test import TestCase
from rest_framework import serializers

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restTutorial.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

# Django Settings
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

settings.configure(
    SECRET_KEY='$thk^nk6p-qh9j+ca$d*0g3234#jz-%i^7ny9@q^w4jx0j!9kk',
    DEBUG=True,
    ALLOWED_HOSTS=['*'],
    INSTALLED_APPS=[
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'rest_framework.authtoken',
        'rest_framework',
        'rest_framework_simplejwt',
        'corsheaders',
        'jwtapp',
    ],
    MIDDLEWARE=[
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'corsheaders.middleware.CorsMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ],
    ROOT_URLCONF=__name__,
    TEMPLATES=[
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
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
    ],
    WSGI_APPLICATION=__name__ + '.application',
    CORS_ORIGIN_ALLOW_ALL=True,
    CORS_ALLOW_CREDENTIALS=True,
    CORS_ALLOW_HEADERS=[
        'accept',
        'accept-encoding',
        'authorization',
        'content-type',
        'dnt',
        'origin',
        'user-agent',
        'x-csrftoken',
        'x-requested-with',
        'set-cookie'
    ],
)

# Models
class JwtAppConfig(AppConfig):
    name = 'jwtapp'

# Serializers
class UserSerial(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

# Views
class Home(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        Token.objects.filter(user=request.user).delete()
        return JsonResponse({'stat': 'OK', 'user': request.user.username})

# URL Configuration
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('home/', Home.as_view()),
]

# WSGI Application
application = get_wsgi_application()

# Test Cases
class SimpleTest(TestCase):
    def test_basic_addition(self):
        self.assertEqual(1 + 1, 2)

if __name__ == '__main__':
    main()
