import re
import sys

print(sys.argv)

noTests = int(sys.argv[2])

with open(sys.argv[1]) as f:
    lines = f.readlines()
    times = []
    for line in lines:
        if (line.startswith("Elapsed Total time")):
            re.findall("\d+\.\d+", line)
            times.append(float(re.findall("\d+\.\d+", line)[0]))

    n = 0
    sum = 0
    avgs = []
    for time in times:
        sum += time
        n += 1
        if (n == noTests):
            n = 0
            avgs.append(sum/noTests)
            sum = 0

    print(avgs)