import string
import json
import sys
import time

print()
RankingList = input("Please Enter The Number of Words Ranking You Want: ")

progress = 0
time_start = time.time()
print()
print()

with open("daily_english.json", mode="r") as file:
    Dictionary = file.read()
    Words = Dictionary

allEnglishChar = list(string.ascii_lowercase + string.ascii_uppercase + " " + "-")
decimalDegree = 10


def colors(color, bold):
    effect = ""
    if color != 0:
        effect += "\u001b[38;5;" + str(color) + "m"
    else:
        effect += ""

    if bold == 1:
        effect += "\u001b[1m"
    else:
        effect += ""
    return effect


def FontEffect(string, color, bold):
    return colors(color, bold) + string + colors("\u001b[0", 0)


def FormalFiller(string, col):
    return string + " " * (int(120 / col) - len(string))


class Print:
    def ln(comtent):
        print(comtent, "\n")

    def tabln(comtent):
        print("     ", comtent + "\n")


class Math:
    def percent(element, object, degree):
        percentage = ((element) * 100) / object
        percentage = float(int(percentage * degree)) / degree
        return " ( " + str(percentage) + "% )"

    def takeDecimal(x, y, degree):
        return float(int(x / y * degree)) / degree


with open("database.json", mode="r") as file:
    lastProgress = json.loads(file.read())
    prevProgress = lastProgress[3]["Last Progress"]


class Loading:
    global Adding

    def Adding():
        global time_start
        global progress
        global prevProgress
        loadRatio = progress / prevProgress
        Progress = str(progress)
        time_counter = str(Math.takeDecimal(time.time() - time_start, 1, 10000))
        sys.stdout.write("\u001b[1A\u001b[1000D" + "( Calcualated")
        sys.stdout.write(
            " " * (len(Progress) + 1) + "\u001b[" + str(len(Progress)) + "D" + Progress
        )
        sys.stdout.write(" " * 9 + "\u001b[8D" + "times in")
        sys.stdout.write(
            " " * (len(time_counter) + 1)
            + "\u001b["
            + str(len(time_counter))
            + "D"
            + time_counter
        )
        sys.stdout.write(" " * 8 + "\u001b[7D" + "seconds )")
        print()
        sys.stdout.write(FontEffect("\u001b[1000D" + LoadBar(loadRatio, 46, 0), 208, 0))
        sys.stdout.flush()
        progress += 1


def LoadBar(ratio, range, height):
    filler = ""
    if height == 1:
        filler = "█"
    if height == 0:
        filler = "▄"
    if ratio <= 1:
        return filler * int(range * ratio) + "_" * int(range - range * ratio)
    else:
        return filler * range


class RegularData:

    sentenceEnd = ['."', '!"', '?"', '\\""']
    Dictionary = Dictionary.replace('": [', "詞").replace('"@', "定").replace('"&', "比")
    Dictionary = Dictionary.replace('""', "空")
    for element in sentenceEnd:
        Dictionary = Dictionary.replace(element, "語")
        Adding()

    sen = len(Dictionary.split("語")) - 1
    voc = len(Dictionary.split("詞")) - 1
    defi = len(Dictionary.split("定")) - 1
    com = len(Dictionary.split("比")) - 1
    unl = len(Dictionary.split("空")) - 1

    alr = voc - int(unl / 2)
    unl = int(unl / 2)
    exp = sen - defi - com


def splitQruotationMark(List, origin, a, b):
    while origin in List:
        List.append(a)
        List.append(b)
        List.remove(origin)
        Adding()


class AdvancedData:

    global progress
    Words = str.lower(Words)
    for char in Words:
        if char not in allEnglishChar:
            Words = Words.replace(char, "")
            while "  " in Words:
                Words = Words.replace("  ", " ")
                Adding()
            while "-" in Words:
                Words = Words.replace("-", " ")
                Adding()

    wordsList = str.split(Words)

    while "s" in wordsList:
        wordsList.append("1980s")
        wordsList.remove("s")
        Adding()

    for x in [0]:
        splitQruotationMark(wordsList, "hes", "he", "is")
        splitQruotationMark(wordsList, "shes", "she", "is")
        splitQruotationMark(wordsList, "youre", "you", "are")
        splitQruotationMark(wordsList, "hes", "he", "is")
        splitQruotationMark(wordsList, "im", "i", "am")
        splitQruotationMark(wordsList, "theyre", "they", "are")
        splitQruotationMark(wordsList, "hed", "he", "had")
        splitQruotationMark(wordsList, "shed", "she", "had")
        splitQruotationMark(wordsList, "itd", "it", "had")
        splitQruotationMark(wordsList, "isnt", "is", "not")
        splitQruotationMark(wordsList, "cant", "can", "not")
        splitQruotationMark(wordsList, "dont", "do", "not")
        splitQruotationMark(wordsList, "doesnt", "does", "not")
        splitQruotationMark(wordsList, "didnt", "did", "not")
        splitQruotationMark(wordsList, "wouldnt", "would", "not")
        splitQruotationMark(wordsList, "souldnt", "sould", "not")
        splitQruotationMark(wordsList, "couldnt", "could", "not")

    WordsRepeated = []

    allEnglishChar.remove("-")

    for word in wordsList:
        if [0, word] not in WordsRepeated:
            WordsRepeated.append([0, word])
        Adding()

    for index in range(0, len(WordsRepeated)):
        for word in wordsList:
            if word == WordsRepeated[index][1]:
                WordsRepeated[index][0] += 1
        Adding()

    WordsRepeated.sort(reverse=True)

    emptyJson = "{}"
    WordsRepeatedJson = json.loads(emptyJson)

    for word in WordsRepeated:
        WordsRepeatedJson.update({word[1]: word[0]})
        Adding()

    def WordsAmount(WordsRepeated, index):
        return WordsRepeated[index][0]

    def WordsItself(WordsRepeated, index):
        w = WordsRepeated
        return WordsRepeated[index][1]

    TopUsed = ""
    if RankingList == "all" or int(RankingList) >= len(WordsRepeated):
        RankRange = len(WordsRepeated)
    else:
        RankRange = int(RankingList)

    col = 3
    row = int(RankRange / col) + 1
    num = 0
    record = 0
    remain = RankRange - (col - 1) * row
    arr = []
    while len(arr) < RankRange:
        arr.append(num)
        num += row
        if record < remain:
            arr.append(num)
            num += row
            record += 1
            arr.append(num)
            num -= row * 2 - 1
        else:
            arr.append(num)
            num -= row - 1
        Adding()
    # arr.sort()
    for index in arr:
        if index < row:
            TopUsed += "\n      "
        Word = (
            str(index + 1)
            + '. "'
            + WordsItself(WordsRepeated, index).capitalize()
            + '"'
        )
        Amount = ": " + str(WordsAmount(WordsRepeated, index)) + " "
        Percentage = Math.percent(
            WordsAmount(WordsRepeated, index), len(wordsList), 100
        )
        TopUsed += FormalFiller(Word + Amount + Percentage, 3)
        Adding()


R = RegularData
A = AdvancedData


def IndexGrade(currentSortList, criticalSortList):
    Grade = 100
    for char in currentSortList:
        num = 0
        dist = abs(currentSortList.index(char) - criticalSortList.index(char))
        num = 1 - (1 / 25 * dist)
        Grade *= num
        Adding()
    return Math.percent(Grade, 100, 100)


class AllanPoeIndex:
    # Original goal is "eaoidhnrstuycfglmwbkpqxz"
    Letter = A.WordsRepeated
    letters = ""
    LettersRepeated = []

    for word in Letter:
        letters += word[1] * word[0]
        Adding()

    letters += "s" * 2
    allLowerLetter = list(string.ascii_lowercase)

    for letter in allLowerLetter:
        LettersRepeated.append([0, letter])
        Adding()

    for element in LettersRepeated:
        for letter in letters:
            if letter == element[1]:
                element[0] += 1
        Adding()

    LettersRepeated.sort(reverse=True)
    ShowLettersSort = ""
    for letter in LettersRepeated:
        ShowLettersSort += letter[1] + ", "
        Adding()

    CurrentSortList = ShowLettersSort.split(", ")
    CurrentSortList.remove("")

    CriticalSortList = [
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
    Grade = IndexGrade(CurrentSortList, CriticalSortList)


class BillMurrayIndex:

    Letter = A.WordsRepeated
    LettersRepeated = []

    allLowerLetter = list(string.ascii_lowercase)
    for letter in allLowerLetter:
        LettersRepeated.append([0, letter])
        Adding()

    for element in LettersRepeated:
        for letter in Letter:
            if letter[1][0] == element[1]:
                element[0] += letter[0]
        Adding()

    LettersRepeated.sort(reverse=True)

    ShowLettersSort = ""
    for letter in LettersRepeated:
        ShowLettersSort += letter[1] + ", "
        Adding()
    # ShowLettersSort = ShowLettersSort.replace(ShowLettersSort[-2:0], '')

    CurrentSortList = ShowLettersSort.split(", ")
    CurrentSortList.remove("")
    CriticalSortList = [
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
    Grade = IndexGrade(CurrentSortList, CriticalSortList)


class TypingTest:
    with open("TypingPracticeRecords.json", mode="r") as file:
        typingJson = file.read()
        TypingDatas = json.loads(typingJson)
    time = wpm = accuracy = backrate = number = 0
    WrongWords = []
    for test in TypingDatas:
        time += test["TestLength"]
        wpm += test["WPM"]
        accuracy += test["Accuracy"]
        backrate = test["BackRate"]
        for word in test["WrongWords"]:
            WrongWords.append(word)
        Adding()
        number += 1

    avgTime = Math.takeDecimal(time, number, 10)
    avgWpm = Math.takeDecimal(wpm, number, 100)
    avgAccuracy = Math.takeDecimal(accuracy * 100, number, 10)
    avgBackrate = Math.takeDecimal(backrate * 100, number, 10)
    WrongWordsRepeated = []
    for word in WrongWords:
        if [0, word] not in WrongWordsRepeated:
            WrongWordsRepeated.append([0, word])
        Adding()
    for index in range(len(WrongWordsRepeated)):
        for word in WrongWords:
            if word == WrongWordsRepeated[index][1]:
                WrongWordsRepeated[index][0] += 1
            Adding()
    WrongWordsRepeated.sort(reverse=True)

    emptyJson = "{}"
    WrongWordsRepeatedJson = json.loads(emptyJson)
    for word in WrongWordsRepeated:
        WrongWordsRepeatedJson.update({word[1]: word[0]})
        Adding()

    TypoRate = WrongWordsRepeated
    for word in TypoRate:
        word[0] = float(word[0] / lastProgress[1]["Words Repeat Time"][word[1]])
        Adding()

    TypoRate.sort(reverse=True)
    MostTypo = TypoRate[0][1]

    TypoRateJson = json.loads(emptyJson)
    for word in TypoRate:
        TypoRateJson.update({word[1]: word[0]})
        Adding()

    jsonUpload = [
        {
            "Test Duration": avgTime,
            "WPM": avgWpm,
            "Accuracy": avgAccuracy / 100,
            "BackSpace Press Rate": avgBackrate,
            "Wrong Words List": WrongWordsRepeatedJson,
            "Typo Rate": TypoRateJson,
        }
    ]

    for x in range(5):
        Adding()


Allan = AllanPoeIndex
Bill = BillMurrayIndex
T = TypingTest

print()


class Write:
    AllanRate = (
        FontEffect("Allan Poe Index:    ", 83, 1)
        + FontEffect(str(Allan.Grade)[2:-1], 0, 1)
        + "     "
        + LoadBar(float(str(Allan.Grade)[2:-3]) / 100, 60, 1)
    )
    AllanResult = "Result:        " + Allan.ShowLettersSort[:76]

    BillRate = (
        FontEffect("Bill Murray Index:  ", 83, 1)
        + FontEffect(str(Bill.Grade)[2:-1], 0, 1)
        + "     "
        + LoadBar(float(str(Bill.Grade)[2:-3]) / 100, 60, 1)
    )
    BillResult = "Result:        " + Bill.ShowLettersSort[:76]

    Vocabularies = FontEffect("VOCABULARIES: ", 160, 1) + str(R.voc)

    Learned = "Learned: " + str(R.alr) + Math.percent(R.alr, R.voc, decimalDegree)
    Unlearned = "Unlearned: " + str(R.unl) + Math.percent(R.unl, R.voc, decimalDegree)
    Individuals = "Individuals: " + str(len(A.WordsRepeated))

    Sentences = FontEffect("SENTENCES: ", 160, 1) + str(R.sen)
    Examples = "Examples: " + str(R.exp) + Math.percent(R.exp, R.sen, decimalDegree)
    Definitions = (
        "Definitions: " + str(R.defi) + Math.percent(R.defi, R.sen, decimalDegree)
    )
    Comparisons = (
        "Comparisons: " + str(R.com) + Math.percent(R.com, R.sen, decimalDegree)
    )

    TotalWords = "Total Words: " + str(len(A.wordsList))
    TotalCharacters = "Total Characters: " + str(len(Allan.letters))
    LettersPerWord = "Letters Per Word: " + str(
        Math.takeDecimal(len(Allan.letters), len(A.wordsList), 1000)
    )

    avgTime = "Test Duration: " + str(T.avgTime) + " min"
    avgWpm = "WPM: " + str(T.avgWpm)
    avgAccuracy = "Accuracy: " + str(T.avgAccuracy) + " %"
    avgBackrate = "Back Rate: " + str(T.avgBackrate) + " %"
    MostType = "Most Typo: " + '"' + T.MostTypo + '"'


Print.ln("")
Print.ln(Write.AllanRate)
Print.tabln(
    FontEffect(
        "Stantard:      e, t, a, o, i, n, s, h, r, d, l, c, u, m, w, f, g, y, p, b, v, k, j, x, q, z",
        0,
        1,
    )
)
Print.tabln(Write.AllanResult)
Print.ln(Write.BillRate)
Print.tabln(
    FontEffect(
        "Stantard:      t, a, s, h, w, i, o, b, m, f, c, l, d, p, n, e, g, r, y, u, v, j, k, q, x, z",
        0,
        1,
    )
)
Print.tabln(Write.BillResult)
Print.ln(Write.Vocabularies)
Print.tabln(
    FormalFiller(Write.Learned, 3)
    + FormalFiller(Write.Unlearned, 3)
    + Write.Individuals
)
Print.ln(Write.Sentences)
Print.tabln(
    FormalFiller(Write.Examples, 3)
    + FormalFiller(Write.Definitions, 3)
    + Write.Comparisons
)
Print.ln(FontEffect("ADVANCED DATA: ", 201, 1))
Print.tabln(
    FormalFiller(Write.TotalWords, 3)
    + FormalFiller(Write.TotalCharacters, 3)
    + Write.LettersPerWord
)
Print.ln(FontEffect("Typing Test Results: ", 165, 1))
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
Print.tabln(
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
print(FontEffect("TOP " + str(A.RankRange) + " USED WORDS: ", 208, 1))
Print.tabln(A.TopUsed)


with open("Database.json", mode="w") as file:
    json.dump(
        [
            {"Words List": A.wordsList},
            {"Words Repeat Time": A.WordsRepeatedJson},
            {"Typing Test Results": T.jsonUpload},
            {"Last Progress": progress},
        ],
        file,
    )
