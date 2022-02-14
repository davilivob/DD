from MyModules import (
    art as Art,
    readFiles as File,
    doTheMath as Math,
    Aj as AJ,
    regularData as R,
    AllanBill as AB,
    advancedData as A,
    typingData as TT,
    ranking as Rank,
)
from MyModules import TimerLoadBar as TimeBar
import json

print()
ifPrint = input(
    "If You Hope the Analysis Results to be Displayed on the Terminal, Just Type Anything Then Press Enter."
    + "\n\nOtherwise, Press Enter Only: "
)
if ifPrint != "":
    RankingList = input(
        "\nTo See a Ranked List of the Most Frequently Used Words, Enter 'all' or Enter the Range of the List."
        + "\n\nOtherwise, Press Enter Only: "
    )
else:
    RankingList = "0"


print()


A = A.A
wordsList, WordsRepeated, WordsRepeatedJson = (
    A.wordsList,
    A.WordsRepeated,
    A.WordsRepeatedJson,
)

R = R.R
(
    sentences,
    vocabularies,
    definitions,
    comparisons,
    unlearned,
    learned,
    examples,
    fromlyrics,
) = (
    R.sentences,
    R.vocabularies,
    R.definitions,
    R.comparisons,
    R.unlearned,
    R.learned,
    R.examples,
    R.fromlyrics,
)

Allan, Bill = AB.AllanBill("A"), AB.AllanBill("B")
(
    AllanGrade,
    AllanShowLettersSort,
    AllanLettersRepeatedJson,
    allLetters,
    lettersSortList,
    BillGrade,
    BillShowLettersSort,
    BillLettersRepeatedJson,
    firstLettersSortList,
) = (
    Allan.Grade(),
    Allan.ShowLettersSort(),
    Allan.LettersRepeatedJson(),
    Allan.letters(),
    Allan.CurrentSortList(),
    Bill.Grade(),
    Bill.ShowLettersSort(),
    Bill.LettersRepeatedJson(),
    Bill.CurrentSortList(),
)
allLettersLen = len(allLetters)
Type = TT.TypingTest

WordsRanking = Rank.Ranking(RankingList, WordsRepeated, wordsList, 1)
LettersRanking = Rank.Ranking("26", lettersSortList, allLetters, 0)
FirstLettersRanking = Rank.Ranking("26", firstLettersSortList, wordsList, 0)


def UploadDatasToJson():
    WordsKinds = len(WordsRepeated)
    TotalWords = len(wordsList)
    TotalChars = allLettersLen
    CharsPerWord = Math.takeDecimal(allLettersLen, len(wordsList), 100000)
    AllanJson = {
        "Allan Poe Index": float(AllanGrade[3:-3]),
        "Bill Murray Index": float(BillGrade[3:-3]),
    }
    analysisJson = {
        "Vocabularies": {
            "Total": vocabularies,
            "Learned": learned,
            "Unlearned": unlearned,
        },
        "Sentences": {
            "Total": sentences,
            "Examples": examples,
            "Definitions": definitions,
            "Comparisons": comparisons,
            "Lyrics": fromlyrics,
        },
        "Advanced Datas": {
            "Words Kinds": WordsKinds,
            "Total Words": TotalWords,
            "Total Characters": TotalChars,
            "Characters Repeated Times": AllanLettersRepeatedJson,
            "First Letters Repeated Times": BillLettersRepeatedJson,
            "Letters Per Words": CharsPerWord,
        },
        "Typing Results": {
            "Test Duration": Type.avgTime,
            "WPM": Type.avgWpm,
            "Accuracy": Type.avgAccuracy,
            "BackSpace Press Rate": Type.avgBackrate,
            "Wrong Chars List": Type.WrongCharsRepeatedJson,
            "Typo Rate": Type.TypoRateJson,
        },
    }

    with open("Databases/Database.json", mode="w") as file:
        json.dump(
            [
                {"Words List": wordsList},
                {"Words Repeat Time": WordsRepeatedJson},
                {"Analysing Results": analysisJson},
                {"Project Statment": AllanJson},
            ],
            file,
            indent=2,
        )

    def settingUpload():
        return {
            "PrevTime": TimeBar.timeNow(),
            "doTheTimeBar": 1,
            "fillBar": 1,
            "definition": File.Load.definition,
            "comparison": File.Load.comparison,
            "lyric": File.Load.lyric,
        }

    with open("Databases/Setting.json", mode="w") as file:
        json.dump(settingUpload(), file, indent=2)


class Write:
    def AllanRate():
        return "".join(
            [
                Art.FontEffect("Allan Poe Index:    ", 83, 1),
                Art.FontEffect(str(AllanGrade)[2:-1], 0, 1),
                "\n",
                Art.FontEffect(
                    Art.LoadBar(
                        float(str(AllanGrade)[2:-3]) / 100, 100, 0), 185, 0
                ),
            ]
        )

    def AllanResult():
        return "          ".join(["Result:", AllanShowLettersSort[0:-2]])

    def BillRate():
        return "".join(
            [
                Art.FontEffect("Bill Murray Index:  ", 83, 1),
                Art.FontEffect(str(BillGrade)[2:-1], 0, 1),
                "\n",
                Art.FontEffect(
                    Art.LoadBar(
                        float(str(BillGrade)[2:-3]) / 100, 100, 0), 185, 0
                ),
            ]
        )

    def BillResult():
        return "          ".join(["Result:", BillShowLettersSort[0:-2]])

    def Vocabularies():
        return "".join([Art.FontEffect("Vocabularies: ", 160, 1), str(vocabularies)])

    def Learned():
        return "".join(
            ["Learned: ", str(learned), Math.percent(
                learned, vocabularies, 10)]
        )

    def Unlearned():
        return "".join(
            ["Unlearned: ", str(unlearned), Math.percent(
                unlearned, vocabularies, 10)]
        )

    def Individuals():
        return "".join(["Individuals: ", str(len(WordsRepeated))])

    def Sentences():
        return "".join([Art.FontEffect("Sentences:    ", 160, 1), str(sentences)])

    def Examples():
        return "".join(
            ["Examples: ", str(examples), Math.percent(
                examples, sentences, 10)]
        )

    def Definitions():
        return "".join(
            [
                "Definitions: ",
                str(definitions),
                Math.percent(definitions, sentences, 10),
            ]
        )

    def Comparisons():
        return "".join(
            [
                "Comparisons: ",
                str(comparisons),
                Math.percent(comparisons, sentences, 10),
            ]
        )

    def FromLyrics():
        return "".join(
            [
                "Lyrics: ",
                str(fromlyrics),
                Math.percent(fromlyrics, sentences, 10),
            ]
        )

    def TotalWords():
        return "".join(["Total Words: ", str(len(wordsList))])

    def TotalCharacters():
        return "".join(["Total Characters: ", str(allLettersLen)])

    def LettersPerWord():
        return "".join(
            [
                "Letters Per Word: ",
                str(Math.takeDecimal(allLettersLen, len(wordsList), 1000)),
            ]
        )

    def avgTime():
        return " ".join(["Test Duration:", str(Type.avgTimePrint)])

    def avgWpm():
        return " ".join(["WPM:", str(Type.avgWpmPrint)])

    def avgAccuracy():
        return " ".join(["Accuracy:", str(Type.avgAccuracyPrint), "%"])

    def avgBackrate():
        return " ".join(["Back Rate:", str(Type.avgBackratePrint), "%"])

    def MostType():
        return "".join(["Most Typo: ", '"', Type.MostTypo, '"'])


TimeBar.AddingFiller()


def PrintResults():
    Art.Print.ln(Write.AllanRate())
    Art.Print.tabln(
        Art.FontEffect(
            "".join(["Stantard:        ", ", ".join(AB.CriticalSortList("A"))]),
            0,
            1,
        )
    )
    Art.Print.tabln(Write.AllanResult())
    Art.Print.ln(Write.BillRate())
    Art.Print.tabln(
        Art.FontEffect(
            "".join(["Stantard:        ", ", ".join(AB.CriticalSortList("B"))]),
            0,
            1,
        )
    )
    Art.Print.tabln(Write.BillResult())
    Art.Print.ln(Write.Vocabularies())
    Art.Print.tabln(
        "".join(
            [
                Art.FormalFiller(Write.Learned(), 3),
                Art.FormalFiller(Write.Unlearned(), 3),
                Write.Individuals(),
            ]
        )
    )
    Art.Print.ln(Write.Sentences())
    Art.Print.tabln(
        "".join(
            [
                Art.FormalFiller(Write.Examples(), 4),
                Art.FormalFiller(Write.Definitions(), 4),
                Art.FormalFiller(Write.FromLyrics(), 4),
                Write.Comparisons(),
            ]
        )
    )
    Art.Print.ln(Art.FontEffect("Advanced Datas: ", 201, 1))
    Art.Print.tabln(
        "".join(
            [
                Art.FormalFiller(Write.TotalWords(), 3),
                Art.FormalFiller(Write.TotalCharacters(), 3),
                Write.LettersPerWord(),
            ]
        )
    )
    Art.Print.ln(
        " ".join(
            [
                Art.FontEffect("Typing Test Results:", 165, 1),
                " ( based on",
                Art.FontEffect("".join(str(Type.testNumber)), 220, 0),
                Art.FontEffect("Tests", 213, 0),
                "with total",
                Art.FontEffect("".join(str(Type.totalTime)), 220, 0),
                Art.FontEffect("Minutes", 213, 0),
                "and",
                Art.FontEffect("".join(str(Type.totalChars)), 220, 0),
                Art.FontEffect("Characters", 213, 0),
                ")",
            ]
        )
    )
    fillerForType = " " * int(
        (
            110
            - len(
                Write.MostType()
                + Write.avgAccuracy()
                + Write.avgWpm()
                + Write.avgBackrate()
                + Write.avgTime()
            )
        )
        / 4
    )
    Art.Print.tabln(
        fillerForType.join(
            [
                Write.MostType(),
                Write.avgAccuracy(),
                Write.avgWpm(),
                Write.avgBackrate(),
                Write.avgTime(),
            ]
        )
    )
    print(Art.FontEffect(" ".join(["TOP USED LETTERS: "]), 200, 1))
    Art.Print.tabln(LettersRanking.TopUsed())
    print(Art.FontEffect(" ".join(["TOP USED FIRST LETTERS: "]), 141, 1))
    wordsRankNum = WordsRanking.RankRange()
    Art.Print.tabln(FirstLettersRanking.TopUsed())
    if wordsRankNum != 0:
        print(
            Art.FontEffect(
                " ".join(["TOP", str(wordsRankNum), "USED WORDS: "]), 208, 1)
        )
        Art.Print.tabln(WordsRanking.TopUsed())


if ifPrint != "":
    PrintResults()

UploadDatasToJson()
TimeBar.showFinalTime()
