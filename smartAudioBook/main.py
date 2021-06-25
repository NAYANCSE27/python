import pyttsx3
import PyPDF2

book = open('web.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

voice = pyttsx3.init()
print("Enter the range(l,r) of pages you want to hear:")
x, y = input().split()
x = int(x)
y = int(y)
for num in range(x - 1, y - 1):
    page = pdfReader.getPage(num)
    text = page.extractText()
    voice.say(text)
    voice.runAndWait()
