from django.contrib import admin
from django.urls import path
from SentimentApp.views import SentimentApp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', SentimentApp, name='App'),
]
