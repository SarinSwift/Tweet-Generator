import random
import sys


def get_random_word(file):
    sentence_string = ""
    array_of_number = sys.argv[1]

    with open(file, 'r') as f:
        content_of_file = f.read()

    for i in range(0, int(array_of_number[0])):
        lines = content_of_file.split()
        line_number = random.randrange(0, len(lines))

        sentence_string += (lines[line_number] + " ")

    return sentence_string


def random_sentence_from_dict(file):
    array_string = []
    array_of_number = sys.argv[1]

    with open(file, 'r') as f:
        content_of_file = f.read()

    for i in range(0, int(array_of_number[0])):
        lines = content_of_file.split()
        line_number = random.randrange(0, len(lines))

        array_string.append(lines[line_number])

    answer_string = " ".join(array_string) + "."

    return answer_string.capitalize()


if __name__ == '__main__':
    # print(get_random_word('/Users/sarinswift/Desktop/Designs/words_sample.txt'))
    print(random_sentence_from_dict('/usr/share/dict/words'))
