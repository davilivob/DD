import json

with open('./Databases/Database.json') as file:
    DBjson = json.loads(file.read())
    words = list(DBjson[1]['Words Repeat Time'])

with open('./Databases/words_to_join.json') as file:
    wtjjson = json.loads(file.read())

with open('Databases/text.txt') as file:
    string = file.read()

deleted = list((',', '.', "'s", "'", ';', ':'))
string = string.replace('-', ' ').replace('\n', ' ')
for char in deleted:
    string = string.replace(char, '')


arr = string.split(' ')
newarr = []

for element in arr:
    if element.lower() not in words and element.lower() not in wtjjson:
        newarr.append(element.lower())

print(newarr)
input = input('\n')
if input == '':
    for element in newarr:
        wtjjson.update({element: [""]})

    with open('./Databases/words_to_join.json', 'w') as file:
        json.dump(wtjjson, file)
