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

# sample.py function we covered in class
def sample_in_class():
    sentence = "one fish two fish red fish blue fish"
    sentence_array = sentence.split()
    dict = histogram(sentence_array)

    total_count = len(sentence_array)
    cumulative_probability = 0

    randomized = random.random()
    for key in dict:
        cumulative_probability += dict[key] / total_count
        if cumulative_probability > randomized:
            return key


def histogram(array):
    histogram = {}

    for word in array:
        if histogram.get(word) == None:
            histogram[word] = 1
        else:
            histogram[word] += 1

    return histogram


def test_probability():
    dict = {'one': 0, 'fish': 0, 'two': 0, 'red': 0, 'blue': 0}

    for i in range(0, 10000):
        dict[sample()] += 1

    print(dict)



if __name__ == '__main__':
    # print(sample())
    print(sample_in_class())
    # print(test_probability())
