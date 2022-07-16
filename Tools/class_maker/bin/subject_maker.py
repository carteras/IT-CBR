from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from docxtpl import DocxTemplate
from inspect import currentframe, getframeinfo
from configparser import ConfigParser
from datetime import datetime
from json import dumps

# import typing
# typing.Union[str, Path]
    
filename = getframeinfo(currentframe()).filename
home = Path(filename).resolve().parent.parent

data = home / '.data'
achievement_standards = data / 'assets'
output = home / "test_output"
assignment_item_templates = home / '.templates'

template_docx = data / "template.docx"
subjects_dir = home / 'subjects'


def get_configs(location: Path) -> list[Path]:
    file_list = []
    for x in location.iterdir():
        if x.is_file(): file_list.append(x)
        elif x.is_dir(): file_list.extend(get_configs(location / x))
    return file_list

def get_unfinished_configs(cfgs: Path) -> list[Path]:
    out = []
    for cfg in cfgs:
        config = ConfigParser()
        config.read_file(open(cfg))
        try:
            print(config["DEFAULT"]['updated'])
            # TODO test to see if file update is more recent than the last update time
        except KeyError:
            out.append(cfg) 
    return out

def construct_subject(course_cfg: Path, ai_location: Path):
    print(course_cfg)
    print(ai_location)
    config = ConfigParser()
    config.read_file(open(course_cfg))
    for section in config.sections():
        for key in config[section]:
            print(section, key, config[section][key])

if __name__ == "__main__":
    courses_cfg = get_unfinished_configs(get_configs(subjects_dir)) 
    for cfg in courses_cfg:
        construct_subject(cfg, assignment_item_templates)
    
