#!/usr/env python

import time


def reject_description(description):
    print(description)
    descriptionRejected = False

    numberOfVowels = count_vowels(description)
    moduleVowels = numberOfVowels % 10
    numberOfChars = len(description)
    moduleChar = numberOfChars % 10
    if moduleChar == 0:
        descriptionRejected = True

    # latencia variable
    timeToSleep = moduleChar * 0.20

    # latencia muy grande
    if (moduleChar == moduleVowels) and (moduleChar == 5):
        timeToSleep += 60

    print("durmiendo " + str(timeToSleep))
    time.sleep(timeToSleep)

    return descriptionRejected


def count_vowels(string):
    numVowels = 0
    for char in string:
        if char in "aeiouAEIOU":
            numVowels = numVowels + 1
    return numVowels
