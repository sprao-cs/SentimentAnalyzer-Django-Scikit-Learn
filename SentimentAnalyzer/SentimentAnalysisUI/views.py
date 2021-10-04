from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import requests
import os
import re
from SentimentAnalysisApi import clean_text
from SentimentAnalyzer.settings import BASE_DIR

''' Import for Image Processsing '''
from SentimentAnalysisUI.util import image_process

''' Import for Audio Processing '''
from SentimentAnalysisUI.util import audio_process

''' Import for Video Processing '''
from SentimentAnalysisUI.util import video_process

API_URL = "http://127.0.0.1:8000/classify/"
process = clean_text.TextPreprocess()


''' Main Methods '''
def index(request):
    return render(request, 'index.html')

def textProcess(request):
     return render(request, 'text_extract.html')

def imageProcess(request):
    return render(request, 'image_extract.html')

def audioProcess(request):
    return render(request, 'audio_extract.html')

def videoProcess(request):
    return render(request, 'video_extract.html')


''' Sub Methods '''
def analyzeText(request):
     try:
        if request.method == 'POST':
            text = request.POST.get("userText")
            # cleaned_text = process.normalizer(text)

            params = {'text': text}
            response = requests.get(url=API_URL, params=params)
            data = response.json()
            sentiment = data["text_sentiment"]

     except Exception as ex:
        print("Exception Occured ", ex)

     return render(request,'result.html', {'type': 'text_sentiment', 'given_text': text, 'result': sentiment})

def analyzeImage(request):
    if request.method == "POST":
        my_uploaded_file = request.FILES['uploaded_img'] # get the uploaded file
    
        fs = FileSystemStorage()
        filename = fs.save(my_uploaded_file.name, my_uploaded_file)
        uploaded_file_path = fs.path(filename)

        imageProcess = image_process.ImageProcess()
        imgText = imageProcess.image_to_text(uploaded_file_path)
        cleaned_text = process.normalizer(imgText)
        
        output = re.sub(r"[\n\t]*", "", cleaned_text)
        output = output.encode('ascii', errors='ignore').decode()

        params = {'text': cleaned_text}
        response = requests.get(url=API_URL, params=params)
        data = response.json() 
        sentiment = data["text_sentiment"]

    return render(request, 'result.html', {'type': 'image_sentiment', 'given_text': imgText, 'result': sentiment})

def analyzeAudio(request):
    
    if request.method == "POST":
        my_uploaded_file = request.FILES['uploaded_audio'] # get the uploaded file
    
        fs = FileSystemStorage()
        filename = fs.save(my_uploaded_file.name, my_uploaded_file)
        
        uploaded_file_path = fs.path(filename)

        audioProcess = audio_process.AudioProcess()
        audioText = audioProcess.get_large_audio_transcription(uploaded_file_path)
        cleaned_text = process.normalizer(audioText)

        output = re.sub(r"[\n\t]*", "", cleaned_text)
        output = output.encode('ascii', errors='ignore').decode()

        params = {'text': cleaned_text}
        response = requests.get(url=API_URL, params=params)
        data = response.json()
        sentiment = data["text_sentiment"]
         
    return render(request, 'result.html', {'type': 'audio_sentiment', 'given_text': cleaned_text, 'result': sentiment})

def analyzeVideo(request):
         
    if request.method == "POST":
        my_uploaded_file = request.FILES['uploaded_video'] # get the uploaded file
        choice = request.POST.get("sentiment-choice")

        fs = FileSystemStorage()
        filename = fs.save(my_uploaded_file.name, my_uploaded_file)

        uploaded_file_path = fs.path(filename)
        videoProcess = video_process.VideoProcess()

        if choice == "text":
            frames_path = videoProcess.extract_frames(uploaded_file_path)
            extract_text = videoProcess.extract_frame_text(frames_path)

        elif choice == "audio":
                 
            audioPath = videoProcess.video_to_audio(uploaded_file_path)

            audioProcess = audio_process.AudioProcess()
            extract_text = audioProcess.get_large_audio_transcription(audioPath)
            cleaned_text = process.normalizer(extract_text)

        else:
            print("invalid")
        
        
        params = {'text': cleaned_text}
        response = requests.get(url=API_URL, params=params)
        data = response.json()
        sentiment = data["text_sentiment"]
    
    return render(request, 'result.html', {'type': 'video_sentiment', 'given_text': extract_text, 'result': sentiment})
