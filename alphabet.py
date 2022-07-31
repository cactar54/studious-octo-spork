def alphabet(array, letter):
    matchingItems = []
    arrayPosition = 0

    for item in array:
        if (item[0] == letter):
            matchingItems[arrayPosition] = item
            arrayPosition += 1
    return matchingItems