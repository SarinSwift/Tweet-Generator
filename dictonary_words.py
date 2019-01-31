import random
import sys

# 2. Random Dictionary Words

def get_random_word(file):
    sentence_string = ""
    array_of_number = sys.argv[1]

    with open(file, 'r') as f:
        content_of_file = f.read()


    lines = content_of_file.split()
    for i in range(0, int(array_of_number[0])):
        line_number = random.randrange(len(lines))

        sentence_string += (lines[line_number] + " ")

    return sentence_string


def random_sentence_from_dict(file):
    array_string = []
    array_of_number = sys.argv[1]

    # make an indented block that acesses the file and as soon as you leave the block, it automatically closes the file
    with open(file, 'r') as f:
        # gets everything from the file (one huge entire string of content)
        content_of_file = f.read()

    # an array of words in the file we read from
    lines = content_of_file.split()
    for i in range(0, int(array_of_number[0])):

        # random number in the range 0 -> len of lines
        # gets valid indexes
        line_number = random.randrange(len(lines))

        array_string.append(lines[line_number])

    answer_string = " ".join(array_string) + "."

    return answer_string.capitalize()



if __name__ == '__main__':
    # print(get_random_word('/Users/sarinswift/Desktop/Designs/words_sample.txt'))
    print(random_sentence_from_dict('/usr/share/dict/words'))
