
def markov_chain(sentence):
    histogram = {}
    sentence_array = sentence.split()

    # create this >>> {'one': {}, 'fish': {}, 'two': {}, 'red': {}, 'blue': {}}
    for word in sentence_array:
        if word not in histogram:
            histogram[word] = {}

    # adds in the nested histogram
    index = 0
    for word in sentence_array:
        if index + 1 < len(sentence_array):
            next_word = sentence_array[index+1]
            if next_word in histogram[word].keys():
                histogram[word][next_word] += 1
            else:
                histogram[word][next_word] = 1
            index += 1

    return histogram



if __name__ == '__main__':
    print(markov_chain("one fish two fish red fish blue fish"))
