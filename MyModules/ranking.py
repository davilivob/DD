from MyModules import doTheMath as Math, art as Art
import sys
from os.path import dirname, abspath

d = dirname(dirname(abspath(__file__)))
sys.path.append(d)


class Ranking:
    def __init__(self, inputNumber, Array, BigNumArray, capital):
        self.RankingNumber = inputNumber
        self.RepeatedArray = Array
        self.BigNum = len(BigNumArray)
        self.Capital = capital
        self.RankRange()

    def RankRange(self):
        if self.RankingNumber == "all":
            RankRange = len(self.RepeatedArray)
        elif self.RankingNumber == "":
            RankRange = 0
        elif Math.checkNumber(self.RankingNumber) == False:
            RankRange = 0
        elif Math.checkNumber(self.RankingNumber) == True:
            RankRange = int(self.RankingNumber)
            if int(self.RankingNumber) >= len(self.RepeatedArray):
                RankRange = len(self.RepeatedArray)

        return RankRange

    def TopUsed(self):
        TopUsed = ""
        arr = Math.createRankinglistArray(self.RankRange())
        for index in arr:
            if index < Math.row():
                TopUsed += "\n      "
            if self.Capital == 1:
                self.RepeatedArray[index][1] = self.RepeatedArray[index][1].capitalize(
                )
            Word = "".join(
                [str(index + 1), '. "', self.RepeatedArray[index][1], '"'])
            Amount = "".join([": ", str(self.RepeatedArray[index][0]), " "])
            Percentage = Math.percent(
                self.RepeatedArray[index][0], self.BigNum, 100)
            TopUsed += Art.FormalFiller("".join([Word, Amount, Percentage]), 3)

        return TopUsed
