import sys

# 1. Let's Get Started
# Bonus challenges: cowsay

def cowsay():

    array_argument = sys.argv[1:]
    string_words = " ".join(array_argument)

    underscores = ""
    for i in range(0, len(string_words)):
        underscores += "_"



    cow_string = """
         \   ^__^
          \  (oo)\_______
             (__)\       )\/\\
                 ||----w |
                 ||     ||
    """

    return underscores + "\n" + string_words + "\n" + underscores + cow_string


if __name__ == '__main__':
    print(cowsay())
