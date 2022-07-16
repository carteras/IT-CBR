from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from docxtpl import DocxTemplate
from inspect import currentframe, getframeinfo
from configparser import ConfigParser
from datetime import datetime
from json import dumps
    
filename = getframeinfo(currentframe()).filename
here = Path(filename).resolve().parent
data = here / ".data"
achievement_standards = data / 'assets'
output = here / "test_output"
assignment_item_templates = here / '.templates'

template_docx = data / "template.docx"
subjects_dir = here / 'subjects'

def get_configs(location):
    file_list = []
    for x in location.iterdir():
        if x.is_file(): file_list.append(x)
        elif x.is_dir(): file_list.extend(get_configs(location / x))
    return file_list

def make_subjects_templates(subjects_cfgs,assignment_item_templates):
    print(subjects_cfgs, assignment_item_templates)
    for subject_cfg in subjects_cfgs:
        subject_folder = subject_cfg.parent
        config = ConfigParser()
        config.read_file(open(subject_cfg))
        for section in config.sections():
            for key in config[section]:
                if key == "year": continue
                if key == 'semester': continue
                for year in config[section]['years'].split(" "):
                    for accreditation in config[section]['accreditation'].split(" "):
                        if key[:2] == 'ai':
                            ai_num = key.upper()
                            ai_type = config[section][key]
                            
                            print(ai_type, subject_folder/section.lower()/ai_num, f"{year}{accreditation}_{ai_type}")
                        # print(key, config[section][key], year, accreditation)


    



subjects_cfgs = get_configs(subjects_dir)
make_subjects_templates(subjects_cfgs, assignment_item_templates)

# for subject in subjects:
#     config_semester(subject, output)

# build templates if not already built



# assignment_items = assignment_items(output)

# for ai in assignment_items:
#     # print(dumps(ai, indent=4))
#     make_assignment_item(ai, template_docx, assignment_item_templates, output)
#     break

