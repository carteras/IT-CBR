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
    course_name: str
    unit_name: str
    year: str
    semester: str
    year11: bool
    year12: bool
    accredited: bool
    tertiary: bool
    assessments: dict()


def get_dirs(dir):
    return [f for f in dir.iterdir() if f.is_dir()]

def get_subjects(subject_directory):
    return get_dirs(subject_directory)

def get_assignment_folders(assignment_directory):
    return get_dirs(assignment_directory)

def get_files_in_folder(folder_to_inspect):
    if not folder_to_inspect.is_dir(): return None
    return [f for f in folder_to_inspect.iterdir() if f.is_file()]

def config_subject(config_location):
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
    return Subject(
        course_name = course_name,
        unit_name = unit_name,
        year = year,
        semester = semester,
        year11 = "True" == year11,
        year12 = "True" == year12,
        accredited = "True" == accredited,
        tertiary = "True" == tertiary,
        assessments=assessments
    )

def make_assignments():
    subjects = get_subjects(subjects_dir)
    task = None
    rubric = None
    for subject_address in subjects:
        doc = DocxTemplate(template)
        subject = config_subject(subject_address)
        for assessment in subject.assessments:
            assignment_files = get_files_in_folder(subject_address / assessment)
            if assignment_files is None: continue
            for file_address in assignment_files:
                if file_address.name == "task.docx":
                    task_path = Path(file_address)
                    task = doc.new_subdoc(task_path)
                elif file_address.name == 'rubric.docx':
                    rubric_path = Path(file_address)
                    rubric = doc.new_subdoc(rubric_path)
            context = {
                'task' : task,
                'rubric' : rubric,
            }
            subject_output = output_dir / f"{subject.unit_name}"
            subject_output.mkdir(parents=True, exist_ok=True)
            output_name = f"{subject.year}_{''.join(subject.semester.split())}_{''.join(subject.course_name.split())}_{''.join(subject.unit_name.split())}_{subject.assessments[assessment]}"
            print(f"MAKING: {output_name}")
            doc.render(context)
            doc.save(output_dir/ subject_output / f"{output_name}.docx")

if __name__ == "__main__":
    make_assignments()