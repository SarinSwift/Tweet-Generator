
# 3. Analyze Word Frequency In Text


def histogram():
    histogram = {}

    with open('/Users/sarinswift/Desktop/Designs/words_sample.txt', 'r') as f:
        content_of_file = f.read()
    array = content_of_file.split()

    for word in array:
        if histogram.get(word) == None:
            histogram[word] = 1
        else:
            histogram[word] += 1

    return histogram


def histogram_list0flist():
    histogram = []

    with open('/Users/sarinswift/Desktop/Designs/words_sample.txt', 'r') as f:
        content_of_file = f.read()
    array = content_of_file.split()

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


def histogram_listOfTuples():
    # using the dictionary to add the items in the tuple
    dictionary = histogram()
    listTuples = []

    for key in dictionary:
        # print(key, dictionary[key])
        listTuples.append((key, dictionary[key]))

    return listTuples



def unique_words(histogram):
    unique_count = 0

    for count in histogram.values():
        if count == 1:
            unique_count += 1

    return unique_count


def frequency(word, histogram):
    print(histogram)
    freq = 0

    for pair in histogram:
        print(pair)

    return freq


if __name__ == '__main__':
    # print(histogram())
    # print(unique_words(histogram()))
    # print(frequency('fish', histogram()))

    # print(histogram_list0flist())
    print(histogram_listOfTuples())
