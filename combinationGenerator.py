import random


def combinationGenerator():
    listLetters = ['A', 'B', 'C']
    listNumbers = [1,2,3,4,5]

    resultSet = []

    while len(resultSet) < 30:
        tempLetters = listLetters.copy()
        tempNumbers = listNumbers.copy()

        combination = []
        while len(tempLetters) > 0:

            randomLetter = random.choice(tempLetters)

            if randomLetter == 'A':
                # can only be combined with 1 number
                randomNumber = random.choice(tempNumbers)
                tempNumbers.remove(randomNumber)

                unit = {randomLetter, randomNumber}
                combination.append(unit)
            else:
                #can be combined with two numbers
                randomNumber1 = random.choice(tempNumbers)
                tempNumbers.remove(randomNumber1)
                randomNumber2 = random.choice(tempNumbers)
                tempNumbers.remove(randomNumber2)

                unit = {randomLetter, randomNumber1, randomNumber2}
                combination.append(unit)

            tempLetters.remove(randomLetter)

        if combination not in resultSet:
            print("koekoek")
            resultSet.append(combination)
        else:
            print("whoops got a duplicate")
            continue

    return resultSet
