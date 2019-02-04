import random

# 4. Stochastic Sampling

def sample():
    sentence = "one fish two fish red fish blue fish"
    sentence_array = sentence.split()

    dict = histogram(sentence_array)

    # keeps count of where it's covered so far on the line
    currentTaken = 0
    for key in dict:
        # the percentage that the word can appear
        percentage = dict[key]/len(sentence_array) + currentTaken
        dict[key] = [currentTaken, percentage]
        currentTaken = percentage

    randomized = random.random()
    for key in dict:
        # return the key that has the value between the randomized number
        if dict[key][0] < randomized < dict[key][1]:
            return key



    return


def histogram(array):
    histogram = {}

    for word in array:
        if histogram.get(word) == None:
            histogram[word] = 1
        else:
            histogram[word] += 1

    return histogram

if __name__ == '__main__':
    print(sample())
