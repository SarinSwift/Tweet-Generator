from flask import Flask
import analyze_word_freq as ana

import markov_chain

app = Flask(__name__)

@app.route('/')
def hello_world():
    # findingHist = ana.histogram()
    longer_model = markov_chain.markov_chain(markov_chain.open_file('/Users/sarinswift/Documents/CS1.2/WarAndPeace.txt'))
    return markov_chain.generate_sentence(10, longer_model)
    # return "Hellooo"
