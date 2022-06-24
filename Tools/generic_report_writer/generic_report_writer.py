import pandas as pd
from pathlib import Path
from inspect import currentframe, getframeinfo

filename = getframeinfo(currentframe()).filename
docs = Path.cwd() / '.foo' / 'reports'
here = Path(filename).resolve().parent

def get_generic_descriptor(grade: str) -> str: 
    '''
    Dynamically loads generic descriptors for games. 

    Searches for and finds a file with the appropriate grade. 

    params
    : grade - the grade to get a descriptor

    returns
    : str - a string describing the grade
    '''
    with open(docs/grade) as fd: return fd.readlines()[0]

def get_report(reports: dict, name: str, grade: str) -> str:
    '''
    Generates a generic report based on grade. 

    params
    : name - the students name
    : grade - the grade of the student. Used as key
    
    returns
    : string - a bespoke string based off of given grade. 
    '''
    return f"{name}, {reports[grade]}"

def load_descriptors() -> dict:
    '''
    Loads the descriptors for each grade into dictionary. 

    params
    : none

    returns
    : a dictionary of generic grade descriptors.
    '''
    reports = {}
    reports["A"] = get_generic_descriptor('A')
    reports["B"] = get_generic_descriptor('B')
    reports["C"] = get_generic_descriptor('C')
    reports["D"] = get_generic_descriptor('D')
    reports["E"] = get_generic_descriptor('E')
    reports["V"] = get_generic_descriptor('V')
    reports["P"] = get_generic_descriptor("P")
    return reports

def write_reports(course_name: str, results: pd.DataFrame, generic_descriptors: dict) -> None:
    '''
    Writes reports for a given course. 

    params
    : course_name - the string name of the course 
    : results - a dataframe of results
    : reports - a dictionary of generic grade descriptors
    '''
    with open(docs/f"{course_name.replace(' ', '')}.txt", 'w') as fd:
        fd.write(f"# {course_name} reports\n\n")
        for _, row in results[results['COURSE_NAME'] == course_name].iterrows():
            _, given = row.STUDENT_NAME.strip().split(",")
            given= given.split(" ")[1]
            fd.write(f"## {row.STUDENT_NAME} {row.GRADE}\n\n")
            fd.write(f"{get_report(generic_descriptors, given, row.GRADE)}\n\n")

if __name__ == "__main__": 
    results = pd.read_excel(docs/"marks.xlsx", converters={'STUDENT_NUMBER': '{:0>7}'.format})
    generic_descriptors = load_descriptors()
    course_names = sorted(results.COURSE_NAME.unique())
    for course_name in course_names: 
        write_reports(course_name, results, generic_descriptors)