
import re
import string
import random
from dictogram import Dictogram

def open_file(file):
    '''
    Returns a list of words in the whole textfile
    '''
    with open(file, 'r') as f:
        content_of_file = f.read()
        content_of_file = content_of_file.replace(".", "").replace(",", "").replace("*", "").replace(string.punctuation, "").replace("?", "").replace("!", "").replace(";", "").replace(":", "").replace('“', "").replace('”', "").replace('-', "")

    array = content_of_file.split()
    return array


def markov_chain(file):
    '''
    Creates the markov model as such: {'one': {'fish': 1}, 'fish': {'two': 1, 'red': 1, 'blue': 1},
                                       'two': {'fish': 1}, 'red': {'fish': 1}, 'blue': {'fish': 1}}
    '''
    histogram = {}

    # create this >>> {'one': {}, 'fish': {}, 'two': {}, 'red': {}, 'blue': {}}
    for word in file:   # is a single string of the word
        if word not in histogram:
            histogram[word] = {}

    # adds in the nested histogram
    index = 0
    for word in file:
        if index + 1 < len(file):
            next_word = file[index+1]
            if next_word in histogram[word].keys():
                histogram[word][next_word] += 1
            else:
                histogram[word][next_word] = 1
            index += 1

    return histogram



def generate_start_word(chain):
    '''
    Returns a random starting word
    TODO: Make more accurate by selecting words from a text file that is the *start* words in different sentences
    '''
    worddd = random.choice(list(chain.keys()))      # python3: need to change this to a list to use indexing on it

    return worddd


def generate_sentence(chain):
    '''
    Generates a random sentence from the main markov chain model
    Generates a sentence with the input length of words
    '''
    length = 10
    starting_word = generate_start_word(chain)
    sentence = [starting_word]

    for i in range(length-1):
        dict_of_following = chain[starting_word]
        sentence.append(generate_start_word(chain[sentence[i]]))


    my_string = " ".join(sentence)
    return my_string


def pick_rand_word(dict):
    '''
    Picks a random word from the nested dict that contains the following words
    (code from sample.py)
    '''
    total_count = len(dict)
    print(total_count)
    cumulative_probability = 0
    randomized = random.random()

    for key in dict:
        cumulative_probability += dict[key] / total_count
        if cumulative_probability > randomized:
            return key




# def markov_chain_second(sentence):
#     histogram = {}
#     sentence_array = sentence.split()
#     double_words_arr = []
#
#     # create this >>> {'one fish': {}, 'fish two': {}, 'two fish': {}, 'fish red': {}, 'red fish': {}, 'fish blue': {}}
#     for i in range(len(sentence_array)-2):
#         empt_string = ""
#         empt_string += sentence_array[i]
#         empt_string += " "
#         empt_string += sentence_array[i+1]
#         double_words_arr.append(empt_string)
#         if empt_string not in histogram:
#             histogram[empt_string] = {}
#
#     # need to also loop through the sentence_array to get the words in the text
#     print(histogram)
#     print(double_words_arr)


if __name__ == '__main__':
    # model = markov_chain(open_file('/Users/sarinswift/Desktop/Designs/words_sample.txt'))
    longer_model = markov_chain(open_file('WarAndPeace.txt'))

    # print(generate_sentence(10, longer_model))
    print(generate_sentence(longer_model))
