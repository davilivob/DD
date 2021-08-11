import string

with open("daily_english.json", mode="r") as file:
    Dictionary = file.read()
    Words = Dictionary

allEnglishChar = list(string.ascii_lowercase + string.ascii_uppercase + ' ')

decimalDegree = 10

BigSpace = " "*24
SmallSpace = " "*15


def fitSpace(string):
    return " "*(32-len(string))


class Print:
    def ln(comtent):
        print(comtent, "\n")

    def tabln(comtent):
        print("     ", comtent+'\n')


class Math:
    def percent(element, object, degree):
        percentage = ((element)*100)/object
        percentage = float(int(percentage*degree))/degree
        return ' ( '+str(percentage)+'% )'

    def takeDecimal(x, y, degree):
        return float(int(x/y*degree))/degree


class RegularData:
    voc = sen = defi = com = unl = 0

    # words
    Dictionary = Dictionary.replace('": [', '詞')

    sentenceEnd = ['."', '!"', '?"', '\\\""']
    for element in sentenceEnd:
        Dictionary = Dictionary.replace(element, '語')

    Dictionary = Dictionary.replace(
        '"@', '定').replace('"&', '比').replace('""', '空')

    for char in Dictionary:
        if char == '詞':
            voc += 1
        if char == '語':
            sen += 1
        if char == '定':
            defi += 1
        if char == '比':
            com += 1
        if char == '空':
            unl += 1

    alr = voc-int(unl/2)
    unl = int(unl/2)
    exp = sen-defi-com


class AdvancedData:
    Words = str.lower(Words)

    for char in Words:
        if char not in allEnglishChar:
            Words = Words.replace(char, '')

    while '  ' in Words:
        Words = Words.replace('  ', ' ')

    wordsList = str.split(Words)

    while 's' in wordsList:
        wordsList.remove('s')

    WordsRepeated = []

    for word in wordsList:
        if [0, word] not in WordsRepeated:
            WordsRepeated.append([0, word])

    for index in range(0, len(WordsRepeated)):
        for word in wordsList:
            if word == WordsRepeated[index][1]:
                WordsRepeated[index][0] += 1

    WordsRepeated.sort(reverse=True)

    def WordsAmount(WordsRepeated, index):
        return WordsRepeated[index][0]

    def WordsItself(WordsRepeated, index):
        w = WordsRepeated
        return WordsRepeated[index][1]

    TopUsed = ""
    RankRange = 100

    for index in range(0, RankRange):
        Word = '"' + WordsItself(WordsRepeated, index)+'"'
        Amount = ": " + str(WordsAmount(WordsRepeated, index))+" "
        Percentage = Math.percent(WordsAmount(WordsRepeated, index), len(
            wordsList), decimalDegree)
        TopUsed += Word + Amount + Percentage
        TopUsed += fitSpace(Amount + Percentage + Word)
        if (index) % 5 == 4 and index <= RankRange-3:
            TopUsed += "\n\n      "


R = RegularData
A = AdvancedData


class AllanPoeIndex:
    # Original goal is "eaoidhnrstuycfglmwbkpqxz"
    Letter = A.WordsRepeated
    letters = ''
    LettersRepeated = []

    for word in Letter:
        letters += word[1]*word[0]
    letters += 's'*2
    allLowerLetter = list(string.ascii_lowercase)

    for letter in allLowerLetter:
        LettersRepeated.append([0, letter])

    for element in LettersRepeated:
        for letter in letters:
            if letter == element[1]:
                element[0] += 1

    LettersRepeated.sort(reverse=True)
    ShowLettersSort = ''
    for letter in LettersRepeated:
        ShowLettersSort += letter[1] + ", "

    CurrentSortList = ShowLettersSort.split(', ')
    CurrentSortList.remove('')

    CriticalSortList = ['e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l',
                        'c', 'u', 'm', 'w', 'f', 'g', 'y', 'p', 'b', 'v', 'k', 'j', 'x', 'q', 'z']
    Grade = 100
    for char in CurrentSortList:
        num = 0
        dist = abs(CurrentSortList.index(char) - CriticalSortList.index(char))
        num = 1-(1/25*dist)
        Grade *= num
    Grade = Math.percent(Grade, 100, 100)


class FirstLetterIndex:
    FirstLetter = "t, a, s, h, w, i, o, b, m, f, c, l, d, p, n, e, g, r, y, u, v, j, k, q, x, z".split(
        ", ")

    Letter = A.WordsRepeated
    LettersRepeated = []

    allLowerLetter = list(string.ascii_lowercase)
    for letter in allLowerLetter:
        LettersRepeated.append([0, letter])

    for element in LettersRepeated:
        for letter in Letter:
            if letter[1][0] == element[1]:
                element[0] += letter[0]

    LettersRepeated.sort(reverse=True)

    ShowLettersSort = ''
    for letter in LettersRepeated:
        ShowLettersSort += letter[1] + ", "
    # ShowLettersSort = ShowLettersSort.replace(ShowLettersSort[-2:0], '')

    CurrentSortList = ShowLettersSort.split(', ')
    CurrentSortList.remove('')
    CriticalSortList = ['t', 'a', 's', 'h', 'w', 'i', 'o', 'b', 'm', 'f', 'c',
                        'l', 'd', 'p', 'n', 'e', 'g', 'r', 'y', 'u', 'v', 'j', 'k', 'q', 'x', 'z']
    Grade = 100
    for char in CurrentSortList:
        num = 0
        dist = abs(CurrentSortList.index(char) - CriticalSortList.index(char))
        num = 1-(1/25*dist)
        Grade *= num
    Grade = Math.percent(Grade, 100, 100)


APL = AllanPoeIndex
F = FirstLetterIndex


class Write:
    Vocbularies = 'VOCABULARIES: ' + str(R.voc)
    Learned = 'Learned: ' + str(R.alr) + \
        Math.percent(R.alr, R.voc, decimalDegree)
    Unlearned = 'Unlearned: ' + \
        str(R.unl) + Math.percent(R.unl, R.voc, decimalDegree)
    Sentences = 'SENTENCES: ' + str(R.sen)
    Examples = 'Examples: ' + \
        str(R.exp) + Math.percent(R.exp, R.sen, decimalDegree)
    Definitions = 'Definitions: ' + \
        str(R.defi) + Math.percent(R.defi, R.sen, decimalDegree)
    Comparisons = 'Comparisons: ' + \
        str(R.com) + Math.percent(R.com, R.sen, decimalDegree)
    TotalWords = "Total Words: " + str(len(A.wordsList))
    TotalCharacters = "Total Characters: " + str(len(APL.letters))
    LettersPerWord = "Letters Per Word: " + str(Math.takeDecimal(
        len(APL.letters), len(A.wordsList), 1000))
    APLrate = "Allan Poe Index:    " + str(APL.Grade)[2:-1]
    APLresult = "Result:     " + APL.ShowLettersSort[:76]
    FLIrate = "First Letter Index: " + str(F.Grade)[2:-1]
    FLIresult = "Result:     " + F.ShowLettersSort[:76]


Print.ln('')
Print.ln(Write.APLrate)
Print.tabln(
    "Stantard:   e, t, a, o, i, n, s, h, r, d, l, c, u, m, w, f, g, y, p, b, v, k, j, x, q, z")
Print.tabln(Write.APLresult)
Print.ln(Write.FLIrate)
Print.tabln(
    "Stantard:   t, a, s, h, w, i, o, b, m, f, c, l, d, p, n, e, g, r, y, u, v, j, k, q, x, z")
Print.tabln(Write.FLIresult)
Print.ln(Write.Vocbularies)
Print.tabln(Write.Learned + fitSpace(Write.Learned) + Write.Unlearned)
Print.ln(Write.Sentences)
Print.tabln(Write.Examples + fitSpace(Write.Examples) +
            Write.Definitions + fitSpace(Write.Definitions) + Write.Comparisons)
Print.ln("ADVANCED DATA: ")
Print.tabln(Write.TotalWords + fitSpace(Write.TotalWords) + Write.TotalCharacters +
            fitSpace(Write.TotalCharacters) + Write.LettersPerWord)
Print.ln("TOP "+str(A.RankRange)+" USED WORDS: ")
Print.tabln(A.TopUsed)

# print(str(F.LettersRepeated))
# print(str(F.FirstLetter))
# print(str(F.ShowLettersSort))
# print(str(F.CurrentSortList))
