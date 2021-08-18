import json

print()
ifPrint = input(
    "If You Hope the Analyzing Results Show on the Terminal, Just Press Any Button and Press Enter.\n\nOtherwise, Press Enter Only: "
)
if ifPrint != "":
    RankingList = input("\nPlease Enter The Number of Words Ranking You Want to See: ")
else:
    RankingList = "0"

import MyModules.TimerLoadBar as TimeBar

time_start = TimeBar.Counter.start
print()

from MyModules import (
    art as Art,
    readFiles as File,
    doTheMath as Math,
    Aj as AJ,
    ragularData as R,
    AllanBill as AB,
    advancedData as A,
    typingData as TT,
    ranking as Rank,
)


A = A.A
wordsList, WordsRepeated, WordsRepeatedJson = (
    A.wordsList,
    A.WordsRepeated,
    A.WordsRepeatedJson,
)

R = R.R
(sentences, vocabularies, definitions, comparisons, unlearned, learned, examples,) = (
    R.sentences,
    R.vocabularies,
    R.definitions,
    R.comparisons,
    R.unlearned,
    R.learned,
    R.examples,
)

Allan, Bill = AB.AllanBill("A"), AB.AllanBill("B")
(
    AllanGrade,
    AllanShowLettersSort,
    AllanLettersRepeatedJson,
    BillGrade,
    BillShowLettersSort,
    BillLettersRepeatedJson,
) = (
    Allan.Grade(),
    Allan.ShowLettersSort(),
    Allan.LettersRepeatedJson(),
    Bill.Grade(),
    Bill.ShowLettersSort(),
    Bill.LettersRepeatedJson(),
)

Type = TT.TypingTest

WordsRanking = Rank.Ranking(RankingList, WordsRepeated, wordsList)


def UploadDatasToJson():
    WordsKinds = len(WordsRepeated)
    TotalWords = len(wordsList)
    TotalChars = len(Allan.letters())
    CharsPerWord = Math.takeDecimal(len(Allan.letters()), len(wordsList), 100000)
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
            "Wrong Words List": Type.WrongWordsRepeatedJson,
            "Wrong Chars List": Type.WrongCharsRepeatedJson,
            "Typo Rate": Type.TypoRateJson,
        },
    }

    with open("Databases\Database.json", mode="w") as file:
        json.dump(
            [
                {"Words List": wordsList},
                {"Words Repeat Time": WordsRepeatedJson},
                {"Analysing Results": analysisJson},
                {"Project Statment": AllanJson},
            ],
            file,
        )
    with open("Databases\prevTime.txt", mode="w") as file:
        file.write(str(TimeBar.timeNow()))


class Write:
    def AllanRate():
        return "".join(
            [
                Art.FontEffect("Allan Poe Index:    ", 83, 1),
                Art.FontEffect(str(AllanGrade)[2:-1], 0, 1),
                "\n",
                Art.FontEffect(
                    Art.LoadBar(float(str(AllanGrade)[2:-3]) / 100, 100, 0), 185, 0
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
                    Art.LoadBar(float(str(BillGrade)[2:-3]) / 100, 100, 0), 185, 0
                ),
            ]
        )

    def BillResult():
        return "          ".join(["Result:", BillShowLettersSort[0:-2]])

    def Vocabularies():
        return "".join([Art.FontEffect("Vocabularies: ", 160, 1), str(vocabularies)])

    def Learned():
        return "".join(
            ["Learned: ", str(learned), Math.percent(learned, vocabularies, 10)]
        )

    def Unlearned():
        return "".join(
            ["Unlearned: ", str(unlearned), Math.percent(unlearned, vocabularies, 10)]
        )

    def Individuals():
        return "".join(["Individuals: ", str(len(WordsRepeated))])

    def Sentences():
        return "".join([Art.FontEffect("Sentences:    ", 160, 1), str(sentences)])

    def Examples():
        return "".join(
            ["Examples: ", str(examples), Math.percent(examples, sentences, 10)]
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

    def TotalWords():
        return "".join(["Total Words: ", str(len(wordsList))])

    def TotalCharacters():
        return "".join(["Total Characters: ", str(len(Allan.letters()))])

    def LettersPerWord():
        return "".join(
            [
                "Letters Per Word: ",
                str(Math.takeDecimal(len(Allan.letters()), len(wordsList), 1000)),
            ]
        )

    def avgTime():
        return " ".join(["Test Duration:", str(Type.avgTimePrint), "mins"])

    def avgWpm():
        return " ".join(["WPM:", str(Type.avgWpmPrint)])

    def avgAccuracy():
        return " ".join(["Accuracy:", str(Type.avgAccuracyPrint), "%"])

    def avgBackrate():
        return " ".join(["Back Rate:", str(Type.avgBackratePrint), "%"])

    def MostType():
        return "".join(["Most Typo: ", '"', Type.MostTypo, '"'])


TimeBar.AddingFiller()

print()
print()
print()


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
                Art.FormalFiller(Write.Examples(), 3),
                Art.FormalFiller(Write.Definitions(), 3),
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
    Art.Print.ln(Art.FontEffect("Typing Test Results: ", 165, 1))
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
    print(
        Art.FontEffect(
            " ".join(["TOP", str(WordsRanking.RankRange()), "USED WORDS: "]), 208, 1
        )
    )
    Art.Print.tabln(WordsRanking.TopUsed())


if ifPrint != "":
    PrintResults()

UploadDatasToJson()
TimeBar.showFinalTime()
