from pathlib import Path
from inspect import currentframe, getframeinfo

filename = getframeinfo(currentframe()).filename
here = Path(filename).resolve().parent

reports = {
    'a' : "I'm afraid for the calendar. Its days are numbered. (A)",
    'b' : "what’s black and yellow and flies at 30,000 feet? (B)ees on an airplane.",
    'c' : "did you hear about the pirate who had trouble with the alphabet? He always got lost at C!",
    'd' : "which bear is the most condescending? A pan-(D)uh!",
    'e' : "why are sheep such bad drivers? They always make illegal (E)we turns!",
    'v' : "(V)oilà! In (v)iew, a humble (v)aude(v)illian (v)eteran, cast (v)icariously as both (v)ictim and (v)illain by the (v)icissitudes of Fate. This (v)isage, no mere (v)eneer of (v)anity, is a (v)estige of the (v)ox populi, now (v)acant, (v)anished. Howe(v)er, this (v)alorous (v)isitation of a bygone (v)exation stands (v)i(v)ified, and has (v)owed to (v)anquish these (v)enal and (v)irulent (v)ermin (v)anguarding (v)ice and (v)ouchsafing the (v)iolently (v)icious and (v)oracious (v)iolation of (v)olition! The only (v)erdict is (v)engeance; a (v)endetta held as a (v)oti(v)e, not in (v)ain, for the (v)alue and (v)eracity of such shall one day (v)indicate the (v)igilant and the (v)irtuous. (V)erily, this (v)ichyssoise of (v)erbiage (v)eers most (v)erbose, so let me simply add that it's my (v)ery good honor to meet you and you may call me (V).",
}

def get_report(name, grade):
    return f"{name}, {reports[grade]}"

with open(here/"names") as fd:
    for line in fd.readlines():
        name, grade = line.strip().split(",")
        print(get_report(name, grade.lower()), end="\n\n")