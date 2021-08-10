vocabularies = 0
with open("daily_english.json", mode="r") as file:
    dictionary = file.read()
dictionary = dictionary.replace('""', '').replace(' "', '').replace('."', '').replace('!"','').replace('?"', '')

for char in dictionary:
    if char == '"':
        vocabularies += 1
# print(dictionary,'\n')
print(vocabularies)