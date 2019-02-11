from flask import Flask
import analyze_word_freq as ana

app = Flask(__name__)

@app.route('/')
def hello_world():
    # findingHist = ana.histogram()
    return "hello world"
