from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from docxtpl import DocxTemplate
from inspect import currentframe, getframeinfo
from datetime import datetime
from json import dumps
import toml

def get_files_of_type(location: Path, file_type: str) -> list[Path]:
    """
    Given a starting directory find all possible subject configuration files of a type. 
    
    param
    : location - the starting path to search from
    : file_type - the type of file to find

    return
    : a list of paths with given file_type
    """
    if file_type == None: return None
    file_list = []
    for x in location.iterdir():
        if x.is_file() and x.suffix == file_type: 
            file_list.append(x)
        elif x.is_dir(): file_list.extend(get_tomls(location / x))
    return file_list


def get_tomls(location: Path) -> list[Path]:
    """
    Given a starting directory find all possible subject configuration files (toml). 
    
    param
    : location - the starting path to search from

    return
    : a list of paths
    """
    return get_files_of_type(location, ".toml")

def get_docx_templates(location: Path) -> list[Path]:
    """
    Given a starting directory find all possible subject configuration files (docx). 
    
    param
    : location - the starting path to search from

    return
    : a list of paths
    """
    return get_files_of_type(location, ".docx")


def load_tomls(subject_tomls: toml) -> list:
    """
    Given a list of paths where tomls exist load them into memory 
    """
    out = []
    for subject_toml in subject_tomls:
        try:
            out.append(toml.load(subject_toml))
        except Exception as e: 
            print(e)
    return out


def build_assignments_templates(output, subject, assignment_item_templates):
    year = subject['year']
    semester = subject['semester']
    year_semester_dir = Path(output / year / semester)
    print(year_semester_dir, assignment_item_templates)
    for course in subject['courses']:
        for years in subject['courses'][course]['properties']['years']:
            for accreditation in subject['courses'][course]['properties']['accreditation']:
                for ai in subject['courses'][course]['assignments']:
                    assignment_item_name = subject['courses'][course]['assignments'][ai]
                    match assignment_item_name.split("_"):
                        case [percent, namea, nameb]: assignment_name = f"{namea} {nameb} {percent}"
                        case [percent, name]:  assignment_name = f"{name} {percent}"
                    course_name = ' '.join(course.split("_"))
                    assignment_item_dir = Path(year_semester_dir / course_name / ai)

                    print(get_docx_templates(assignment_item_templates / assignment_item_name))
                    break
                    # print(accreditation, years, assignment_name)
    

filename = getframeinfo(currentframe()).filename
here = Path(filename).resolve().parent
data = here / ".data"
achievement_standards = data / 'assets'
assignment_item_templates = here / '.templates'

template_docx = data / "template.docx"
subjects_dir = here / 'subjects'

output = here / "test_output"

subjects_tomls = get_tomls(subjects_dir)
subject_dics = load_tomls(subjects_tomls)
for subject in subject_dics:
    build_assignments_templates(output, subject, assignment_item_templates)