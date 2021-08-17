import sys
import string
from os.path import dirname, abspath

d = dirname(dirname(abspath(__file__)))
sys.path.append(d)
import readFiles as File
import Aj as AJ
import TimerLoadBar as TimeBar


class A:
    allEnglishChar = list(
        string.ascii_lowercase + string.ascii_uppercase + " " + "-" + "'"
    )
    Words = str.lower(File.Load.Dictionary)
    while "  " in Words or "-" in Words:
        Words = Words.replace("  ", " ")
        Words = Words.replace("-", " ")
    for char in Words:
        if char not in allEnglishChar:
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

