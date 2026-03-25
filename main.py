import pypdf as pdf # Importin Required Libraries.
import pytesseract
from pdf2image import convert_from_path
from gtts import gTTS
import shutil
import os

destination = r"C:\Users\Tahsin Siyam\Documents\Audio Converter"
language = 'en' # Defining Language

def txt_extract_pypdf(ask2):
    reader = pdf.PdfReader(f"{ask2}")
    text = ""
    for pages in reader.pages:
        text += (pages.extract_text() or "")+"\n"
    return text
def anotherway(ask2):
    images = convert_from_path(ask2,poppler_path=r"C:\poppler-25.12.0\Library\bin")
    text = ""
    for img in images:
        text+=pytesseract.image_to_string(img)+"\n"
    return text

ask2 = r""
ask2 = input("Enter PDF Location: ")
ask = input("Scanned or Real pdf? S/R")

if ask == "S":
    maintext = anotherway(ask2)
elif ask == "R":
    maintext = txt_extract_pypdf(ask2)

myobj = gTTS(text=maintext, lang=language,slow=False)
myobj.save("AudioBook.mp3")
os.makedirs(destination,exist_ok=True)
shutil.move("AudioBook.mp3", destination)