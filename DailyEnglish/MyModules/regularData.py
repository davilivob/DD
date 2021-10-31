import sys
from os.path import dirname, abspath

d = dirname(dirname(abspath(__file__)))
sys.path.append(d)

from MyModules import (
    readFiles as File,
    TimerLoadBar as TimeBar,
)

Dictionary = File.Load.Dictionary
defi = File.Load.definition
comp = File.Load.comparison
lyri = File.Load.lyric
sentenceEnd = ['."', '!"', '?"']
Dictionary = (
    Dictionary.replace('": [', "詞")
    .replace(defi, "定")
    .replace(comp, "比")
    .replace(lyri, "歌")
)
Dictionary = Dictionary.replace('""', "空")
for element in sentenceEnd:
    TimeBar.Adding()
    Dictionary = Dictionary.replace(element, "語")


class R:
    sentences = len(Dictionary.split("語")) - 1

    vocabularies = len(Dictionary.split("詞")) - 1

    definitions = len(Dictionary.split("定")) - 1

    comparisons = len(Dictionary.split("比")) - 1

    unlearned = len(Dictionary.split("空")) - 1
    
    fromlyrics = len(Dictionary.split("歌")) - 1

    learned = vocabularies - unlearned

    examples = sentences - definitions - comparisons - fromlyrics
