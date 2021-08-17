import json
import time

class Load:
    with open("Databases\Database.json", mode="r") as file:
        load_json = json.loads(file.read())
    with open("daily_english.json", mode="r") as file:
        Dictionary = file.read()

    lastCharsRepeated = load_json[2]["Analysing Results"]["Advanced Datas"][
        "Characters Repeated Times"
    ]

    prevTime = load_json[4]["Last Loading Time"]

    lastAllan = load_json[3]["Project Statment"]["Allan Poe Index"]

    with open("Databases\TypingPracticeRecords.json", mode="r") as file:
        typingJson = file.read()
        typingDatas =  json.loads(typingJson)
