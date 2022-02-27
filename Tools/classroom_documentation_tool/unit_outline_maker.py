import datetime
from collections import namedtuple
from pathlib import Path
import shutil
import pandas as pd
from docxtpl import DocxTemplate
current_path = Path("tools/classroom_documentation_tool/")
output_path = Path("tools/classroom_documentation_tool/out/")
output_path.mkdir(parents=True, exist_ok=True)
template_unit_outline = 'template_unit_outline.docx'
template_assignment_item = 'template_assignment_item.docx'
courses = 'courses.csv'  #tools\classroom_documentation_tool\courses.csv
assignments = 'assignments.csv'
week_by_week = 'week_by_week.csv'
year = 2021
semester = 1
term = 1


start_date = datetime.datetime.strptime("01/02/2020", "%d/%m/%Y")

assignment = namedtuple('assignment', ['ai_name', 'ai_percent', 'ai_issue', 'ai_due', 'ai_description', 'ai_assignment_team_status'])

class Unit:
    def __init__(self, **kwargs):
        self.course_name = kwargs['course_name']
        self.unit_name = kwargs['unit_name']
        self.course_number_a = kwargs['course_number_a']
        self.course_number_t = kwargs['course_number_t']
        self.unit_number_a = kwargs['unit_number_a']
        self.unit_number_t = kwargs['unit_number_t']
        self.bsss_location = kwargs['bsss_location']
        self.semester = kwargs['semester']
        self.year = kwargs['year']
        self.term_a = kwargs['term']
        self.term_b = self.term_a + 1
        self.week_by_week = []
        self.assignments = []

    def context_unit_outline(self):
        out = {
            'semester':self.semester,
            'year':self.year,
            'course_name':self.course_name,
            'unit_name':self.unit_name,
            'a_ccode':self.course_number_a,
            't_ccode':self.course_number_t,
            'a_ucode':self.unit_number_a,
            't_ucode':self.unit_number_t,
            'bsss_url':self.bsss_location
        }

        for i, assignment in enumerate(self.assignments):
            out[f'ai_name_{i}'] = assignment.ai_name
            out[f'ai_percent_{i}'] = assignment.ai_percent
            out[f'ai_issue_{i}'] = assignment.ai_issue
            out[f'ai_due_{i}'] = assignment.ai_due
            out[f'ai_description_{i}'] = assignment.ai_description

        
        return out

    def context_assignments(self):
        
        return {}

units = {}   
courses_df = pd.read_csv('tools/classroom_documentation_tool/courses.csv')
assignments_df = pd.read_csv('tools/classroom_documentation_tool/assignments.csv')
week_by_week_df = pd.read_csv('tools/classroom_documentation_tool/week_by_week.csv')
# print(courses_df)

for index, row in courses_df.iterrows():
    # print(row)
    unit = Unit(
        course_name = row['course_name'],
        unit_name = row['unit_name'],
        course_number_a = row['course_number_a'],
        course_number_t = row['course_number_t'],
        unit_number_a = row['unit_number_a'],
        unit_number_t = row['unit_number_t'],
        bsss_location = row['bsss_location'],
        semester = semester,
        year = year,
        term = term
    )
    units[row['unit_name']] = unit
for index, row in assignments_df.iterrows():
    units[row['unit_name']].assignments.append(
        assignment(
            ai_name=row['ai_name'],
            ai_percent=row['ai_percent'],
            ai_issue=row['ai_issue'],
            ai_due=row['ai_due'],
            ai_description=row['ai_description'],
            ai_assignment_team_status = row['ai_assignment_team_status']
        )
    )
for unit in units:
    context = units[unit].context_unit_outline()
    new_file = f'Unit_Outline_{units[unit].course_name}_{units[unit].unit_name}_{units[unit].year}_S{units[unit].semester}.docx'
    shutil.copy(current_path / template_unit_outline, output_path / new_file)
    doc = DocxTemplate(output_path / new_file)
    doc.render(context)
    doc.save(output_path / new_file)


for unit in units:
    for assignment in units[unit].assignments:
        context_assignment_item = {
            'course_name': units[unit].course_name,
            'unit_name':units[unit].unit_name,
            'semester': units[unit].semester,
            'year': units[unit].year,
            'a_ccode': units[unit].course_number_a,
            't_ccode': units[unit].course_number_a,
            'a_ucode': units[unit].unit_number_a,
            't_ucode': units[unit].unit_number_t,
            'ai_name':assignment.ai_name,
            'ai_issue': assignment.ai_issue,
            'ai_due':assignment.ai_due,
            'ai_percent':assignment.ai_percent,
            'ai_description':assignment.ai_description,
            'ai_team_status':assignment.ai_assignment_team_status 
        }
        print(assignment.ai_name, assignment.ai_assignment_team_status)
        new_file = f'Assignment_Item_{units[unit].course_name}_{units[unit].unit_name}_{assignment.ai_name}_{units[unit].year}_S{units[unit].semester}.docx'
        shutil.copy(current_path / template_assignment_item, output_path / new_file)
        doc = DocxTemplate(output_path / new_file)
        doc.render(context_assignment_item)
        doc.save(output_path / new_file)