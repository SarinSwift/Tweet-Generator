
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
    Takes in an array of words from the text file
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
    last_word = sentence[-1]

    for i in range(length-1):
        dict_of_following = chain[last_word]
        word_from_freq = pick_rand_word(dict_of_following)
        sentence.append(word_from_freq)
        last_word = sentence[-1]


    my_string = " ".join(sentence)
    return my_string


def pick_rand_word(dict):
    '''
    Picks a random word from the nested dict that contains the next follow up words
    (code from sample.py)
    '''
    total_count = len(dict)
    cumulative_probability = 0
    print(total_count)
    randomized = random.random()

    for key in dict:
        cumulative_probability += dict[key] / total_count
        if cumulative_probability > randomized:
            return key








def markov_chain_second(file):
    '''
    Creates the markov model as such: {('One', 'fish'): {'two': 1}, ('fish', 'two'): {'fish': 1}, ('two', 'fish'):
                                            {'red': 1}, ('fish', 'red'): {'fish': 1}, ('red', 'fish'): {'blue': 1},
                                            ('fish', 'blue'): {'fish': 1}}
    '''
    histogram = Dictogram()
    sentence_array = file
    second_histogram = Dictogram()

    # creates this >>> {('One', 'fish'): {}, ('fish', 'two'): {}, ('two', 'fish'): {}, ('fish', 'red'): {},
    #                  ('red', 'fish'): {}, ('fish', 'blue'): {}}
    for i in range(len(sentence_array)-2):
        curr_word = sentence_array[i]
        curr_word_next = sentence_array[i+1]
        histogram[(curr_word, curr_word_next)] = {}

    # creates this >>> {('One', 'fish'): {'two': 1}, ('fish', 'two'): {'fish': 1}, ('two', 'fish'): {'red': 1},
    #                  ('fish', 'red'): {'fish': 1}, ('red', 'fish'): {'blue': 1}, ('fish', 'blue'): {'fish': 1}}
    for i in range(len(sentence_array)-2):
        curr_word = sentence_array[i]
        curr_word_next = sentence_array[i+1]
        next_word = sentence_array[i+2]

        val = histogram[(curr_word, curr_word_next)]
        if next_word in val:
            val[next_word] += 1
        else:
            val[next_word] = 1

    return histogram


def generate_start_word_second(chain):
    '''
    Returns a random tuple pair     ex. ('only', 'thing')
    TODO: Make more accurate by selecting words from a text file that is the *start* words in different sentences
    '''
    tuple_words = random.choice(list(chain.keys()))      # python3: need to change this to a list to use indexing on it
    return tuple_words

def generate_sentence_second(chain):
    '''
    Generates a random sentence from the main markov chain model
    Generates a sentence with the input length of words
    '''
    length = 10
    starting_word = generate_start_word_second(chain)       # tuple
    sentence = [starting_word[0], starting_word[1]]         # [str, str]

    for i in range(length-1):
        dict_of_following = chain[(sentence[i], sentence[i+1])]
        # sentence.append(list(dict_of_following.keys())[0])
        sentence.append(pick_rand_word(dict_of_following))

    my_string = " ".join(sentence)
    return my_string + '.'


if __name__ == '__main__':
    ''' testing fist order markov chain'''
    # model = markov_chain(open_file('/Users/sarinswift/Desktop/Designs/words_sample.txt'))
    longer_model = markov_chain(open_file('WarAndPeace.txt'))
    # print(generate_sentence(model))
    print(generate_sentence(longer_model))

    ''' testing second order markov chain '''
    # longer_model_more = markov_chain_second(open_file('/Users/sarinswift/Desktop/Designs/pg1250.txt'))
    # print(generate_sentence_second(longer_model_more))

    # longer_model_more2 = markov_chain_second(open_file('corpus.txt'))
    # print(generate_sentence_second(longer_model_more2))

    # model3 = markov_chain_second(open_file('/Users/sarinswift/Desktop/Designs/words_sample.txt'))
    # print(generate_sentence_second(model3))


    # longer_model_more3 = markov_chain_second(open_file('/Users/sarinswift/Desktop/Designs/pg1250.txt'))
    # print(generate_sentence_second(longer_model_more3))

    # longer_model_more4 = markov_chain_second(open_file('corpus.txt'))
    # print(generate_sentence_second(longer_model_more4))

    # print(markov_chain_second("One fish two fish red fish blue One fish three move"))
    # print(markov_chain_second("One fish two fish red fish blue fish"))
