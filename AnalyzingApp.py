import string
import json
import sys
import time
import math

efficiencyTest = 0
print()
RankingList = input("Please Enter The Number of Words Ranking You Want: ")

progress = 0
time_start = time.time()
print()
print()

with open("daily_english.json", mode="r") as file:
    Dictionary = file.read()
    Words = Dictionary


allEnglishChar = list(string.ascii_lowercase + string.ascii_uppercase + " " + "-" + "'")
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
    def ln(content):
        print(content, "\n")

    def tabln(content):
        print("     ", content + "\n")


class Math:
    def percent(element, object, degree):
        percentage = ((element) * 100) / object
        percentage = float(int(percentage * degree)) / degree
        return " ( " + str(percentage) + "% )"

    def takeDecimal(x, y, degree):
        return float(int(x / y * degree)) / degree


with open("Databases\Database.json", mode="r") as file:
    lastProgress = json.loads(file.read())
    prevProgress = lastProgress[4]["Last Progress"]
    lastAllan = lastProgress[3]["Project Statment"]["Allan Poe Index"]


class Loading:
    global Adding

    def Adding():
        global time_start
        global progress
        global prevProgress
        global lastAllan
        loadRatio = progress / prevProgress
        Progress = str(progress)
        time_counter = str(Math.takeDecimal(time.time() - time_start, 1, 10000))
        sys.stdout.write("\u001b[1A\u001b[1000D" + "( Completed Statement:")
        sys.stdout.write(
            " " * (len(Progress) + 1) + "\u001b[" + str(len(Progress)) + "D" + Progress
        )
        sys.stdout.write(" " * 9 + "\u001b[8D" + "in")
        sys.stdout.write(
            " " * (len(time_counter) + 1)
            + "\u001b["
            + str(len(time_counter))
            + "D"
            + time_counter
        )
        sys.stdout.write(" " * 8 + "\u001b[7D" + "seconds )")
        print()
        barRange = math.floor(lastAllan)
        sys.stdout.write(
            FontEffect("\u001b[1000D" + LoadBar(loadRatio, barRange, 0), 208, 0)
        )
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

    sentences = len(Dictionary.split("語")) - 1
    vocabularies = len(Dictionary.split("詞")) - 1
    definitions = len(Dictionary.split("定")) - 1
    comparisons = len(Dictionary.split("比")) - 1
    unlearned = len(Dictionary.split("空")) - 1

    learned = vocabularies - unlearned
    examples = sentences - definitions - comparisons


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
    while "-" in Words:
        Words = Words.replace("-", " ")
    wordsList = str.split(Words)

    while "s" in wordsList:
        wordsList.append("1980s")
        wordsList.remove("s")
        Adding()

    for x in [0]:
        splitQruotationMark(wordsList, "isn't", "is", "not")
        splitQruotationMark(wordsList, "weren't", "were", "not")
        splitQruotationMark(wordsList, "wasn't", "was", "not")
        splitQruotationMark(wordsList, "won't", "will", "not")
        splitQruotationMark(wordsList, "can't", "can", "not")
        splitQruotationMark(wordsList, "don't", "do", "not")
        splitQruotationMark(wordsList, "doesn't", "does", "not")
        splitQruotationMark(wordsList, "didn't", "did", "not")
        splitQruotationMark(wordsList, "hasn't", "has", "not")
        splitQruotationMark(wordsList, "haven't", "have", "not")
        splitQruotationMark(wordsList, "wouldn't", "would", "not")
        splitQruotationMark(wordsList, "souldn't", "sould", "not")
        splitQruotationMark(wordsList, "couldn't", "could", "not")
        splitQruotationMark(wordsList, "he's", "he", "is")
        splitQruotationMark(wordsList, "she's", "she", "is")
        splitQruotationMark(wordsList, "it's", "it", "is")
        splitQruotationMark(wordsList, "there's", "there", "is")
        splitQruotationMark(wordsList, "that's", "that", "is")
        splitQruotationMark(wordsList, "what's", "what", "is")
        splitQruotationMark(wordsList, "he's", "he", "is")
        splitQruotationMark(wordsList, "i'm", "i", "am")
        splitQruotationMark(wordsList, "you're", "you", "are")
        splitQruotationMark(wordsList, "they're", "they", "are")
        splitQruotationMark(wordsList, "we're", "we", "are")
        splitQruotationMark(wordsList, "he'd", "he", "had")
        splitQruotationMark(wordsList, "she'd", "she", "had")
        splitQruotationMark(wordsList, "they'd", "they", "had")
        splitQruotationMark(wordsList, "they've", "they", "have")
        splitQruotationMark(wordsList, "i've", "i", "have")
        splitQruotationMark(wordsList, "you've", "you", "have")
        splitQruotationMark(wordsList, "we've", "we", "have")
        splitQruotationMark(wordsList, "we'd", "we", "had")
        splitQruotationMark(wordsList, "it'd", "it", "had")
        splitQruotationMark(wordsList, "i'll", "i", "will")
        splitQruotationMark(wordsList, "he'll", "he", "will")
        splitQruotationMark(wordsList, "she'll", "she", "will")
        splitQruotationMark(wordsList, "we'll", "we", "will")
        splitQruotationMark(wordsList, "it'll", "it", "will")
        splitQruotationMark(wordsList, "kinda", "kind", "of")

        splitQruotationMark(wordsList, "st", "first", "'")
        splitQruotationMark(wordsList, "nd", "second", "'")
        splitQruotationMark(wordsList, "rd", "third", "'")
        splitQruotationMark(wordsList, "dr", "doctor", "'")

    while "'" in wordsList:
        wordsList.remove("'")

    possessive = 0

    for word in wordsList:
        if "'s" in word or "s'" in word:
            possessive += 1
            if "'s" in word:
                wordsList.append(word.replace("'s", ""))
                wordsList.remove(word)
                Adding()
            else:
                wordsList.append(word.replace("'", ""))
                wordsList.remove(word)
                Adding()

    for num in range(possessive):
        wordsList.append("'s")
        Adding()

    WordsRepeated = []

    allEnglishChar.remove("-")

    for word in wordsList:
        if [0, word] not in WordsRepeated:
            WordsRepeated.append([0, word])

    for index in range(0, len(WordsRepeated)):
        if index % 10 == 0:
            Adding()
        for word in wordsList:
            if word == WordsRepeated[index][1]:
                WordsRepeated[index][0] += 1

    WordsRepeated.sort(reverse=True)

    emptyJson = "{}"
    WordsRepeatedJson = json.loads(emptyJson)

    for word in WordsRepeated:
        WordsRepeatedJson.update({word[1]: word[0]})

    def WordsAmount(WordsRepeated, index):
        return WordsRepeated[index][0]

    def WordsItself(WordsRepeated, index):
        w = WordsRepeated
        return WordsRepeated[index][1]

    TopUsed = ""

    def checkNumber(string):
        allNumbers = []
        for num in range(10):
            allNumbers.append(str(num))
            Adding()
        result = 0
        if string != "all":
            for char in string:
                if char not in allNumbers:
                    result += 1
        if result == 0:
            return True
        elif result > 0:
            return False

    if RankingList == "" or checkNumber(RankingList) == False:
        RankRange = 0
        Adding()
    elif RankingList == "all" or int(RankingList) >= len(WordsRepeated):
        RankRange = len(WordsRepeated)
        Adding()
    elif checkNumber(RankingList) == True:
        RankRange = int(RankingList)
        Adding()

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


R = RegularData
A = AdvancedData


def IndexGrade(currentSortList, criticalSortList, SorG):
    Grade = 100
    ShowLetterSort = ""
    for index in range(len(currentSortList)):
        num = 0
        dist = abs(index - criticalSortList.index(currentSortList[index][1]))
        char = currentSortList[index][1]
        if dist > 0:
            ShowLetterSort += FontEffect(char, 210 - 2 * dist, 0) + ", "
            Adding()
        else:
            ShowLetterSort += FontEffect(char, 0, 1) + ", "
            Adding()
        num = 1 - (1 / 25 * dist)
        Grade *= num

    if SorG == 0:
        return Math.percent(Grade, 100, 100)
    else:
        return ShowLetterSort


class AllanPoeIndex:
    # Original goal is "eaoidhnrstuycfglmwbkpqxz"
    Letter = A.WordsRepeated
    letters = ""
    LettersRepeated = []
    LettersRepeated_copy = []

    for word in Letter:
        letters += word[1] * word[0]

    allLowerLetter = list(string.ascii_lowercase)

    for letter in allLowerLetter:
        LettersRepeated.append([0, letter])
        LettersRepeated_copy.append([0, letter])
        Adding()

    for element in LettersRepeated:
        for letter in letters:
            if letter == element[1]:
                element[0] += 1

    LettersRepeated.sort(reverse=True)
    CurrentSortList = LettersRepeated

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
    Grade = IndexGrade(CurrentSortList, CriticalSortList, 0)
    ShowLettersSort = IndexGrade(CurrentSortList, CriticalSortList, 1)


class BillMurrayIndex:

    Letter = A.WordsRepeated
    LettersRepeated = AllanPoeIndex.LettersRepeated_copy

    for element in LettersRepeated:
        for letter in Letter:
            if letter[1][0] == element[1]:
                element[0] += letter[0]

    LettersRepeated.sort(reverse=True)

    CurrentSortList = LettersRepeated

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
    Grade = IndexGrade(CurrentSortList, CriticalSortList, 0)
    ShowLettersSort = IndexGrade(CurrentSortList, CriticalSortList, 1)


class TypingTest:
    with open("Databases\TypingPracticeRecords.json", mode="r") as file:
        typingJson = file.read()
        TypingDatas = json.loads(typingJson)
    time = wpm = accuracy = backrate = totalchar = 0
    WrongWords = []
    for test in TypingDatas:
        time += test["TestLength"]
        accuracy += test["Accuracy"]
        backrate += test["BackRate"]
        totalchars += test["TotalChars"]
        for word in test["WrongWords"]:
            WrongWords.append(word)
        Adding()
    number = len(TypingDatas)
    avgTime = Math.takeDecimal(time, number, 10)
    avgWpm = Math.takeDecimal(wpm, number, 100)
    avgAccuracy = Math.takeDecimal(accuracy * 100, number, 10)
    avgBackrate = Math.takeDecimal(backrate * 100, number, 100)
    WrongWordsRepeated = []
    for word in WrongWords:
        if [0, word] not in WrongWordsRepeated:
            WrongWordsRepeated.append([0, word])
    for index in range(len(WrongWordsRepeated)):
        for word in WrongWords:
            if word == WrongWordsRepeated[index][1]:
                WrongWordsRepeated[index][0] += 1
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


Allan = AllanPoeIndex
Bill = BillMurrayIndex
Type = TypingTest

AllanJson = {
    "Allan Poe Index": float(Allan.Grade[3:-3]),
    "Bill Murray Index": float(Bill.Grade[3:-3]),
}


WordsKinds = len(A.WordsRepeated)
TotalWords = len(A.wordsList)
TotalChars = len(Allan.letters)
CharsPerWord = Math.takeDecimal(len(Allan.letters), len(A.wordsList), 100000)

analysisJson = {
    "Vocabularies": {
        "Total": R.vocabularies,
        "Learned": R.learned,
        "Unlearned": R.unlearned,
    },
    "Sentences": {
        "Total": R.sentences,
        "Examples": R.examples,
        "Definitions": R.definitions,
        "Comparisons": R.comparisons,
    },
    "Advanced Datas": {
        "Word's Kinds": WordsKinds,
        "Total Words": TotalWords,
        "Total Characters": TotalChars,
        "Letters Per Words": CharsPerWord,
    },
    "Typing Results": {
        "Test Duration": Type.avgTime,
        "WPM": Type.avgWpm,
        "Accuracy": Type.avgAccuracy / 100,
        "BackSpace Press Rate": Type.avgBackrate / 100,
        "Wrong Words List": Type.WrongWordsRepeatedJson,
        "Typo Rate": Type.TypoRateJson,
    },
}


with open("Databases\Database.json", mode="w") as file:
    json.dump(
        [
            {"Words List": A.wordsList},
            {"Words Repeat Time": A.WordsRepeatedJson},
            {"Analysing Results": analysisJson},
            {"Project Statment": AllanJson},
            {"Last Progress": progress},
        ],
        file,
    )


class Write:
    AllanRate = (
        FontEffect("Allan Poe Index:    ", 83, 1)
        + FontEffect(str(Allan.Grade)[2:-1], 0, 1)
        + "\n"
        + FontEffect(LoadBar(float(str(Allan.Grade)[2:-3]) / 100, 100, 0), 185, 0)
    )
    AllanResult = "Result:          " + Allan.ShowLettersSort[0:-2]

    BillRate = (
        FontEffect("Bill Murray Index:  ", 83, 1)
        + FontEffect(str(Bill.Grade)[2:-1], 0, 1)
        + "\n"
        + FontEffect(LoadBar(float(str(Bill.Grade)[2:-3]) / 100, 100, 0), 185, 0)
    )
    BillResult = "Result:          " + Bill.ShowLettersSort[0:-2]

    Vocabularies = FontEffect("Vocabularies: ", 160, 1) + str(R.vocabularies)

    Learned = (
        "Learned: "
        + str(R.learned)
        + Math.percent(R.learned, R.vocabularies, decimalDegree)
    )
    Unlearned = (
        "Unlearned: "
        + str(R.unlearned)
        + Math.percent(R.unlearned, R.vocabularies, decimalDegree)
    )
    Individuals = "Individuals: " + str(len(A.WordsRepeated))

    Sentences = FontEffect("Sentences:    ", 160, 1) + str(R.sentences)
    Examples = (
        "Examples: "
        + str(R.examples)
        + Math.percent(R.examples, R.sentences, decimalDegree)
    )
    Definitions = (
        "Definitions: "
        + str(R.definitions)
        + Math.percent(R.definitions, R.sentences, decimalDegree)
    )
    Comparisons = (
        "Comparisons: "
        + str(R.comparisons)
        + Math.percent(R.comparisons, R.sentences, decimalDegree)
    )

    TotalWords = "Total Words: " + str(len(A.wordsList))
    TotalCharacters = "Total Characters: " + str(len(Allan.letters))
    LettersPerWord = "Letters Per Word: " + str(
        Math.takeDecimal(len(Allan.letters), len(A.wordsList), 1000)
    )

    avgTime = "Test Duration: " + str(Type.avgTime) + " min"
    avgWpm = "WPM: " + str(Type.avgWpm)
    avgAccuracy = "Accuracy: " + str(Type.avgAccuracy) + " %"
    avgBackrate = "Back Rate: " + str(Type.avgBackrate) + " %"
    MostType = "Most Typo: " + '"' + Type.MostTypo + '"'


def AddingFiller():
    if progress < prevProgress:
        for x in range(prevProgress - progress):
            Adding()
    else:
        for x in range(2):
            Adding()


if efficiencyTest == False:
    AddingFiller()


print()

Print.ln("")
Print.ln(Write.AllanRate)
Print.tabln(
    FontEffect(
        "Stantard:        e, t, a, o, i, n, s, h, r, d, l, c, u, m, w, f, g, y, p, b, v, k, j, x, q, z",
        0,
        1,
    )
)
Print.tabln(Write.AllanResult)
Print.ln(Write.BillRate)
Print.tabln(
    FontEffect(
        "Stantard:        t, a, s, h, w, i, o, b, m, f, c, l, d, p, n, e, g, r, y, u, v, j, k, q, x, z",
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
Print.ln(FontEffect("Advanced Datas: ", 201, 1))
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
