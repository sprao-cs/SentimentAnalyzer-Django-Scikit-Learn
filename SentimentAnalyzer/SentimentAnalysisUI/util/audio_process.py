import os
import speech_recognition as sr 
from pydub import AudioSegment
from pydub.silence import split_on_silence

from SentimentAnalyzer.settings import BASE_DIR

class AudioProcess:
         

    def __init__(self):
        pass

    def remove_processed_audio(self, audioPath):
        if os.path.exists(audioPath):
            os.remove(audioPath)

    def get_large_audio_transcription(self, path):
        
        r = sr.Recognizer()
          
        sound = AudioSegment.from_wav(path)  

        chunks = split_on_silence(sound, min_silence_len = 500, silence_thresh = sound.dBFS-14, keep_silence=500)

        folder_name = os.path.join(BASE_DIR, 'media') + "\\audioChunks"

        if not os.path.exists(folder_name):
            os.mkdir(folder_name)
     
        exportText = ""
        
        # process each chunk 
        for i, audio_chunk in enumerate(chunks, start=1):

            chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
            audio_chunk.export(chunk_filename, format="wav")

            with sr.AudioFile(chunk_filename) as source:
                audio_listened = r.record(source)

                try:
                    text = r.recognize_google(audio_listened)
                except sr.UnknownValueError as e:
                    print("Error:", str(e))
                else:
                    text = f"{text.capitalize()}. "
                    exportText += text

            os.remove(chunk_filename)
        
        self.remove_processed_audio(path)      
        return exportText