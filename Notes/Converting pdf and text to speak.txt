import pyttsx3
import PyPDF2
speaker=pyttsx3.init()
speaker.say("Hey boss, Thank you. I can speak now")
speaker.runAndWait()
mypdf = open("mytext.pdf","rb")
pdfreader=PyPDF2.PdfFileReader(mypdf)
pages = pdfreader.numPages
print("Total pages are = ",pages)
for i in range(pages):
    page = pdfreader.getPage(i)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()