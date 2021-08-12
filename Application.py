import string
import json

with open("daily_english.json", mode="r") as file:
    Dictionary = file.read()
    Words = Dictionary




allEnglishChar = list(string.ascii_lowercase + string.ascii_uppercase + ' ' + '-')

decimalDegree = 10

RankingList = 328


def fitSpace(string):
    return " "*(40-len(string))


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


def LoadBar(ratio, range):
    return '█'*int(range*ratio)+'_'*int(range-range*ratio)


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

    while '-' in Words:
        Words = Words.replace('-', ' ')

    wordsList = str.split(Words)

    while 's' in wordsList:
        wordsList.append('1980s')
        wordsList.remove('s')

    while 'hes' in wordsList:
        wordsList.append('is')
        wordsList.append('he')
        wordsList.remove('hes')

    while 'shes' in wordsList:
        wordsList.append('is')
        wordsList.append('she')
        wordsList.remove('shes')

    while 'theyre' in wordsList:
        wordsList.append('are')
        wordsList.append('they')
        wordsList.remove('theyre')

    while 'hed' in wordsList:
        wordsList.append('had')
        wordsList.append('he')
        wordsList.remove('hed')

    while 'shed' in wordsList:
        wordsList.append('had')
        wordsList.append('she')
        wordsList.remove('shed')

    while 'isnt' in wordsList:
        wordsList.append('is')
        wordsList.append('not')
        wordsList.remove('isnt')

    while 'dont' in wordsList:
        wordsList.append('do')
        wordsList.append('not')
        wordsList.remove('dont')

    while 'doesnt' in wordsList:
        wordsList.append('does')
        wordsList.append('not')
        wordsList.remove('doesnt')

    while 'cant' in wordsList:
        wordsList.append('can')
        wordsList.append('not')
        wordsList.remove('cant')

    while 'wouldnt' in wordsList:
        wordsList.append('would')
        wordsList.append('not')
        wordsList.remove('wouldnt')

    while 'couldnt' in wordsList:
        wordsList.append('could')
        wordsList.append('not')
        wordsList.remove('couldnt')


    WordsRepeated = []
    
    allEnglishChar.remove('-')

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
    RankRange = len(WordsRepeated)

    col = 3
    row = int(RankRange/col)+1
    num = 0
    record = 0
    remain = RankRange - (col-1)*row
    arr = []
    while len(arr) < RankRange:
        arr.append(num)
        num += row
        if record < remain:
            arr.append(num)
            num += row
            record += 1
            arr.append(num)
            num -= (row*2-1)
        else:
            arr.append(num)
            num -= (row-1)
    # arr.sort()
    for index in arr:
        if index < row:
            TopUsed += "\n      "
        Word = str(index+1) + '. "' + \
            WordsItself(WordsRepeated, index).capitalize() + '"'
        Amount = ": " + str(WordsAmount(WordsRepeated, index))+" "
        Percentage = Math.percent(WordsAmount(WordsRepeated, index), len(
            wordsList), 100)
        TopUsed += Word + Amount + Percentage
        TopUsed += fitSpace(Amount + Percentage + Word)


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
    Vocabularies = 'VOCABULARIES: ' + str(R.voc)
    Learned = 'Learned: ' + str(R.alr) + \
        Math.percent(R.alr, R.voc, decimalDegree)
    Unlearned = 'Unlearned: ' + \
        str(R.unl) + Math.percent(R.unl, R.voc, decimalDegree)
    Individuals = 'Individuals: ' + str(len(A.WordsRepeated))
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
    APLrate = "Allan Poe Index:    " + \
        str(APL.Grade)[2:-1] + "     " + \
        LoadBar(float(str(APL.Grade)[2:-3])/100, 60)
    APLresult = "Result:        " + APL.ShowLettersSort[:76]
    FLIrate = "First Letter Index: " + \
        str(F.Grade)[2:-1] + "     " + \
        LoadBar(float(str(F.Grade)[2:-3])/100, 60)
    FLIresult = "Result:        " + F.ShowLettersSort[:76]


Print.ln('')
Print.ln(Write.APLrate)
Print.tabln(
    "Stantard:      e, t, a, o, i, n, s, h, r, d, l, c, u, m, w, f, g, y, p, b, v, k, j, x, q, z")
Print.tabln(Write.APLresult)
Print.ln(Write.FLIrate)
Print.tabln(
    "Stantard:      t, a, s, h, w, i, o, b, m, f, c, l, d, p, n, e, g, r, y, u, v, j, k, q, x, z")
Print.tabln(Write.FLIresult)
Print.ln(Write.Vocabularies)
Print.tabln(Write.Learned + fitSpace(Write.Learned) + Write.Unlearned + fitSpace(Write.Unlearned) + Write.Individuals)
Print.ln(Write.Sentences)
Print.tabln(Write.Examples + fitSpace(Write.Examples) +
            Write.Definitions + fitSpace(Write.Definitions) + Write.Comparisons)
Print.ln("ADVANCED DATA: ")
Print.tabln(Write.TotalWords + fitSpace(Write.TotalWords) + Write.TotalCharacters +
            fitSpace(Write.TotalCharacters) + Write.LettersPerWord)
print("TOP "+str(A.RankRange)+" USED WORDS: ")
Print.tabln(A.TopUsed)


with open("Database.json", mode="w") as file:
    json.dump([{"Words List":A.wordsList},{"Words Repeat Time":A.WordsRepeated}], file)