

# 1. Let's Get Started
# Stretch Challenges: Reverse words, Reverse sentences

def reverse_word(word):
    # return "".join(reversed(word))
    # return word[::-1]

    return ''.join(word[i] for i in range(len(word)-1, -1, -1))


def reverse_sentence(sentence):
    splited = sentence.split()
    reversedArray = []

    for i in range(len(splited)-1, -1, -1):
        reversedArray.append(splited[i])

    return ' '.join(reversedArray)

if __name__ == '__main__':
    word = "look"
    print(reverse_word(word))

    sentence = "sarin is coding"
    print(reverse_sentence(sentence))
