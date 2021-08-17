import time
import sys
from os.path import dirname, abspath

d = dirname(dirname(abspath(__file__)))
sys.path.append(d)
print()
progress, efficiencyTest, RankingList = (
    0,
    True,
    input("Please Enter The Number of Words Ranking You Want: "),
)
from AnalyzingApp import TimerLoadBar as TimeBar
time_start = TimeBar.Counter.start
print()
from AnalyzingApp import readFiles as File

prevTime, lastAllan = File.Load.prevTime, File.Load.lastAllan


def timeNow():
    return time.time() - time_start


import string
import json
import math
from AnalyzingApp import art as Art

TimeBar.Adding()
from AnalyzingApp import math as Math

TimeBar.Adding()
from AnalyzingApp import Aj as AJ

TimeBar.Adding()
from AnalyzingApp import ragularData as R

TimeBar.Adding()
from AnalyzingApp import AllanBill as AB

TimeBar.Adding()
from AnalyzingApp import advancedData as A

TimeBar.Adding()

A = A.A

wordsList, WordsRepeated, WordsRepeatedJson = (
    A.wordsList,
    A.WordsRepeated,
    A.WordsRepeatedJson,
)

R = R.R
(sentences, vocabularies, definitions, comparisons, unlearned, learned, examples,) = (
    R.sentences,
    R.vocabularies,
    R.definitions,
    R.comparisons,
    R.unlearned,
    R.learned,
    R.examples,
)


def AddingFiller():
    while timeNow() < prevTime:
        TimeBar.Adding()


class Ranking:
    def __init__(self):
        self.RankRange()

    def RankRange(self):
        if RankingList == "" or Math.checkNumber(RankingList) == False:
            RankRange = 0
        elif RankingList == "all" or int(RankingList) >= len(WordsRepeated):
            RankRange = len(WordsRepeated)
        elif Math.checkNumber(RankingList) == True:
            RankRange = int(RankingList)

        return RankRange

    def TopUsed(self):
        TopUsed = ""
        arr = Math.createRankinglistArray(self.RankRange())
        for index in arr:
            if index < Math.row():
                TopUsed += "\n      "
            Word = str(index + 1) + '. "' + WordsRepeated[index][1].capitalize() + '"'
            Amount = ": " + str(WordsRepeated[index][0]) + " "
            Percentage = Math.percent(WordsRepeated()[index][0], len(wordsList), 100)
            TopUsed += Art.FormalFiller(Word + Amount + Percentage, 3)

        return TopUsed


class AllanBill:
    def __init__(self, whichOne):
        self.WhichOne = whichOne
        self.letters()
        self.CurrentSortList()

    def letters(self):
        return "".join(wordsList)

    def CurrentSortList(self):
        letters = self.letters()
        LettersRepeated = AB.allLowerLetters()
        if self.WhichOne == "A":
            for element in LettersRepeated:
                TimeBar.Adding()
                for letter in letters:
                    if letter == element[1]:
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
            self.CurrentSortList(), AB.CriticalSortList(self.WhichOne), 0
        )

    def ShowLettersSort(self):
        return Math.IndexGrade(
            self.CurrentSortList(), AB.CriticalSortList(self.WhichOne), 1
        )

    def LettersRepeatedJson(self):
        return AJ.CreateJsonObject(self.CurrentSortList())


Allan = AllanBill("A")
Bill = AllanBill("B")


class TypingTest:
    TypingDatas = File.Load.typingDatas
    totaltime, wpm, accuracy, totalback, totalchars, goodchars = 0, 0, 0, 0, 0, 0
    WrongWords, WrongChars = [], []

    for test in TypingDatas:
        TimeBar.Adding()
        totaltime += test["TestLength"]
        totalback += test["TotalBack"]
        totalchars += test["TotalChars"]
        goodchars += test["GoodChars"]

        for word in test["WrongWords"]:
            WrongWords.append(word)
            TimeBar.Adding()

        for char in test["WrongChars"]:
            WrongChars.append(char)
            TimeBar.Adding()

    avgTime, avgWpm, avgCpm, avgAccuracy, avgBackrate = (
        totaltime / len(TypingDatas),
        totalchars / (5 * totaltime),
        totalchars / totaltime,
        goodchars / totalchars,
        totalback / totalchars,
    )

    avgTimePrint, avgWpmPrint, avgCpmPrint, avgAccuracyPrint, avgBackratePrint = (
        Math.takeDecimal(totaltime, len(TypingDatas), 10),
        Math.takeDecimal(totalchars / 5, totaltime, 100),
        Math.takeDecimal(totalchars, totaltime, 100),
        Math.takeDecimal(goodchars * 100, totalchars, 100),
        Math.takeDecimal(totalback * 100, totalchars, 100),
    )
    WrongWordsRepeated, WrongCharsRepeated = (
        AJ.CreateRepeatedArray(WrongWords),
        AJ.CreateRepeatedArray(WrongChars),
    )
    WrongWordsRepeatedJson, WrongCharsRepeatedJson = (
        AJ.CreateJsonObject(WrongWordsRepeated),
        AJ.CreateJsonObject(WrongCharsRepeated),
    )

    TypoRate = WrongCharsRepeated
    for char in TypoRate:
        if str(char[1]) != "Symbols" and str(char[1]) != "Spaces":
            char[0] = float(char[0]) / File.Load.lastCharsRepeated[str(char[1])]
        if str(char[1]) == "Spaces":
            char[0] = float(char[0]) / ((len(wordsList) - learned * 2))
        TimeBar.Adding()

    TypoRate.sort(reverse=True)
    MostTypo = TypoRate[1][1]

    TypoRateJson = AJ.CreateJsonObject(TypoRate)


Type = TypingTest


def UploadDatasToJson():
    WordsKinds = len(WordsRepeated)
    TotalWords = len(wordsList)
    TotalChars = len(Allan.letters())
    CharsPerWord = Math.takeDecimal(len(Allan.letters()), len(wordsList), 100000)
    AllanJson = {
        "Allan Poe Index": float(Allan.Grade()[3:-3]),
        "Bill Murray Index": float(Bill.Grade()[3:-3]),
    }
    analysisJson = {
        "Vocabularies": {
            "Total": vocabularies,
            "Learned": learned,
            "Unlearned": unlearned,
        },
        "Sentences": {
            "Total": sentences,
            "Examples": examples,
            "Definitions": definitions,
            "Comparisons": comparisons,
        },
        "Advanced Datas": {
            "Words Kinds": WordsKinds,
            "Total Words": TotalWords,
            "Total Characters": TotalChars,
            "Characters Repeated Times": Allan.LettersRepeatedJson(),
            "First Letters Repeated Times": Bill.LettersRepeatedJson(),
            "Letters Per Words": CharsPerWord,
        },
        "Typing Results": {
            "Test Duration": Type.avgTime,
            "WPM": Type.avgWpm,
            "Accuracy": Type.avgAccuracy,
            "BackSpace Press Rate": Type.avgBackrate,
            "Wrong Words List": Type.WrongWordsRepeatedJson,
            "Wrong Chars List": Type.WrongCharsRepeatedJson,
            "Typo Rate": Type.TypoRateJson,
        },
    }

    with open("Databases\Database.json", mode="w") as file:
        json.dump(
            [
                {"Words List": wordsList},
                {"Words Repeat Time": WordsRepeatedJson},
                {"Analysing Results": analysisJson},
                {"Project Statment": AllanJson},
                {"Last Loading Time": timeNow()},
            ],
            file,
        )


class Write:
    AllanRate = (
        Art.FontEffect("Allan Poe Index:    ", 83, 1)
        + Art.FontEffect(str(Allan.Grade())[2:-1], 0, 1)
        + "\n"
        + Art.FontEffect(
            Art.LoadBar(float(str(Allan.Grade())[2:-3]) / 100, 100, 0), 185, 0
        )
    )
    AllanResult = "Result:          " + Allan.ShowLettersSort()[0:-2]

    BillRate = (
        Art.FontEffect("Bill Murray Index:  ", 83, 1)
        + Art.FontEffect(str(Bill.Grade())[2:-1], 0, 1)
        + "\n"
        + Art.FontEffect(
            Art.LoadBar(float(str(Bill.Grade())[2:-3]) / 100, 100, 0), 185, 0
        )
    )
    BillResult = "Result:          " + Bill.ShowLettersSort()[0:-2]

    Vocabularies = Art.FontEffect("Vocabularies: ", 160, 1) + str(vocabularies)

    Learned = "Learned: " + str(learned) + Math.percent(learned, vocabularies, 10)
    Unlearned = (
        "Unlearned: " + str(unlearned) + Math.percent(unlearned, vocabularies, 10)
    )
    Individuals = "Individuals: " + str(len(WordsRepeated))

    Sentences = Art.FontEffect("Sentences:    ", 160, 1) + str(sentences)
    Examples = "Examples: " + str(examples) + Math.percent(examples, sentences, 10)
    Definitions = (
        "Definitions: " + str(definitions) + Math.percent(definitions, sentences, 10)
    )
    Comparisons = (
        "Comparisons: " + str(comparisons) + Math.percent(comparisons, sentences, 10)
    )

    TotalWords = "Total Words: " + str(len(wordsList))
    TotalCharacters = "Total Characters: " + str(len(Allan.letters()))
    LettersPerWord = "Letters Per Word: " + str(
        Math.takeDecimal(len(Allan.letters()), len(wordsList), 1000)
    )

    avgTime = "Test Duration: " + str(Type.avgTimePrint) + " mins"
    avgWpm = "WPM: " + str(Type.avgWpmPrint)
    avgAccuracy = "Accuracy: " + str(Type.avgAccuracyPrint) + " %"
    avgBackrate = "Back Rate: " + str(Type.avgBackratePrint) + " %"
    MostType = "Most Typo: " + '"' + Type.MostTypo + '"'


if efficiencyTest == False:
    AddingFiller()


UploadDatasToJson()

print()
print()
print(
    Art.FontEffect(
        "".join(
            [
                "(Calculate Completed in ",
                str(Math.takeDecimal(timeNow(), 1, 10000)),
                " seconds)",
            ]
        ),
        240,
        0,
    )
)

print()

Art.Print.ln(Write.AllanRate)
Art.Print.tabln(
    Art.FontEffect(
        "Stantard:        e, t, a, o, i, n, s, h, r, d, l, c, u, m, w, f, g, y, p, b, v, k, j, x, q, z",
        0,
        1,
    )
)
Art.Print.tabln(Write.AllanResult)
Art.Print.ln(Write.BillRate)
Art.Print.tabln(
    Art.FontEffect(
        "Stantard:        t, a, s, h, w, i, o, b, m, f, c, l, d, p, n, e, g, r, y, u, v, j, k, q, x, z",
        0,
        1,
    )
)
Art.Print.tabln(Write.BillResult)
Art.Print.ln(Write.Vocabularies)
Art.Print.tabln(
    Art.FormalFiller(Write.Learned, 3)
    + Art.FormalFiller(Write.Unlearned, 3)
    + Write.Individuals
)
Art.Print.ln(Write.Sentences)
Art.Print.tabln(
    Art.FormalFiller(Write.Examples, 3)
    + Art.FormalFiller(Write.Definitions, 3)
    + Write.Comparisons
)
Art.Print.ln(Art.FontEffect("Advanced Datas: ", 201, 1))
Art.Print.tabln(
    Art.FormalFiller(Write.TotalWords, 3)
    + Art.FormalFiller(Write.TotalCharacters, 3)
    + Write.LettersPerWord
)
Art.Print.ln(Art.FontEffect("Typing Test Results: ", 165, 1))
fillerForType = " " * int(
    (
        110
        - len(
            Write.MostType
            + Write.avgAccuracy
            + Write.avgWpm
            + Write.avgBackrate
            + Write.avgTime
        )
    )
    / 4
)
Art.Print.tabln(
    Write.MostType
    + fillerForType
    + Write.avgAccuracy
    + fillerForType
    + Write.avgWpm
    + fillerForType
    + Write.avgBackrate
    + fillerForType
    + Write.avgTime
)
print(Art.FontEffect("TOP " + str(Ranking().RankRange()) + " USED WORDS: ", 208, 1))
Art.Print.tabln(Ranking().TopUsed())
