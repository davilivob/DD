import sys
from os.path import dirname, abspath

d = dirname(dirname(abspath(__file__)))
sys.path.append(d)

from MyModules import (
    readFiles as File,
    doTheMath as Math,
    Aj as AJ,
    regularData as R,
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

    for char in test["WrongChars"]:
        WrongChars.append(char)
        TimeBar.Adding()


class TypingTest:
    allCharsIWant = " ".join("qwertyuiopasdfghjklzxcvbnm").split()
    allCharsIWant.append("Spaces")

    totalTime, totalChars = totaltime, totalchars
    testNumber, avgTime, avgWpm, avgCpm, avgAccuracy, avgBackrate = (
        len(TypingDatas),
        totaltime / len(TypingDatas),
        totalchars / (5 * totalTime),
        totalchars / totalTime,
        (goodchars + totalback) / (totalchars + totalback),
        totalback / (totalchars + totalback),
    )

    avgTimePrint, avgWpmPrint, avgCpmPrint, avgAccuracyPrint, avgBackratePrint = (
        Math.takeDecimal(avgTime, 1, 100),
        Math.takeDecimal(avgWpm, 1, 100),
        Math.takeDecimal(avgCpm, 1, 100),
        Math.takeDecimal(avgAccuracy * 100, 1, 100),
        Math.takeDecimal(avgBackrate * 100, 1, 100),
    )
    WrongCharsRepeated = AJ.CreateRepeatedArray(WrongChars)
    

    for element in WrongCharsRepeated:
        if element[1] in allCharsIWant:
            allCharsIWant.remove(element[1])
    for char in allCharsIWant:
        WrongCharsRepeated.append([0, char])

    WrongCharsRepeatedJson = AJ.CreateJsonObject(WrongCharsRepeated)
    

    TypoRate = WrongCharsRepeated

    for char in TypoRate:
        if str(char[1]) != "Spaces":
            char[0] = float(char[0]) / File.Load.lastCharsRepeated[str(char[1])]
        if str(char[1]) == "Spaces":
            char[0] = float(char[0]) / ((len(A.A.wordsList) - R.R.learned * 2))
        TimeBar.Adding()

    TypoRate.sort(reverse=True)
    MostTypo = TypoRate[0][1]

    TypoRateJson = AJ.CreateJsonObject(TypoRate)
