import sys
import random

def rearranging():
    # ['how', 'now', 'brown', 'cow']
    arrayOfWords = sys.argv[1:]

    # for i in the len of (array - 1) down until 0 by going down -1 each time
    for i in range(len(arrayOfWords)-1, 0, -1):
        # picking a rondom index from 0...i
        rand_index = random.randint(0, i+1)
        # basically swaping the current index item with the random index item in the array
        arrayOfWords[i], arrayOfWords[rand_index] = arrayOfWords[rand_index], arrayOfWords[i]

    return arrayOfWords

if __name__ == '__main__':
    print(rearranging())
