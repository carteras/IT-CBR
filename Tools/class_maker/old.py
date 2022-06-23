
# def config_semester(config_file, output_dir):
#     # TODO split this up one function to generate configs second to write them
#     config = ConfigParser()
#     config.read_file(open(config_file))
#     delivered_year = config.get("DEFAULT", "year")
#     delivered_semester = config.get("DEFAULT", "semester")
#     semester_dir = output_dir/ delivered_year /delivered_semester
#     semester_dir.mkdir(parents=True, exist_ok=True)
#     for section in config.sections():
#         subject_dir = semester_dir / section.lower()
#         subject_dir.mkdir(parents=True, exist_ok=True)
#         subject_cfg = ConfigParser()
#         subject_cfg['DEFAULT'] = {}

#         for key in config[section]:
#             if key == "year": continue
#             if key == 'semester': continue
#             subject_cfg['DEFAULT'][key] = config.get(section, key)

#         with open(f"{subject_dir}/config.ini", 'w') as configfile:
#             subject_cfg.write(configfile)

# def get_assignment_items(cfg_location):
#     out = {}
#     location = cfg_location.parent
#     config = ConfigParser()
#     config.read_file(open(cfg_location))
#     years = config.get("DEFAULT", 'years').split(" ")
#     accreditations = config.get('DEFAULT', 'accreditation').split(" ")
#     for year in years:
#         for accreditation in accreditations:
#             for key in config['DEFAULT']:
#                 if key == "years": continue
#                 if key == "accreditation": continue
#                 ai = location / key.upper()                
#                 out[f"{key.upper()}{year}{accreditation}"] = {
#                     "type": config.get('DEFAULT', key),
#                     "year": year,
#                     "accreditation": accreditation,
#                     "ai": key[-1],
#                     "location": str(ai),
#                 }
#     return out



# def assignment_items(output):
#     out = []
#     for subject in get_configs(output):
#         subject_assignment_items = get_assignment_items(subject)
#         out.append(subject_assignment_items)
#     return out


# def make_assignment_item(assignment_item, template_docx, assignment_item_templates, output):
#     print(template_docx, assignment_item_templates, output)
#     # print(dumps(assignment_item, indent=2 ))
#     for key in assignment_item:
#         item_type = assignment_item[key]['type']
#         year = assignment_item[key]['year']
#         accreditation = assignment_item[key]['accreditation']
#         ai = assignment_item[key]['ai']
#         location = Path(assignment_item[key]['location'])
#         print(item_type, year, accreditation, ai, location)
#         print(assignment_item_templates / item_type)
        # docx_name = f"{assignment_item[key]['year']}_{assignment_item[key]['accreditation']}_{assignment_item[key]['type']}.docx"
        # file_path = Path(assignment_item[key]['location']) / docx_name