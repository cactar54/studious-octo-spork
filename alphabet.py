def alphabet(array, letter):
    matchingItems = []

    for item in array:
        if item[0].lower() == letter.lower():
            matchingItems.append(item)

    return matchingItems
