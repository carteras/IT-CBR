from statistics import mean, median, mode
from pathlib import Path
from inspect import currentframe, getframeinfo

this_filename = getframeinfo(currentframe()).filename
here = Path(this_filename).resolve().parent

names = []
scores = []

with open(here/"test_results.txt") as test_results:
    for line in test_results:
        line = line.strip()
        name, score = line.split(':')
        score = int(score)
        names.append(name)
        scores.append(score)

highest_score = max(scores)
first_highest = names[scores.index(highest_score)]
print(first_highest, highest_score)