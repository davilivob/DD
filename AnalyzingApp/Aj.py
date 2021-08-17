import json
import TimerLoadBar as TimeBar
def CreateRepeatedArray(Array):
    TwoDArray = []
    for element in Array:
        if [0, element] not in TwoDArray:
            TwoDArray.append([0, element])
    for index in range(len(TwoDArray)):
        TimeBar.Adding()
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
    return JsonArray


def splitQruotationMark(List, origin, a, b):
    while origin in List:
        List.append(a)
        List.append(b)
        List.remove(origin)

def SeparateAllShort(wordsList):
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
        splitQruotationMark(wordsList, "s", "1980s", "'")