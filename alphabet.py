def alphabet(array, letter):
    matchingItems = []
    firstLetters = []
    position = 0

    for item in array:
        firstLetters.append(array[position][0])
        if letter.isupper():
            if firstLetters[position] == letter:
                matchingItems.append(item)

        if letter.islower():
            if firstLetters[position] == letter.upper():
                matchingItems.append(item)

        position += 1

    return matchingItems
