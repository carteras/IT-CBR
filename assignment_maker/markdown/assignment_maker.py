from dataclasses import dataclass
from pathlib import Path
from argparse import ArgumentParser

class FileAddress:
    def __init__(self, folder, name):
        self.address = folder / name


path = Path.cwd()

templates = path / './templates'
output = path / "output"

achievement_standard_image = None
rubric = None


file_addresses = {
    'task' : FileAddress(templates, '01_task.md'),
    'rubric_summary' : FileAddress(templates, '02_rubric_summary.md'),
    'scoring_notes' : FileAddress(templates, '03_scoring_notes.md'),
    'achievement_standards' : FileAddress(templates, '04_achievement_standards.md'),
    'higher_order_thinking' : FileAddress(templates, '05_higher_order_thinking.md'),
    'rubric' : FileAddress(templates, '06_rubric.md'),
    'competencies' : FileAddress(templates, '07_competencies.md'),
}

assignment_title = 'assignment'


parser = ArgumentParser()
parser.add_argument('-n', "--name", help="the name of the assignment")
parser.add_argument('-s', '--save_location', help="The folder where output will go")
parser.add_argument('-d', '--data', help='the folder where custom elements are found')
parser.add_argument('-y', "--year", help="What year is this assignment for?")
parser.add_argument('-a', '--acc', help="what accreditation level is this assignment for?")
parser.add_argument('-c', '--course', help="which course achievement frame this uses")
parser.add_argument('-r', '--rubric', help="the name of the rubric file")
args = parser.parse_args()
print(args)
if args.name: 
    assignment_title = args.name
if args.save_location:
    output = output / args.save_location
if args.data: 
    data_path = path / args.data
    for f in list(data_path.iterdir()):
        if f.is_file:
            file_addresses[f.stem.split('_')[1]] = FileAddress(data_path, f.name)

if args.rubric: 
    file_addresses['rubric'] = FileAddress(data_path, args.rubric)

if args.year and args.acc and args.course:
    print(args.year, args.acc, args.course, "---------====--------")
    file_addresses["achievement_standards"] = FileAddress(templates, f'04_achievement_standards_{args.course}_{args.year}_{args.acc}.md')
    achievement_standard_image = f"{args.course}_{args.year}_{args.acc}.png"
    # rubric = f"06_rubric.html"
    # print(data_path, rubric)
    # file_addresses['rubric'] = FileAddress(data_path, rubric)


    

assignment_name = f"{assignment_title}.md"
output.mkdir(parents=True, exist_ok=True)

for key in file_addresses:
    print(key, file_addresses[key].address)

with open(output/assignment_name, 'w') as file_writer:
    for assignment_part in file_addresses:
        file_ady = file_addresses[assignment_part]
        with open(file_addresses[assignment_part].address, 'r', encoding='utf8')  as file_reader:
            for line in file_reader:
                file_writer.write(line)
        
    if achievement_standard_image:
        src = templates / "assets" / achievement_standard_image
        dest_folder = output / 'assets'
        dest_folder.mkdir(parents=True, exist_ok=True)
        dest =  dest_folder / achievement_standard_image
        dest.write_bytes(src.read_bytes())

    # if rubric:
    #     src = templates / "assets" / rubric
    #     dest_folder = output / 'assets'
    #     dest_folder.mkdir(parents=True, exist_ok=True)
    #     dest =  dest_folder / rubric
    #     dest.write_bytes(src.read_bytes())




