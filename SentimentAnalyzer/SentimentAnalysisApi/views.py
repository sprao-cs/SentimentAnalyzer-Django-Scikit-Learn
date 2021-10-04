from django.shortcuts import render

from .apps import SentimentanalysisapiConfig
from django.http import JsonResponse
from rest_framework.views import APIView

from sklearn.metrics import confusion_matrix,f1_score

from SentimentAnalysisApi import clean_text

class call_model(APIView):

     def get(Self, request):
          if request.method == "GET":
               text = request.GET.get("text")  # get text from the parameter

               #Cleaning the received text
               process = clean_text.TextPreprocess()
               cleanedText = process.normalizer(text)

               # vectorizing the given text
               vector_text = SentimentanalysisapiConfig.vectorizer.transform([cleanedText])

               # Predict sentiment based on vector
               _predicted_data = SentimentanalysisapiConfig.model.predict(vector_text)
               prediction = _predicted_data[0]

               # build json response
               response = {'text_sentiment': prediction}

               return JsonResponse(response)