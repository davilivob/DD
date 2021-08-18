import sys
from os.path import dirname, abspath

d = dirname(dirname(abspath(__file__)))
sys.path.append(d)

from MyModules import art as Art, doTheMath as Math

import time

with open("Databases/prevTime.txt", mode="r") as file:
    prevTime = file.read()

efficiencyTest = 0


class Counter:
    start = time.time()
    prevTime = float(prevTime)


def timeNow():
    return time.time() - Counter.start


barRange = 46


def Adding():
    if int(timeNow() * 1000) % 100 == 0 and timeNow() <= Counter.prevTime:
        loadRatio = timeNow() / Counter.prevTime
        sys.stdout.write(
            Art.FontEffect(
                "".join(["\u001b[1000D" + Art.LoadBar(loadRatio, barRange, 0)]), 208, 0
            )
        )
        sys.stdout.flush()
        return 0


def AddingFiller():
    if efficiencyTest == 0:
        sys.stdout.write(
            Art.FontEffect(
                "".join(["\u001b[1000D", Art.LoadBar(1.0, barRange, 0)]), 208, 0
            )
        )
        sys.stdout.flush()


def showFinalTime():
    sys.stdout.write(
        Art.FontEffect(
            " ".join(
                [
                    "\u001b[1000D(Calculation Completed in",
                    str(Math.takeDecimal(timeNow(), 1, 10000)),
                    "seconds)                                          ",
                ]
            ),
            240,
            0,
        )
    )
    sys.stdout.flush()
