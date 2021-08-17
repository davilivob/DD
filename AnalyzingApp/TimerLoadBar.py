import math
import sys
import time

class Counter:
    start = time.time()

from os.path import dirname, abspath
d = dirname(dirname(abspath(__file__)))
sys.path.append(d)
import art as Art
import readFiles as File

prevTime = File.Load.prevTime
lastAllan = File.Load.lastAllan

def timeNow():
    return time.time() - Counter.start

def Adding():
    loadRatio = timeNow() / prevTime
    barRange = math.floor(lastAllan)
    sys.stdout.write(
        Art.FontEffect("\u001b[1000D" + Art.LoadBar(loadRatio, barRange, 0), 208, 0)
    )
    sys.stdout.flush()
    return 0
