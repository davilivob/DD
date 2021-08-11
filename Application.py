import string
with open("daily_english.json", mode="r") as file:
    Dictionary = file.read()
    Words = Dictionary
allEnglishChar = list(string.ascii_lowercase + string.ascii_uppercase + ' ')

decimalDegree = 10


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
    RankRange = 50
    for index in range(0, RankRange):
        TopUsed += '"' + WordsItself(WordsRepeated, index)+'"'
        TopUsed += ": " + str(WordsAmount(WordsRepeated, index))+" " + \
            Math.percent(WordsAmount(WordsRepeated, index), len(
                wordsList), decimalDegree) + ","
        TopUsed += " "*(30-len(": " + str(WordsAmount(WordsRepeated, index))+" " +
                                                     Math.percent(WordsAmount(WordsRepeated, index), len(
                                                         wordsList), decimalDegree) + ","+'"' + WordsItself(WordsRepeated, index)+'"'))
        if index % 5 == 4:
            TopUsed += "\n\n      "


R = RegularData
A = AdvancedData
Print.ln('')
Print.ln('VOCABULARIES: ' + str(R.voc))
Print.tabln('Learned: ' + str(R.alr) +
            Math.percent(R.alr, R.voc, decimalDegree))
Print.tabln('Unlearned: ' + str(R.unl) +
            Math.percent(R.unl, R.voc, decimalDegree))
Print.ln('SENTENCES: ' + str(R.sen))
Print.tabln('Examples: ' + str(R.exp) +
            Math.percent(R.exp, R.sen, decimalDegree))
Print.tabln('Definitions: ' + str(R.defi) +
            Math.percent(R.defi, R.sen, decimalDegree))
Print.tabln('Comparisons: ' + str(R.com) +
            Math.percent(R.com, R.sen, decimalDegree))
Print.ln("ADVANCED DATA: ")
Print.tabln("Total words: " + str(len(A.wordsList)))
Print.tabln("Top "+str(A.RankRange)+" used words: ")
Print.tabln(A.TopUsed)

# Print.ln(str(A.WordsRepeated))
