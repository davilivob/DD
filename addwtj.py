
from MyModules import Aj
import json
# import sys
# from os.path import dirname, abspath
# d = dirname(dirname(abspath(__file__)))
# sys.path.append(d)


with open('./Databases/Database.json') as file:
    DBjson = json.loads(file.read())
    words = list(DBjson[1]['Words Repeat Time'])

with open('./Databases/words_to_join.json') as file:
    wtjjson = json.loads(file.read())

with open('Databases/text.txt') as file:
    string = file.read().lower()

deleted = list(('-', '\n', ',', '.', ';', ':', '?'))
for char in deleted:
    string = string.replace(char, ' ')

while '  ' in string:
    string = string.replace('  ', ' ')

arr = string.split(' ')

Aj.SeparateAllShort(arr)
newarr = []

for element in arr:
    if element.lower() not in words and element.lower() not in wtjjson and element not in newarr and "'" not in element:
        newarr.append(element.lower())


def printArr(arr):
    n = 0
    for element in arr:
        print(n, element, sep=': ')
        n += 1


printArr(newarr)


def getInput():
    Input = input('\n')
    if Input == '':
        for element in newarr:
            wtjjson.update({element: [""]})

        with open('./Databases/words_to_join.json', 'w') as file:
            json.dump(wtjjson, file)
        return 0
    else:
        if Input.isnumeric():
            if int(Input) < len(newarr):
                newarr.remove(newarr[int(Input)])
                printArr(newarr)
        else:
            exit()
        getInput()


getInput()
