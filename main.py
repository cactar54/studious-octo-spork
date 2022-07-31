from combine import combine
from reverse import reverse
from alphabet import alphabet
from mirror import mirror
from randomizer import randomizeOrder
from randomizer import randomizeSpelling

#Enter letter you wish to search for in the alphabet function here
searchLetter = "d"

if __name__ == "__main__":
    animals = ["Horse", "Dog", "Cat", "Panda", "Snake"]

    print(reverse(animals))
    print(combine(animals))
    print(alphabet(animals, searchLetter))
    print(mirror(animals))
    print(randomizeOrder(animals))
    print(randomizeSpelling(animals))