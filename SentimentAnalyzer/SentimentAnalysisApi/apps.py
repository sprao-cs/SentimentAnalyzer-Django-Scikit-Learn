from django.apps import AppConfig
from django.conf import settings

import os
import pickle

class SentimentanalysisapiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'SentimentAnalysisApi'

    path = os.path.join(settings.MODELS, 'models.p')

    # separation of data packed in the model pickle

    with open(path, 'rb') as pickledFile:
        data = pickle.load(pickledFile)

    model = data['model']
    vectorizer = data['vectorizer']

