import sys
import string
from os.path import dirname,abspath
d = dirname(dirname(abspath(__file__)))
sys.path.append(d)
import Aj as AJ
import math as Math

def CriticalSortList(char):
    if char == "A":
        return [
            "e",
            "t",
            "a",
            "o",
            "i",
            "n",
            "s",
            "h",
            "r",
            "d",
            "l",
            "c",
            "u",
            "m",
            "w",
            "f",
            "g",
            "y",
            "p",
            "b",
            "v",
            "k",
            "j",
            "x",
            "q",
            "z",
        ]
    if char == "B":
        return [
            "t",
            "a",
            "s",
            "h",
            "w",
            "i",
            "o",
            "b",
            "m",
            "f",
            "c",
            "l",
            "d",
            "p",
            "n",
            "e",
            "g",
            "r",
            "y",
            "u",
            "v",
            "j",
            "k",
            "q",
            "x",
            "z",
        ]

def allLowerLetters():
    allLowerLetters = list(string.ascii_lowercase)
    LettersRepeated = AJ.CreateRepeatedArray(allLowerLetters)
    return LettersRepeated

def Grade(CurrentSortList, char):
    return Math.IndexGrade(CurrentSortList, CriticalSortList(char), 0)
