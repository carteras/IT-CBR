from lib2to3.pytree import convert
from pathlib import Path
from os import system

def find_dirs(location: Path) -> list[Path]:
    return [f for f in location.iterdir() if f.is_dir()]

def find_files(location: Path) -> list[Path]:
    return [file for file in location.iterdir() if file.is_file()]

def convert_to_markdown() -> None:
    """
    Finds all docx files in output folder and creates markdown versions of them. 
    """
    output_dir = Path.cwd() / "assignments"
    for dir in find_dirs(output_dir):
        for file in find_files(dir):
            md_path = dir/file.parent / f"{file.stem}"
            print(f"FINDING {file}")
            print(f"MAKING: {md_path}.md")
            print("DOING: ",f'pandoc --extract-media "{dir/"media"}" "{file}" -f docx -t markdown-simple_tables-multiline_tables-grid_tables -o "{md_path}.md"')
            system(f'pandoc --extract-media "./" "{file}" -f docx -t markdown-simple_tables-multiline_tables-grid_tables -o "{md_path}.md"')

if __name__ == "__main__":
    convert_to_markdown()