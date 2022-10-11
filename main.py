import requests
import PyPDF2

VOICE_RSS_ENDPOINT = "http://api.voicerss.org/?"
API_KEY = "..."

# -------PDF to text conversion----------

# create file object variable
pdffileobj = open('test.pdf', 'rb')

# create reader variable that will read the pdffileobj
pdfreader = PyPDF2.PdfFileReader(pdffileobj)

# This will store the number of pages of this pdf file
x = pdfreader.numPages

# create a variable that will select the selected number of pages
pageobj = pdfreader.getPage(x - 1)

# (x-1) because python indentation starts with 0.
# create text variable which will store all text data from pdf file
text = pageobj.extractText()


# -------Text to Audio conversion----------

parameters = {
    'key': API_KEY,
    'src': text,
    'hl': "en-us"
}

response = requests.get(VOICE_RSS_ENDPOINT, params=parameters)
response.raise_for_status()

# Saving the response file
with open("sound.wav", "wb") as file:
    for chunk in response.iter_content(chunk_size=128):
        file.write(chunk)
