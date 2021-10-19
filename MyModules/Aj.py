import sys
from os.path import dirname, abspath

d = dirname(dirname(abspath(__file__)))
sys.path.append(d)
import MyModules.TimerLoadBar as TimeBar
import json
def CreateRepeatedArray(Array):
    TwoDArray = []
    for element in Array:
        TimeBar.Adding()
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
        splitQruotationMark(wordsList, "s", "1980s", "'")
        splitQruotationMark(wordsList, "isn't", "is", "not")
        splitQruotationMark(wordsList, "aren't", "are", "not")
        splitQruotationMark(wordsList, "weren't", "were", "not")
        splitQruotationMark(wordsList, "wasn't", "was", "not")
        splitQruotationMark(wordsList, "won't", "will", "not")
        splitQruotationMark(wordsList, "can't", "can", "not")
        splitQruotationMark(wordsList, "cannot", "can", "not")
        splitQruotationMark(wordsList, "don't", "do", "not")
        splitQruotationMark(wordsList, "doesn't", "does", "not")
        splitQruotationMark(wordsList, "didn't", "did", "not")
        splitQruotationMark(wordsList, "hasn't", "has", "not")
        splitQruotationMark(wordsList, "hadn't", "had", "not")
        splitQruotationMark(wordsList, "haven't", "have", "not")
        splitQruotationMark(wordsList, "wouldn't", "would", "not")
        splitQruotationMark(wordsList, "shouldn't", "sould", "not")
        splitQruotationMark(wordsList, "couldn't", "could", "not")
        splitQruotationMark(wordsList, "he's", "he", "is")
        splitQruotationMark(wordsList, "she's", "she", "is")
        splitQruotationMark(wordsList, "it's", "it", "is")
        splitQruotationMark(wordsList, "there's", "there", "is")
        splitQruotationMark(wordsList, "that's", "that", "is")
        splitQruotationMark(wordsList, "what's", "what", "is")
        splitQruotationMark(wordsList, "who's", "who", "is")
        splitQruotationMark(wordsList, "he's", "he", "is")
        # splitQruotationMark(wordsList, "am", "ante", "meridiem")
        # splitQruotationMark(wordsList, "pm", "post", "meridiem")
        splitQruotationMark(wordsList, "i'ma", "i'm", "goingto")
        splitQruotationMark(wordsList, "goingto", "going", "to")
        splitQruotationMark(wordsList, "i'm", "i", "am")
        splitQruotationMark(wordsList, "you're", "you", "are")
        splitQruotationMark(wordsList, "they're", "they", "are")
        splitQruotationMark(wordsList, "we're", "we", "are")
        splitQruotationMark(wordsList, "i'd", "i", "had")
        splitQruotationMark(wordsList, "he'd", "he", "had")
        splitQruotationMark(wordsList, "she'd", "she", "had")
        splitQruotationMark(wordsList, "you'd", "you", "had")
        splitQruotationMark(wordsList, "they'd", "they", "had")
        splitQruotationMark(wordsList, "how'd", "how", "did")
        splitQruotationMark(wordsList, "they've", "they", "have")
        splitQruotationMark(wordsList, "i've", "i", "have")
        splitQruotationMark(wordsList, "you've", "you", "have")
        splitQruotationMark(wordsList, "we've", "we", "have")
        splitQruotationMark(wordsList, "we'd", "we", "had")
        splitQruotationMark(wordsList, "it'd", "it", "had")
        splitQruotationMark(wordsList, "i'll", "i", "will")
        splitQruotationMark(wordsList, "he'll", "he", "will")
        splitQruotationMark(wordsList, "she'll", "she", "will")
        splitQruotationMark(wordsList, "you'll", "you", "will")
        splitQruotationMark(wordsList, "we'll", "we", "will")
        splitQruotationMark(wordsList, "it'll", "it", "will")
        splitQruotationMark(wordsList, "they'll", "it", "will")
        splitQruotationMark(wordsList, "kinda", "kind", "of")
        splitQruotationMark(wordsList, "st", "first", "'")
        splitQruotationMark(wordsList, "nd", "second", "'")
        splitQruotationMark(wordsList, "rd", "third", "'")
        splitQruotationMark(wordsList, "dr", "doctor", "'")
        splitQruotationMark(wordsList, "esp", "especially", "'")
        splitQruotationMark(wordsList, "sth", "something", "'")
        splitQruotationMark(wordsList, "sb", "somebody", "'")
        splitQruotationMark(wordsList, "'cause", "because", "'")
        splitQruotationMark(wordsList, "'til", "until", "'")
        splitQruotationMark(wordsList, "'em", "them", "'")
        splitQruotationMark(wordsList, "o'clock", "o", "clock")
        splitQruotationMark(wordsList, "etc", "et", "cetera")

