#!/usr/bin/env python

import time

print("Press ENTER to begin. Afterwards, press ENTER to \"click\" the stopwatch. Press CTRL-C to quit.")
input()
print("Started.")
startTime = time.time()
lastTime = startTime
lapNum = 1

try:
    while True:
        input()
        lapTime = round(time.time()-lastTime,2)
        totalTime = round(time.time()-startTime,2)

        lapStr = str(lapNum).ljust(2)
        totalStr = str(totalTime).rjust(5)
        lapTStr = str(lapTime).rjust(5)
        print(f'Lap #{lapStr}:{totalStr}({lapTStr})',end="")
        lapNum += 1
        lastTime = time.time()
except KeyboardInterrupt:
  print("\nDone.")