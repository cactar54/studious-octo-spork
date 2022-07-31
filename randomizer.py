import random

def randomizeOrder(array):
    randomizedOrder = []
    arrayLength = len(array)
    usedNumbers = []

    while len(usedNumbers) < arrayLength:
        randomNumber = random.randrange(0, arrayLength, 1)
        if randomNumber not in usedNumbers:
            randomizedOrder.append(array[randomNumber])
            usedNumbers.append(randomNumber)

    return randomizedOrder




def randomizeSpelling(array):
    randomizedSpelling = []
    loops = 0
    usedNumbers = []

    for item in array:
        wordLength = len(array[loops])
        randomString = ""

        while len(usedNumbers) < wordLength:
            randomNumber = random.randrange(0, wordLength, 1)
            if randomNumber not in usedNumbers:
                randomString += array[loops][randomNumber]
                usedNumbers.append(randomNumber)

        randomizedSpelling.append(randomString)
        loops += 1
        usedNumbers = []


    return randomizedSpelling