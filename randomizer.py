import random

def randomizeOrder(array):
    randomizedOrder = []
    arrayLength = len(array)
    usedNumbers = []
    randomNumber = 0

    while len(usedNumbers) < arrayLength:
        randomNumber = random.randrange(0, arrayLength, 1)
        if randomNumber not in usedNumbers:
            randomizedOrder.append(array[randomNumber])
            usedNumbers.append(randomNumber)

    return randomizedOrder







def randomizeSpelling(array):
    randomizedSpelling = []


    return randomizedSpelling