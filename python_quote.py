
import random

quotes = ("It's just a flesh wound.",
          "He's not the Messiah. He's a very naughty boy!",
          "THIS IS AN EX-PARROT!!")

rand_index = random.randint(0, len(quotes) - 1)
print(quotes[rand_index])
