import names
from random import randint
from pathlib import Path
from inspect import currentframe, getframeinfo

this_filename = getframeinfo(currentframe()).filename
this_stem = Path(this_filename).stem
here = Path(this_filename).resolve().parent

with open(here / f"{this_stem}.txt", 'w') as foo:
    for _ in range(1000):
        name = names.get_full_name()
        score = randint(1, 100)
        foo.write(f"{name}:{score}\n")
