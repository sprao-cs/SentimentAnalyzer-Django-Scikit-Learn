from SentimentAnalyzer.settings import BASE_DIR
import moviepy.editor as mvedit
import os
import cv2
from PIL import Image
from pytesseract import pytesseract


class VideoProcess:

     def __init__(self):
          pass

     def video_to_audio(self, fileInput):
          video = mvedit.VideoFileClip(fileInput)
          output_path = os.path.join(BASE_DIR, 'media') + "\\aud.wav"
          audio = video.audio.write_audiofile(output_path)

          return output_path

     def extract_frames(self,pathIn):
          pathOut = os.path.join(BASE_DIR, 'media') + "\\frames\\"
          if not os.path.exists(pathOut):
               os.mkdir(pathOut)

          capture = cv2.VideoCapture(pathIn)
          count = 0

          while (capture.isOpened()):
               ret, frame = capture.read()
               
               if ret == True:
                    print('Read %d frame: ' % count, ret)
                    cv2.imwrite(os.path.join(pathOut, "frame_{:d}.jpg".format(count)), frame)  # save frame as JPEG file
                    count += 1
               else:
                    break
          
          capture.release()
          cv2.destroyAllWindows()
          return pathOut

     def extract_frame_text(self, folderPath):
          exportText = ""

          for imgpath in os.listdir(folderPath):
               act_img = Image.open(folderPath + imgpath)

               pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe" # change the path of your location
               exportText += pytesseract.image_to_string(act_img)

               print(exportText)

          return exportText

               

     