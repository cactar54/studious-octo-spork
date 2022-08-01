from combine import combine
from reverse import reverse
from alphabet import alphabet
from mirror import mirror
from randomizer import randomize_order
from randomizer import randomize_spelling

#Enter letter you wish to search for in the alphabet function here
searchLetter = "d"

if __name__ == "__main__":
    animals = ["Horse", "Dog", "Cat", "Panda", "Snake"]

    print(reverse(animals))
    print(combine(animals))
    print(alphabet(animals, searchLetter))
    print(mirror(animals))
    print(randomize_order(animals))
    print(randomize_spelling(animals))