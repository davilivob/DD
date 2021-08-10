sum = 0
with open("daily_english.json", mode="r") as file:
    data = file.read()
data = data.replace('""', '').replace(' "', '').replace('."', '').replace('!"','').replace('?"', '')

for char in data:
    if char == '"':
        sum += 1
# print(data,'\n')
print(sum)