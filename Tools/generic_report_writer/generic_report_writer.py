from pathlib import Path
from inspect import currentframe, getframeinfo

filename = getframeinfo(currentframe()).filename
docs = Path.cwd() / '.foo' / 'reports'
here = Path(filename).resolve().parent

reports = {}

def get_generic_descriptor(grade: str) -> str: 
    '''
    Dynamically loads generic descriptors for games. 

    Searches for and finds a file with the appropriate grade. 

    params
    : grade - the grade to get a descriptor

    returns
    : str - a string describing the grade
    '''
    with open(docs/grade) as fd: return fd.readlines()

def get_report(name: str, grade: str) -> str:
    '''
    Generates a generic report based on grade. 

    params
    : name - the students name
    : grade - the grade of the student. Used as key
    
    returns
    : string - a bespoke string based off of given grade. 
    '''
    return f"{name}, {reports[grade]}"

reports["a"] = get_generic_descriptor('A')
reports["b"] = get_generic_descriptor('B')
reports["c"] = get_generic_descriptor('C')
reports["d"] = get_generic_descriptor('D')
reports["e"] = get_generic_descriptor('E')
reports["v"] = get_generic_descriptor('V')

with open(docs/"names") as fd:
    for line in fd.readlines():
        name, grade = line.strip().split(",")
        print(get_report(name, grade.lower()), end="\n\n")