from dataclasses import dataclass
from os import system

@dataclass
class Subject:
    class_name: str
    year: int
    accreditation: str
    assignment_name: str
    location: str
    course: str
    rubric:str

subjects = []

with open("subjects") as file_reader:
    for line in file_reader:
        course, class_name, year, accrediation, assignment_name, location, rubric= line.split(" ")
        subjects.append(
            Subject(
                course=course, 
                class_name=class_name, 
                year=year, 
                accreditation=accrediation, 
                assignment_name=assignment_name,
                location=location,
                rubric=rubric
            )
        )
        
for subject in subjects:
    os_call = (
        f"python assignment_maker.py",
        f"-n {subject.assignment_name}_{subject.year}_{subject.accreditation}",
        f"-y {subject.year} -a {subject.accreditation} -c {subject.course}",
        f"-s {subject.class_name} -d {subject.location} -r {subject.rubric}",
    )
    print(" ".join(os_call))
    system(" ".join(os_call))