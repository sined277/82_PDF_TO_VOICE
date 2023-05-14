import PyPDF2
import pyttsx3

# path of the PDF file
path = 'file.pdf'

# creating a PdfReader object
with open(path, 'rb') as file:
    pdfReader = PyPDF2.PdfReader(file)

    # the page with which you want to start
    # this will read the page of 25th page.
    from_page = pdfReader.pages[1]

    # extracting the text from the PDF
    text = from_page.extract_text()

    # initializing the pyttsx3 engine
    engine = pyttsx3.init()

    # adding the text to the engine
    engine.say(text)

    # run the engine
    engine.runAndWait()
