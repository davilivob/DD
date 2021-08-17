import sys
from os.path import dirname,abspath
d = dirname(dirname(abspath(__file__)))
sys.path.append(d)
import art as Art 

def percent(element, object, degree):
    percentage = ((element) * 100) / object
    percentage = float(int(percentage * degree)) / degree
    return " ( " + str(percentage) + "% )"


def takeDecimal(x, y, degree):
    return float(int(x / y * degree)) / degree

def IndexGrade(currentSortList, criticalSortList, SorG):
    Grade = 100
    ShowLetterSort = ""
    for index in range(len(currentSortList)):
        num = 0
        dist = abs(index - criticalSortList.index(currentSortList[index][1]))
        char = currentSortList[index][1]
        if dist > 0:
            ShowLetterSort += Art.FontEffect(char, 210 - 2 * dist, 0) + ", "
        else:
            ShowLetterSort += Art.FontEffect(char, 0, 1) + ", "
        num = 1 - (1 / 25 * dist)
        Grade *= num

    if SorG == 0:
        return percent(Grade, 100, 100)
    else:
        return ShowLetterSort

def createRankinglistArray(RankRange):
    col = 3
    global row
    def row():
        return int(RankRange / col) + 1
    num = record = 0
    remain = RankRange - (col - 1) * row()
    arr = []
    while len(arr) < RankRange:
        arr.append(num)
        num += row()
        if record < remain:
            arr.append(num)
            num += row()
            record += 1
            arr.append(num)
            num -= row() * 2 - 1
        else:
            arr.append(num)
            num -= row() - 1
    return arr

def checkNumber(string):
        allNumbers = []
        for num in range(10):
            allNumbers.append(str(num))
        result = 0
        if string != "all":
            for char in string:
                if char not in allNumbers:
                    result += 1
        if result == 0:
            return True
        elif result > 0:
            return False