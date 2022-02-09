import re

with open('bench.out') as f:
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
        if (n == 3):
            n = 0
            avgs.append(sum/3)
            sum = 0

    print(avgs)