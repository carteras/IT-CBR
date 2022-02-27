import datetime
from collections import namedtuple
from pathlib import Path
import shutil
import pandas as pd
from docxtpl import DocxTemplate
current_path = Path("tools/classroom_documentation_tool/")
output_path = Path("tools/classroom_documentation_tool/out/")
output_path.mkdir(parents=True, exist_ok=True)
template = 'template_test.docx'
unit_goals = 'unit_goals_digital_technology_2020_2024.docx'


# template_unit_outline = 'template_unit_outline.docx'
# template_assignment_item = 'template_assignment_item.docx'
courses = 'courses.csv'  #tools\classroom_documentation_tool\courses.csv
assignments = 'assignments.csv'
week_by_week = 'week_by_week.csv'
year = 2021
semester = 1
term = 1

unit_goals = DocxTemplate(current_path / unit_goals)

context = {
    'test': unit_goals
}
new_file = 'foo_out.docx'

shutil.copy(current_path/template, output_path/new_file)

doc = DocxTemplate(output_path / new_file)
doc.render(context)
doc.save(output_path/new_file)


# doc = DocxTemplate(output_path / "foo_out.docx")
# doc.render(context)
# doc.save(output_path/"foo_out.docx")