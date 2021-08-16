import string
import json
import sys
import time
import math

time_start = time.time()
efficiencyTest = False
RankingList = input("Please Enter The Number of Words Ranking You Want: ")
progress = 0
print()
print()
print()

with open("daily_english.json", mode="r") as file:
    Dictionary = file.read()
    Words = Dictionary

allEnglishChar = list(string.ascii_lowercase + string.ascii_uppercase + " " + "-" + "'")


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


def CreateRepeatedArray(Array):
    TwoDArray = []
    for element in Array:
        if [0, element] not in TwoDArray:
            TwoDArray.append([0, element])
    for index in range(len(TwoDArray)):
        Adding(index, 40)
        for element in Array:
            if element == TwoDArray[index][1]:
                TwoDArray[index][0] += 1
    TwoDArray.sort(reverse=True)
    return TwoDArray


def CreateJsonObject(twoDArray):
    emptyJson = "{}"
    JsonArray = json.loads(emptyJson)
    for element in twoDArray:
        JsonArray.update({element[1]: element[0]})
        Adding(1, 1)
    return JsonArray


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


def splitQruotationMark(List, origin, a, b):
    while origin in List:
        List.append(a)
        List.append(b)
        List.remove(origin)
        Adding(1, 1)


with open("Databases\Database.json", mode="r") as file:
    lastProgress = json.loads(file.read())
    prevProgress = lastProgress[4]["Last Progress"]
    lastAllan = lastProgress[3]["Project Statment"]["Allan Poe Index"]


def Adding(parameter, speed):
    if parameter % speed == 0:
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
        Adding(1, 1)

    sentences = len(Dictionary.split("語")) - 1
    vocabularies = len(Dictionary.split("詞")) - 1
    definitions = len(Dictionary.split("定")) - 1
    comparisons = len(Dictionary.split("比")) - 1
    unlearned = len(Dictionary.split("空")) - 1

    learned = vocabularies - unlearned
    examples = sentences - definitions - comparisons


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
        Adding(1, 1)

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
                Adding(1, 1)
            else:
                wordsList.append(word.replace("'", ""))
                wordsList.remove(word)
                Adding(1, 1)

    for num in range(possessive):
        wordsList.append("'s")
        Adding(1, 1)

    WordsRepeated = CreateRepeatedArray(wordsList)

    allEnglishChar.remove("-")

    WordsRepeatedJson = CreateJsonObject(WordsRepeated)

    TopUsed = ""

    def checkNumber(string):
        allNumbers = []
        for num in range(10):
            allNumbers.append(str(num))
            Adding(1, 1)
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
        Adding(1, 1)
    elif RankingList == "all" or int(RankingList) >= len(WordsRepeated):
        RankRange = len(WordsRepeated)
        Adding(1, 1)
    elif checkNumber(RankingList) == True:
        RankRange = int(RankingList)
        Adding(1, 1)

    col = 3
    row = int(RankRange / col) + 1
    num = record = 0
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
        Word = str(index + 1) + '. "' + WordsRepeated[index][1].capitalize() + '"'
        Amount = ": " + str(WordsRepeated[index][0]) + " "
        Percentage = Math.percent(WordsRepeated[index][0], len(wordsList), 100)
        TopUsed += FormalFiller(Word + Amount + Percentage, 3)
        Adding(index, 20)


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
            Adding(1, 1)
        else:
            ShowLetterSort += FontEffect(char, 0, 1) + ", "
            Adding(1, 1)
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

    allLowerLetters = list(string.ascii_lowercase)

    LettersRepeated = CreateRepeatedArray(allLowerLetters)
    LettersRepeated_copy = CreateRepeatedArray(allLowerLetters)

    for element in LettersRepeated:
        Adding(1, 1)
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
    LettersRepeatedJson = CreateJsonObject(LettersRepeated)


class BillMurrayIndex:

    Letter = A.WordsRepeated
    LettersRepeated = AllanPoeIndex.LettersRepeated_copy

    for element in LettersRepeated:
        Adding(1, 1)
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
    global lastProgress
    with open("Databases\TypingPracticeRecords.json", mode="r") as file:
        typingJson = file.read()
        TypingDatas = json.loads(typingJson)
    totaltime = wpm = accuracy = totalback = totalchars = goodchars = 0
    WrongWords = []
    WrongChars = []
    for test in TypingDatas:
        totaltime += test["TestLength"]
        totalback += test["TotalBack"]
        totalchars += test["TotalChars"]
        goodchars += test["GoodChars"]
        for word in test["WrongWords"]:
            WrongWords.append(word)
        Adding(1, 1)
        for char in test["WrongChars"]:
            WrongChars.append(char)
        Adding(1, 1)
    avgTime = totaltime / len(TypingDatas)
    avgWpm = totalchars / (5 * totaltime)
    avgCpm = totalchars / totaltime
    avgAccuracy = goodchars / totalchars
    avgBackrate = totalback / totalchars

    avgTimePrint = Math.takeDecimal(totaltime, len(TypingDatas), 10)
    avgWpmPrint = Math.takeDecimal(totalchars / 5, totaltime, 100)
    avgCpmPrint = Math.takeDecimal(totalchars, totaltime, 100)
    avgAccuracyPrint = Math.takeDecimal(goodchars * 100, totalchars, 100)
    avgBackratePrint = Math.takeDecimal(totalback * 100, totalchars, 100)

    WrongWordsRepeated = CreateRepeatedArray(WrongWords)
    WrongCharsRepeated = CreateRepeatedArray(WrongChars)
    WrongWordsRepeatedJson = CreateJsonObject(WrongWordsRepeated)
    WrongCharsRepeatedJson = CreateJsonObject(WrongCharsRepeated)

    TypoRate = WrongCharsRepeated
    for char in TypoRate:
        if str(char[1]) != "Symbols" and str(char[1]) != "Spaces":
            char[0] = (
                float(char[0])
                / lastProgress[2]["Analysing Results"]["Advanced Datas"][
                    "Characters Repeated Times"
                ][str(char[1])]
            )
        if str(char[1]) == "Spaces":
            char[0] = float(char[0]) / ((len(A.wordsList) - R.learned * 2))
        Adding(1, 1)

    TypoRate.sort(reverse=True)
    MostTypo = TypoRate[1][1]

    TypoRateJson = CreateJsonObject(TypoRate)


Allan = AllanPoeIndex
Bill = BillMurrayIndex
Type = TypingTest


class AnalysedData:
    WordsKinds = len(A.WordsRepeated)
    TotalWords = len(A.wordsList)
    TotalChars = len(Allan.letters)
    CharsPerWord = Math.takeDecimal(len(Allan.letters), len(A.wordsList), 100000)
    AllanJson = {
        "Allan Poe Index": float(Allan.Grade[3:-3]),
        "Bill Murray Index": float(Bill.Grade[3:-3]),
    }
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
            "Characters Repeated Times": AllanPoeIndex.LettersRepeatedJson,
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
            {"Words List": A.wordsList},
            {"Words Repeat Time": A.WordsRepeatedJson},
            {"Analysing Results": AnalysedData.analysisJson},
            {"Project Statment": AnalysedData.AllanJson},
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

    Learned = "Learned: " + str(R.learned) + Math.percent(R.learned, R.vocabularies, 10)
    Unlearned = (
        "Unlearned: " + str(R.unlearned) + Math.percent(R.unlearned, R.vocabularies, 10)
    )
    Individuals = "Individuals: " + str(len(A.WordsRepeated))

    Sentences = FontEffect("Sentences:    ", 160, 1) + str(R.sentences)
    Examples = (
        "Examples: " + str(R.examples) + Math.percent(R.examples, R.sentences, 10)
    )
    Definitions = (
        "Definitions: "
        + str(R.definitions)
        + Math.percent(R.definitions, R.sentences, 10)
    )
    Comparisons = (
        "Comparisons: "
        + str(R.comparisons)
        + Math.percent(R.comparisons, R.sentences, 10)
    )

    TotalWords = "Total Words: " + str(len(A.wordsList))
    TotalCharacters = "Total Characters: " + str(len(Allan.letters))
    LettersPerWord = "Letters Per Word: " + str(
        Math.takeDecimal(len(Allan.letters), len(A.wordsList), 1000)
    )

    avgTime = "Test Duration: " + str(Type.avgTimePrint) + " mins"
    avgWpm = "WPM: " + str(Type.avgWpmPrint)
    avgAccuracy = "Accuracy: " + str(Type.avgAccuracyPrint) + " %"
    avgBackrate = "Back Rate: " + str(Type.avgBackratePrint) + " %"
    MostType = "Most Typo: " + '"' + Type.MostTypo + '"'


def AddingFiller():
    while progress < prevProgress:
        Adding(1, 1)
    else:
        for x in range(2):
            Adding(1, 1)


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
