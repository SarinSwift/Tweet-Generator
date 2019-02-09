
# 3. Analyze Word Frequency In Text

def open_file():
    with open('/Users/sarinswift/Desktop/Designs/words_sample.txt', 'r') as f:
        content_of_file = f.read()
    array = content_of_file.split()
    return array

def histogram():
    histogram = {}

    array = open_file()

    for word in array:
        # if word not in histogram
        if histogram.get(word) == None:
            histogram[word] = 1
        else:
            histogram[word] += 1

    return histogram


def histogram_list_of_list():
    histogram = []

    array = open_file()

    # loop through indexes in the array
    for i in range(len(array)):
        word_found = False
        # if there's something in the histogram:
        if histogram:
            # looping through the histogram's indexes
            for j in range(len(histogram)):
                # if the word word in histogram == word in array:
                if histogram[j][0] == array[i]:
                    # add the count by 1
                    histogram[j][1] += 1
                    word_found = True
                    break

            # There's no words in the histogram, so we add the word with the count of 1
            if not word_found:
                histogram.append([array[i], 1])

        # nothing is in the histogram
        else:
            histogram.append([array[i], 1])

    return histogram


def histogram_list_list():
    histogram = []

    array = open_file()

    for word in array:
        for arr in histogram:
            if arr[0] == word:
                arr[1] += 1
        histogram.append([word, 1])

    return histogram


def histogram_list_of_tuples():
    # using the dictionary to add the items in the tuple
    dictionary = histogram()
    listTuples = []

    for key in dictionary:
        # print(key, dictionary[key])
        listTuples.append((key, dictionary[key]))

    return listTuples

# not using dictionary!!!
def histogram_list_tuples():
    histogram = []

    array = open_file()

    for word in array:
        found = False
        for inner in histogram:
            if word == inner[0]:
                count = inner[1] + 1
                # since it's immutable, we have to remove from histogram and then append a new one
                histogram.remove(inner)
                histogram.append((word, count))
                break
        if not found:
            histogram.append((word, 1))

    return histogram




def unique_words(histogram):
    unique_count = 0

    for count in histogram.values():
        if count == 1:
            unique_count += 1

    return unique_count


def frequency(word, histogram):
    return histogram[word]


if __name__ == '__main__':
    print(histogram())
    # print(histogram_list_of_list())
    # print(histogram_list_list())

    # print(histogram_list_of_tuples())
    # print(histogram_list_tuples())

    # print(unique_words(histogram()))
    # print(frequency('Sarin', histogram()))
