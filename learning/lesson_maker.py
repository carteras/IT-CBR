from pathlib import Path
import shutil

path = Path().cwd() / "learning"
path_python = path / 'python' / "micro_lessons"

path_cookbook = path / 'test' / 'micro_lessons' / 'mastery_area' / 'template_cookbook.md'
# cookbook = []
# with open(path_cookbook) as fp:
#     cookbook = fp.readlines()

current_path = None
child_path = None
subchild_path = None
what_path = None
with open(path / 'framework.md') as fp:
    for line in fp:
        line = line.rstrip()
        line = line.replace(" ", "_")
        line = line.replace("*", "_")
        line = line.lower()
        if len(line) == 0: continue
        
        
        if line[:6] == "______":
            subchild_path = child_path / line[6:]
            subchild_path.mkdir(parents=True, exist_ok=True)
            shutil.copy(path_cookbook, subchild_path/f"{subchild_path.name}_cookbook.md")
        elif line[:4] == '____':
            child_path = what_path / line[4:]
            print(child_path)
            child_path.mkdir(parents=True, exist_ok=True)
            shutil.copy(path_cookbook, child_path/f"{child_path.name}_cookbook.md")
        elif line[:2] == "__":
            what_path = current_path/line[2:]
            what_path.mkdir(parents=True, exist_ok=True)
            shutil.copy(path_cookbook, what_path/f"{what_path.name}_cookbook.md")
        elif line[0] not in "__":
            current_path = path_python / line
            current_path.mkdir(parents=True, exist_ok=True)
            shutil.copy(path_cookbook, current_path/f"{current_path.name}_cookbook.md")
