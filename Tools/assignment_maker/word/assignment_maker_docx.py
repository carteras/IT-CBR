from dataclasses import dataclass
from pathlib import Path
from docxtpl import DocxTemplate
from inspect import currentframe, getframeinfo
from configparser import ConfigParser

filename = getframeinfo(currentframe()).filename
here_dir = Path(filename).resolve().parent
data_dir = here_dir / '.data'
assets_dir = data_dir / 'assets'
subjects_dir = here_dir / 'subjects'
output_dir = Path.cwd() / "assignments"
output_dir.mkdir(parents=True, exist_ok=True)

template = data_dir / "template.docx"

@dataclass
class Subject:
    """
    Represents a specific unit of a course. 

    Representation can include 
    * the name of the course and unit
    * what year this subject is being deployed
    * what semester this subject is being deployed
    * what composition the subject has (11/12/T/A)
    * What assignments have been prepared. 
    """
    course_name: str
    unit_name: str
    year: str
    semester: str
    composition: list[str]
    assessments: dict()

def config_subject(config_location: str) -> Subject:
    """
    Reads the subjects config.ini

    param: config_location the pathlib.Path of the config.ini for this subject
    
    return: a complete abstraction of subject. 
    """
    from itertools import product
    config = ConfigParser()
    config.read_file(open(config_location/'config.ini'))
    course_name = config.get("DEFAULT", 'CourseName')
    unit_name = config.get("DEFAULT", 'UnitName')
    year = config.get("DEFAULT", 'Year')
    semester = config.get("DEFAULT", 'Semester')
    year11 = config.get("YEARS", 'Year11')
    year12 = config.get("YEARS", 'Year12')
    accredited = config.get("ACCREDITATION", 'Accredited')
    tertiary = config.get("ACCREDITATION", 'Tertiary')
    assessments = {}
    assessments['AI1'] = config.get("ASSESSMENT_ITEMS", 'AI1')
    assessments['AI2'] = config.get("ASSESSMENT_ITEMS", 'AI2')
    assessments['AI3'] = config.get("ASSESSMENT_ITEMS", 'AI3')
    assessments['AI4'] = config.get("ASSESSMENT_ITEMS", 'AI4')
    years = []
    accreditation = []
    if year11: years.append(11) 
    if year12: years.append(12)
    if accredited: accreditation.append("A")
    if tertiary: accreditation.append("T")
    composition = list(product(years, accreditation))
    return Subject(
        course_name = course_name,
        unit_name = unit_name,
        year = year,
        semester = semester,
        composition = composition,
        assessments=assessments
    )

def get_dirs(dir) -> list[Path]:
    """
    Helper function to which returns a list of directories from any given directory. 

    param: a directory to search for sub-directories
    param: a list of Paths 
    """
    return [f for f in dir.iterdir() if f.is_dir()]

def get_subjects(subject_directory) -> list[Path]:
    """
    Helper function to which returns a list of subject directories from a directory. 

    param: a directory to search for sub-directories
    param: a list of Paths 
    """
    return get_dirs(subject_directory)

def get_assignment_folders(assignment_directory) -> list[Path]:
    """
    Helper function to which returns a list of assignment folders from any given subject directory. 

    param: a directory to search for sub-directories
    param: a list of Paths 
    """
    return get_dirs(assignment_directory)

def get_files_in_folder(folder_to_inspect: str) -> list[Path] | None:
    """
    Helper function to return a list of all files in a directory. 

    params: 
    folder_to_inspect: the folder to search
    
    return: 
    A list of Paths of the files in the directory

    None if no files are found
    """
    if not folder_to_inspect.is_dir(): return None
    return [f for f in folder_to_inspect.iterdir() if f.is_file()]

def build_doc_context_accreditation(folder: str, year: str, accrediation: str) -> dict | None:
    if not folder.is_dir(): return None
    if not any(folder.iterdir()): return None
    # TODO make different versions of rubrics by year/accreditation
    task = f"task.docx"
    rubric = f"rubric.docx"
    
    return {
        'task' : task,
        'rubric' : rubric,
    }

def build_doc_context(folder: Path, doc: DocxTemplate) -> dict | None:
    """
    Builds the context for the coversheet. 

    params: 
    folder: The path where the task and rubric, are found. 

    return: 
    None: if the given folder is not a directory
    None: if there are no files in the folder
    dict: if the given files are found
    """
    if not folder.is_dir(): return None
    if not any(folder.iterdir()): return None
    # if file_address.name == "task.docx":
    #                 task_path = Path(file_address)
    #                 task = doc.new_subdoc(task_path)
    #             elif file_address.name == 'rubric.docx':
    #                 rubric_path = Path(file_address)
    #                 rubric = doc.new_subdoc(rubric_path)
    task_path = Path(folder/f"task.docx")
    rubric_path = Path(folder/f"rubric.docx")
    task = doc.new_subdoc(task_path)
    rubric = doc.new_subdoc(rubric_path)
    return {
        'task' : task,
        'rubric' : rubric,
    }

def make_cover_sheet(subject: Subject, subject_address:str, doc:DocxTemplate) -> None:
    """
    Iterates through the assignments in the subject and constructs the cover sheet. 
     
    params: 
    subject: The Subject being constructed
    subject_address: the address where the subject data is found
    doc: the doc render for the context
    """
    for assessment in subject.assessments:
        context = build_doc_context(subject_address/assessment, doc)
        if context is None: continue
        print(context)
        output_name = f"{subject.year}_{''.join(subject.semester.split())}_{assessment}_{subject.assessments[assessment]}"
        subject_output = output_dir / f"{subject.unit_name}"
        subject_output.mkdir(parents=True, exist_ok=True)
        file_out = output_dir/ subject_output / f"{output_name}.docx"
        print(f"MAKING: {file_out}")
        doc.render(context)
        doc.save(file_out)

def make_assignments() -> None:
    """
    Makes word doc assignments for each subject and each assessment item
    """
    subjects = get_subjects(subjects_dir)
    for subject_address in subjects:
        doc = DocxTemplate(template)
        subject = config_subject(subject_address)
        make_cover_sheet(subject, subject_address, doc)
        
if __name__ == "__main__":
    make_assignments()