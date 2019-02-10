import sys
import random

# 2. Random Dictionary Words
# Stretch Challenges


def auto_complete_program():
    with open('/usr/share/dict/words', 'r') as f:
        content_of_file = f.read()

    answer_array = []
    letter = sys.argv[1]

    lines = content_of_file.split()
    while len(answer_array) != 10:
        line_number = random.randrange(0, len(lines))
        if lines[line_number][0] == letter:
            answer_array.append(lines[line_number])

    return answer_array

if __name__ == '__main__':
    print(auto_complete_program())
