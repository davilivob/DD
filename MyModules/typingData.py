import sys
from os.path import dirname, abspath

d = dirname(dirname(abspath(__file__)))
sys.path.append(d)

from MyModules import (
    readFiles as File,
    doTheMath as Math,
    Aj as AJ,
    ragularData as R,
    advancedData as A,
    TimerLoadBar as TimeBar,
)

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


class TypingTest:
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
            char[0] = float(char[0]) / ((len(A.A.wordsList) - R.R.learned * 2))
        TimeBar.Adding()

    TypoRate.sort(reverse=True)
    MostTypo = TypoRate[1][1]

    TypoRateJson = AJ.CreateJsonObject(TypoRate)
