"""SentimentAnalyzer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from SentimentAnalysisUI import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.index, name='index'),
    path('processText', views.textProcess, name='processText'),
    path('processImage', views.imageProcess, name='processImage'),
    path('processAudio', views.audioProcess, name='processAudio'),
    path('processVideo', views.videoProcess, name='processVideo'),

    path('text/analyzeText', views.analyzeText, name='analyzeText'),
    path('image/analyzeImage', views.analyzeImage, name='analyzeImage'),
    path('audio/analyzeAudio', views.analyzeAudio, name='analyzeAudio'),
    path('video/analyzeVideo', views.analyzeVideo, name='analyzeVideo')

]


urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
