import PyPDF2
from flask import Flask, render_template, request, redirect, url_for, flash
import os
from werkzeug.utils import secure_filename
import pyttsx3
import PyPDF2


app = Flask(__name__)

UPLOAD_FOLDER = "path_to_your_folder_where_the_document_has_to_be_saved"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

global speak

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/uploadDoc", methods=['POST', 'GET'])
def uploadDoc():
    if request.method == "POST":
        file = request.files['file']
        # filename = secure_filename(file.filename)
        filename = secure_filename("document.pdf")
        if file.filename == '':
            return f'<h1>File Save Unsuccessful - Please check !</h1>'
        else:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            path = open('./static/document.pdf', 'rb')
            pdfReader = PyPDF2.PdfFileReader(path)
            from_page = pdfReader.getPage(0)
            text = from_page.extractText()
            speak = pyttsx3.init()
            speak.say(text)
            speak.runAndWait()
            return render_template("run.html")



if __name__ == "__main__":
    app.run(debug=True)

