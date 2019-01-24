import sys
import random


# making swaps within the same array
def rearranging():
    # ['how', 'now', 'brown', 'cow']
    arrayOfWords = sys.argv[1:]
    answerString = " "

    # for i in the len of (array - 1) down until 0 by going down -1 each time
    for i in range(len(arrayOfWords)-1, 0, -1):
        # picking a rondom index from 0...i
        rand_index = random.randint(0, i+1)
        # basically swaping the current index item with the random index item in the array
        arrayOfWords[i], arrayOfWords[rand_index] = arrayOfWords[rand_index], arrayOfWords[i]

    return answerString.join(arrayOfWords)


 # 2nd method using choice() method 
def rearrange():
    array = sys.argv[1:]
    randomized = []
    answerString = " "

    for i in range(1, len(sys.argv)):
        random_item = random.choice(array)
        randomized.append(random_item)
        array.remove(random_item)

    return answerString.join(randomized)



if __name__ == '__main__':
    print(rearranging())
    print(rearrange())
