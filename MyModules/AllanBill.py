from MyModules import (
    Aj as AJ,
    doTheMath as Math,
    TimerLoadBar as TimeBar,
    advancedData as A,
)
import sys
from os.path import dirname, abspath

d = dirname(dirname(abspath(__file__)))
sys.path.append(d)


wordsList = A.A.wordsList
WordsRepeated = A.A.WordsRepeated


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
    LettersRepeated = []
    allLowerLetters = "qwertyuiopasdfghjklzxcvbnm"
    for letters in allLowerLetters:
        LettersRepeated.append([0, letters])
    return LettersRepeated


def Grade(CurrentSortList, char):
    return Math.IndexGrade(CurrentSortList, CriticalSortList(char), 0)


class AllanBill:
    def __init__(self, whichOne):
        self.WhichOne = whichOne
        self.letters()
        self.CurrentSortList()

    def letters(self):
        Letters = "".join(wordsList)
        couldBeWrong = " ".join("1234567890'").split()
        for sym in couldBeWrong:
            Letters = Letters.replace(sym, "")
        return Letters

    def CurrentSortList(self):
        letters = self.letters()
        LettersRepeated = allLowerLetters()

        if self.WhichOne == "A":
            for element in LettersRepeated:
                TimeBar.Adding()
                for index in range(len(letters)):
                    if letters[index] == element[1]:
                        element[0] += 1
            LettersRepeated.sort(reverse=True)
            return LettersRepeated

        if self.WhichOne == "B":
            Letter = WordsRepeated
            for element in LettersRepeated:
                TimeBar.Adding()
                for letter in Letter:
                    if letter[1][0] == element[1]:
                        element[0] += letter[0]
            LettersRepeated.sort(reverse=True)
            return LettersRepeated

    def Grade(self):
        return Math.IndexGrade(
            self.CurrentSortList(), CriticalSortList(self.WhichOne), 0
        )

    def ShowLettersSort(self):
        return Math.IndexGrade(
            self.CurrentSortList(), CriticalSortList(self.WhichOne), 1
        )

    def LettersRepeatedJson(self):
        return AJ.CreateJsonObject(self.CurrentSortList())
