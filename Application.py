voc = sen = defi = com = unl = 0
with open("daily_english.json", mode="r") as file:
    dictionary = file.read()
# words
dictionary = dictionary.replace('": [', '詞')

# sentences
dictionary = dictionary.replace('."', '語').replace('!"', '語').replace('?"', '語').replace('\\\""', '語')

# definition
dictionary = dictionary.replace('"@', '定')

# comparison
dictionary = dictionary.replace('"&', '比')

# unlearned
dictionary = dictionary.replace('""', '空')

for char in dictionary:
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
def percent(element, object, degree):
    percentage = ((element)*100)/object
    percentage = float(int(percentage*degree))/degree
    return '( '+str(percentage)+'% )'

# print(dictionary,'\n')
decimalDegree = 10
print('\n', 'VOCABULARIES: ', str(voc))
print('\n   ', 'Learned: ', str(alr), percent(alr, voc, decimalDegree))
print('\n   ', 'Unlearned: ', str(unl), percent(unl, voc, decimalDegree))
print('\n', 'SENTENCES: ', str(sen))
print('\n   ', 'Examples: ', str(exp), percent(exp, sen, decimalDegree))
print('\n   ', 'Definitions: ', str(defi), percent(defi, sen, decimalDegree))
print('\n   ', 'Comparisons: ', str(com), percent(com, sen, decimalDegree))
print('\n')

