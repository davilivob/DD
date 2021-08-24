import sys
from os.path import dirname, abspath

d = dirname(dirname(abspath(__file__)))
sys.path.append(d)

from MyModules import art as Art

import time
import json

with open("Databases/Setting.json", mode="r") as file:
    Setting = json.loads(file.read())

fillBar, doTheTimeBar, barRange = Setting["fillBar"], Setting["doTheTimeBar"], 46


class Counter:
    start = time.time()
    prevTime = float(Setting["PrevTime"])


def timeNow():
    return time.time() - Counter.start


if doTheTimeBar == True:
    def Adding():
        if int(timeNow() * 1000) % 100 == 0 and timeNow() <= Counter.prevTime:
            loadRatio = timeNow() / Counter.prevTime
            sys.stdout.write(
                Art.FontEffect(
                    "".join(["\u001b[1000D" + Art.LoadBar(loadRatio, barRange, 0)]),
                    208,
                    0,
                )
            )
            sys.stdout.flush()


else:

    def Adding():
        return 0


if fillBar == True:

    def AddingFiller():
        sys.stdout.write(
            Art.FontEffect(
                "".join(["\u001b[1000D", Art.LoadBar(1.0, barRange, 0)]), 208, 0
            )
        )
        sys.stdout.flush()
        print()
        print()
        print()


else:

    def AddingFiller():
        return 0


def showFinalTime():
    sys.stdout.write(
        Art.FontEffect(
            " ".join(
                [
                    "\u001b[1000D(Calculation's Completed in",
                    str(timeNow()),
                    "seconds)                                          ",
                ]
            ),
            240,
            0,
        )
    )
    sys.stdout.flush()
