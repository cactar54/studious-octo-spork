def mirror (array):
    mirroredArray = []
    loops = 0

    for item in array:
        reversedString = array[loops][::-1]
        mirroredArray.append(reversedString)
        reversedString = ""
        loops += 1

    return mirroredArray