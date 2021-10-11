import json
import sys
from os.path import dirname, abspath
from typing import overload

d = dirname(dirname(abspath(__file__)))
sys.path.append(d)
import MyModules.TimerLoadBar as TimeBar


class Load:
    with open("Databases\Database.json", mode="r", encoding="utf-8") as file:
        load_json = json.loads(file.read().replace("\n",""))
        TimeBar.Adding()

    with open("Databases\daily_english.json", mode="r", encoding="utf-8") as file:
        Dictionary = file.read().replace("\n","")
        TimeBar.Adding()

    lastCharsRepeated = load_json[2]["Analysing Results"]["Advanced Datas"][
        "Characters Repeated Times"
    ]

    # lastAllan = load_json[3]["Project Statment"]["Allan Poe Index"]

    with open(
        "Databases\TypingPracticeRecords.json", mode="r", encoding="utf-8"
    ) as file:
        typingJson = file.read().replace(" ", "").replace("\n", "")
        TimeBar.Adding()
        typingDatas = json.loads("".join([typingJson,"]"]))
        TimeBar.Adding()
