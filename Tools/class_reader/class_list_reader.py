from dataclasses import dataclass
from pathlib import Path

@dataclass
class Student:
    student_name: str
    student_id: str

def init_my_classes() -> dict:
    '''initialises the dictionary which holds student names and ids

    returns: 
      a dictionary with the desired class lists
    '''
    return {
        '21TNTOS1': [],
        '31TNTOS1': [],
        '41TSTPS1': [],
        '51TNTOS1': [],
        '71TSTPS1': [],
    }

def read_classlist_pdf(file_location: Path) -> list:
    """reads the class list PDF and extracts information into a list

    params: 
      file_location: a Pathlib Path object which highlights the space that the data is held. 

    returns: 
      a list representation of the content in the document
    """
    from pdfminer.high_level import extract_pages
    from pdfminer.layout import LTTextContainer
    out = []
    for page_layout in extract_pages(file_location):
        for element in page_layout:
            if isinstance(element, LTTextContainer):
                out.append(element.get_text())
    return out

def propogate_my_classes(class_list: str, my_classes: dict[str, list] = None) -> dict[str: list[Student]]:
    """ takes the information from the PDF class list and applies it to a dictionary for ease of use

    params: 
      class_list: a string which represents a grouping of text on PDF
      my_classes: a dictionary of my classes (default starts as None and creates itself)

    returns: 
      my_classes: a dictionary of my classes where each class is a list of students
    """
    if my_classes is None:
        my_classes = init_my_classes()

    current_class = None

    for section in class_list:
        section = section.split("\n")
        for group in section:
            match group.split(" / "):
                case [single_var]: 
                    if single_var in my_classes.keys():
                        current_class = single_var
                case [name, student_number]:
                    student = Student(
                        student_name = name, 
                        student_id=student_number[:-2]
                    )
                    my_classes[current_class].append(student)
    return my_classes

def write_classlist_csv(class_list: dict[str, list[Student]], write_location: Path) -> None:
    """ takes a class list and writes to some location 

    params: 
      class_list: a dictionary consisting of a course_key and points to a list of Student objects
      write_location: a pathlib Path object representing the writing location. 
    """
    with open(write_location, 'w') as fp:
        fp.write("class_id, student_name, student_id\n")
        for my_class in class_list:
            for student in class_list[my_class]:
                fp.write(f"{my_class}, {student.student_name}, {student.student_id}\n")

def load_to_drive(src, dest):
    print(type(src), type(dest))
    dest.write_text(src.read_text())
    
    # location_to_copy.write_text(data_to_copy.read_text())


if __name__ == "__main__":
    from datetime import datetime
    from inspect import currentframe, getframeinfo
    filename = getframeinfo(currentframe()).filename
    here = Path(filename).resolve().parent
    data_location = Path.cwd().parent / ".data"
    file_name = f'class_lists.pdf'
    output_file_name = data_location/"class_list.csv"
    class_list = read_classlist_pdf(data_location/file_name)

    class_list.remove('Class\nRoll Class\nTeacher\nRoom\nNo Students\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15\n16\n17\n18\n19\n20\n21\n22\n23\n24\n')

    my_classes = propogate_my_classes(class_list)
    write_classlist_csv(my_classes, output_file_name)
    load_to_drive(output_file_name, Path(f"G:\My Drive\cbrc\data\class_list.csv"))





