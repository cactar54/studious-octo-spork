def mirror (array):
    mirroredArray = []
    loops = 0

    for item in array:
        reversedString = item[::-1]
        mirroredArray.append(reversedString)
        loops += 1

    return mirroredArray