# reverse strings 

def reverse_word(word):
    # return "".join(reversed(word))
    # return word[::-1]

    return ''.join(word[i] for i in range(len(word)-1, -1, -1))


if __name__ == '__main__':
    word = "look"
    print(reverse_word(word))
