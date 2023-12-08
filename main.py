from numpy import log

letters = {

    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0,
    10: 0,
    11: 0,
    12: 0,
    13: 0,
    14: 0,
    15: 0,
    16: 0,
    17: 0,
    18: 0,
    19: 0,
    20: 0,
    21: 0,
    22: 0,
    23: 0,
    24: 0,
    25: 0,
    26: 0

}


def readFile(fileName):
    file = open(fileName, "r")
    words = file.read().splitlines()  # puts the file into an array
    file.close()
    text = ""
    for i in words:
        text = text + i
    return listRemoveNoise(text)

def listRemoveNoise(string):
    string = string.upper()
    array = list(string)
    newList = []
    for i in range(0, len(array)):
        if ord(array[i]) - 65 < 26 and ord(array[i]) - 65 >= 0:
            newList.append(array[i])
    return newList


def lettersCount(array):
    count = []
    for i in range(26):
        count.append(0)

    for j in range(0, len(array)):
        count[ord(array[j]) - 65] = count[ord(array[j]) - 65] + 1
    return count

def lettersFrequency(array):
    count = lettersCount(array)
    frequency = []
    for i in range(26):
        frequency.append([chr(i + 65), count[i] / len(array)])
    return frequency


def textInBlocks(text, m):
    # TRANSFORM THE TEXT IN A LIST OF BLOCKS
    blocks = []
    tmp = []
    j = 0
    for i in range(0, len(text)):
        # CONSTRUCTION OF BLOCKS OF LENGTH m
        if j == m:
            # FULL BLOCK IS INSERTED IN THE LIST
            blocks.append(tmp)
            tmp = []
            j = 0

        tmp.append(ord(text[i]) - 65)
        j = j + 1

    # VERIFY IF THE LAST BLOCK IS FULL
    if len(tmp) == 0:
        # IF THE LAST BLOCK IS EMPTY
        return blocks
    elif len(tmp) < m:
        # IF THE LAST BLOCK IS NOT EMPTY BUT IS NOT FULL
        for i in range(len(tmp), m):
            tmp.append(-1)

    blocks.append(tmp)

    return blocks

def getDistributionBlock(blocks):
    distr = [[blockToString(blocks[0]), 1]]
    for i in range(1, len(blocks)):
        appendNoDuplicate(distr, blockToString(blocks[i]))
    return distr


def appendNoDuplicate(array, block):
    for i in array:
        if i[0] == block:
            i[1] = i[1] + 1
            return 0
    array.append([block, 1])
    return 1

def getFrequencyBlock(blocks):
    frequency = getDistributionBlock(blocks)
    for i in frequency:
        i[1] = i[1]/len(blocks)
    return frequency



def coincidenceIndexBlocks(distributionBlocks, n):
    index = 0
    for i in distributionBlocks:
        index = index + i[1] / n * (i[1]-1)/(n-1)

    return index


def entropyBlocks(distributionBlocks, n):
    H = 0
    for i in distributionBlocks:
        H = H + i[1] / n * log(i[1] / n)

    return -1 * H


def blockToString(block):
    # TRANSFORM A BLOCK TO STRING
    result = []
    for j in range(0, len(block)):
        result.append(chr(block[j] % 26 + 65))
    return "".join(result)


file = "mobydick.txt"
message = readFile(file)

freq = lettersFrequency(message)

print(f"LETTERS FREQUENCY IN FILE: {file}")
print()
for i in freq:
    print(i)


# ANALYSIS WITH BLOCKS
m = 4           # Block length
blocks = textInBlocks(message, m)
print()

print("BLOCK DISTRIBUTION")
disBlocks = getDistributionBlock(blocks)
for i in disBlocks:
    print(i)

print()
print(f"COINCIDENCE INDEX FOR BLOCK LENGTH m = {m} --> {coincidenceIndexBlocks(disBlocks, len(blocks))}")
print()
print(f"COINCIDENCE INDEX FOR BLOCK LENGTH m = {m} --> {entropyBlocks(disBlocks, len(blocks))}")
