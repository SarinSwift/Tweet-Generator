from flask import Flask
import analyze_word_freq as ana

import markov_chain

app = Flask(__name__)


app.longer_model = markov_chain.markov_chain(markov_chain.open_file('WarAndPeace.txt'))

@app.route('/')
def hello_world():
    return markov_chain.generate_sentence(app.longer_model)
