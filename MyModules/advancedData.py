# from AnalyzingApp.TimerLoadBar import Adding
import sys
from os.path import dirname, abspath

d = dirname(dirname(abspath(__file__)))
sys.path.append(d)

from MyModules import readFiles as File, Aj as AJ, TimerLoadBar as TimeBar


class A:
    weDontWant = " ".join('~!@#$%^&*()_+`}1234567890=[]{;:"\|,.<>?').split()
    keepItSpace = ["-", "  ","/"]
    Words = str.lower(File.Load.Dictionary)
    for element in keepItSpace:
        while element in Words:
            TimeBar.Adding()
            Words = Words.replace(element, " ")
    for char in weDontWant:
        Words = Words.replace(char, "")

    wordsList = str.split(Words)

    AJ.SeparateAllShort(wordsList)

    while "'" in wordsList:
        wordsList.remove("'")

    possessive = 0

    for word in wordsList:
        if "'s" in word or "s'" in word:
            possessive += 1
            if "'s" in word:
                wordsList.append(word.replace("'s", ""))
                wordsList.remove(word)
            else:
                wordsList.append(word.replace("'", ""))
                wordsList.remove(word)

    for num in range(possessive):
        wordsList.append("'s")

    WordsRepeated = AJ.CreateRepeatedArray(wordsList)

    WordsRepeatedJson = AJ.CreateJsonObject(WordsRepeated)

