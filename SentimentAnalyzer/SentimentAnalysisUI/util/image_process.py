import os
from PIL import Image
from pytesseract import pytesseract
# After this head to the website "https://github.com/UB-Mannheim/tesseract/wiki" download and install tessarctOCR

class ImageProcess:
         
    def __int__(self):
        pass

    def remove_processed_image(self, imagePath):
        if os.path.exists(imagePath):
            os.remove(imagePath)
    
    def image_to_text(self,imagePath):
        act_img = Image.open(imagePath)

        pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe" # change the path of your location
        exportText = pytesseract.image_to_string(act_img)

        self.remove_processed_image(imagePath)
        return exportText