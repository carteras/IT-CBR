from pathlib import Path
import shutil

def make_lessons(topic_path, framework, cookbook):
    try:
        (topic_path.parent / 'challenges').mkdir(parents=True, exist_ok=False)
    except: 
        pass

    current_path = None
    child_path = None
    subchild_path = None
    what_path = None
    with open(framework) as fp:
        for line in fp:
            line = line.rstrip()
            line = line.replace(" ", "_")
            line = line.replace("*", "_")
            line = line.lower()
            if len(line) == 0: continue
            if line[:6] == "______":
                subchild_path = child_path / line[6:]
                subchild_path.mkdir(parents=True, exist_ok=False)
                try:
                    shutil.copy(cookbook, subchild_path/f"{subchild_path.name}_cookbook.md")
                except: 
                    pass
            elif line[:4] == '____':
                child_path = what_path / line[4:]
                child_path.mkdir(parents=True, exist_ok=False)
                try:
                    shutil.copy(cookbook, child_path/f"{child_path.name}_cookbook.md")
                except: 
                    pass
            elif line[:2] == "__":
                what_path = current_path/line[2:]
                what_path.mkdir(parents=True, exist_ok=False)
                try:
                    shutil.copy(cookbook, what_path/f"{what_path.name}_cookbook.md")
                except: 
                    pass
            elif line[0] not in "__":
                current_path = topic_path / line
                current_path.mkdir(parents=True, exist_ok=False)
                try:
                    shutil.copy(cookbook, current_path/f"{current_path.name}_cookbook.md")
                except: 
                    pass

path = Path().cwd() / "learning"

path_python = path / 'python' / "micro_lessons"
path_c = path / 'c' / "micro_lessons"
path_arduino = path / 'arduino' / "micro_lessons"
path_packet_tracer = path / 'packet_tracer' / "micro_lessons"

python_framework = path / 'framework_python.md'
c_framework = path / 'framework_c.md'
arduino_framework = path / "framework_arduino.md"
packet_tracer_framework = path / 'framework_packet_tracer.md'

index = path / 'test' / 'readme.md'

path_cookbook = path / 'test' / 'micro_lessons' / 'mastery_area' / 'template_cookbook.md'

make_lessons(path_python, python_framework, path_cookbook)
make_lessons(path_c, c_framework, path_cookbook)
make_lessons(path_arduino, arduino_framework, path_cookbook)

# current_path = None
# child_path = None
# subchild_path = None
# what_path = None
# with open(python_framework) as fp:
#     for line in fp:
#         line = line.rstrip()
#         line = line.replace(" ", "_")
#         line = line.replace("*", "_")
#         line = line.lower()
#         if len(line) == 0: continue
        
        
#         if line[:6] == "______":
#             subchild_path = child_path / line[6:]
#             subchild_path.mkdir(parents=True, exist_ok=True)
#             shutil.copy(path_cookbook, subchild_path/f"{subchild_path.name}_cookbook.md")
#         elif line[:4] == '____':
#             child_path = what_path / line[4:]
#             print(child_path)
#             child_path.mkdir(parents=True, exist_ok=True)
#             shutil.copy(path_cookbook, child_path/f"{child_path.name}_cookbook.md")
#         elif line[:2] == "__":
#             what_path = current_path/line[2:]
#             what_path.mkdir(parents=True, exist_ok=True)
#             shutil.copy(path_cookbook, what_path/f"{what_path.name}_cookbook.md")
#         elif line[0] not in "__":
#             current_path = path_python / line
#             current_path.mkdir(parents=True, exist_ok=True)
#             shutil.copy(path_cookbook, current_path/f"{current_path.name}_cookbook.md")
