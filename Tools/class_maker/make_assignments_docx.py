from dataclasses import dataclass
from pathlib import Path
from docxtpl import DocxTemplate
from inspect import currentframe, getframeinfo
from configparser import ConfigParser

filename = getframeinfo(currentframe()).filename
here = Path(filename).resolve().parent
data = here / ".data"
achievement_standards = data / 'assets'

template = data / "template.docx"
subjects_dir = here / 'subjects'

print(list(subjects_dir.rglob("*.*")))