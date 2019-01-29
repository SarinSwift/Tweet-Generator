
def histogram():
    sentence = "one fish two fish red fish blue fish"
    array = sentence.split()
    dict = {}

    for word in array:
        if dict.get(word) == None:
            dict[word] = 1
        else:
            dict[word] += 1

    return dict

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
    print(histogram())
    print(unique_words(histogram()))
    print(frequency('fish', histogram()))
