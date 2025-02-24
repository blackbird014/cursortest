import os

def generate_structure(directory, ignore_dirs=None, ignore_files=None, prefix=""):
    if ignore_dirs is None:
        ignore_dirs = {".git", "__pycache__", "node_modules", "venv", ".idea", ".vscode"}
    if ignore_files is None:
        ignore_files = {".DS_Store"}

    structure = []
    entries = sorted(os.listdir(directory))  # Sort for consistency

    for index, entry in enumerate(entries):
        path = os.path.join(directory, entry)
        is_last = index == len(entries) - 1
        connector = "└── " if is_last else "├── "

        if os.path.isdir(path) and entry not in ignore_dirs:
            structure.append(f"{prefix}{connector}{entry}/")
            structure.extend(generate_structure(path, ignore_dirs, ignore_files, prefix + ("    " if is_last else "│   ")))
        elif os.path.isfile(path) and entry not in ignore_files:
            structure.append(f"{prefix}{connector}{entry}")

    return structure

def update_readme(structure, readme_path="README.md"):
    structure_str = "\n".join(structure)
    section_header = "## Project Structure"
    
    # Read the existing README
    if os.path.exists(readme_path):
        with open(readme_path, "r") as file:
            content = file.read()
        
        if section_header in content:
            content = content.split(section_header)[0]  # Remove existing structure section
    else:
        content = "# Project Documentation\n\n"

    # Write the new README with the updated structure
    with open(readme_path, "w") as file:
        file.write(f"{content}\n{section_header}\n```\n{structure_str}\n```\n")

if __name__ == "__main__":
    project_root = os.path.dirname(os.path.abspath(__file__))  # Current directory
    structure = generate_structure(project_root)
    update_readme(structure)
    print("Updated README.md with project structure!")