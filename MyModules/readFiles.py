import MyModules.TimerLoadBar as TimeBar
import json
import sys
from os.path import dirname, abspath
from typing import overload

d = dirname(dirname(abspath(__file__)))
sys.path.append(d)


class Load:
    with open("Databases/Database.json", mode="r", encoding="utf-8") as file:
        load_json = json.loads(file.read())
        TimeBar.Adding()

    with open("Databases/daily_english.json", mode="r", encoding="utf-8") as file:
        NormalDict = file.read()
        TimeBar.Adding()

    with open("Databases/lyric_dictionary.json", mode="r", encoding="utf-8") as file:
        LyricDict = file.read()
        TimeBar.Adding()

    Dictionary = NormalDict + LyricDict

    lastCharsRepeated = load_json[2]["Analysing Results"]["Advanced Datas"][
        "Characters Repeated Times"
    ]

    # lastAllan = load_json[3]["Project Statment"]["Allan Poe Index"]

    with open(
        "Databases/TypingPracticeRecords.json", mode="r", encoding="utf-8"
    ) as file:
        typingJson = file.read()
        TimeBar.Adding()
        typingDatas = json.loads(typingJson)
        TimeBar.Adding()

    with open("Databases/Setting.json", mode="r", encoding="utf-8") as file:
        setting = json.loads(file.read())
        definition = setting["definition"]
        comparison = setting["comparison"]
        lyric = setting["lyric"]
