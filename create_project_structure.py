#!/usr/bin/env python3
"""
Project Structure Generator for ssh_tools

This script automates the creation of the ssh_tools project structure.
It validates that the script is located in a folder named 'ssh_tools' and
creates the necessary directory layout and files for the project.

Functions:
    check_folder_empty(): Validates that only expected files exist in the root directory
    create_project_structure(): Creates the complete project directory structure

Expected structure:
    ssh_tools/
    ├── pyproject.toml
    └── src/
        └── ssh_tools/
            ├── __init__.py
            ├── __about__.py
            └── cli/
                └── __init__.py
"""

from pathlib import Path

def check_folder_empty():
    """Check if folder contains only this file and README.md"""
    current_dir = Path(__file__).parent
    allowed_files = {'create_project_structure.py', 'README.md','.gitignore','LICENSE'}

    files_in_dir = {f.name for f in current_dir.iterdir() if f.is_file()}

    if files_in_dir == allowed_files or files_in_dir <= allowed_files:
        print("✓ Folder is clean (only expected files present)")
        return True
    else:
        unexpected = files_in_dir - allowed_files
        print(f"✗ Unexpected files found: {unexpected}")
        return False


def create_project_structure():
    """Create the ssh_tools project structure"""
    current_dir = Path(__file__).parent

    # Check if parent folder name is ssh_tools
    if current_dir.name != 'ssh_tools':
        print(f"✗ Error: Current folder is '{current_dir.name}', expected 'ssh_tools'")
        return False

    # Define structure
    structure = {
        'pyproject.toml': '',
        'src/ssh_tools/__init__.py': '',
        'src/ssh_tools/__about__.py': '',
        'src/ssh_tools/cli/__init__.py': '',
    }

    try:
        for file_path, content in structure.items():
            full_path = current_dir / file_path
            full_path.parent.mkdir(parents=True, exist_ok=True)
            if not full_path.exists():
                full_path.write_text(content)
                print(f"✓ Created: {file_path}")
            else:
                print(f"→ Already exists: {file_path}")

        print("\n✓ Project structure created successfully!")
        return True
    except Exception as e:
        print(f"✗ Error creating structure: {e}")
        return False


if __name__ == '__main__':
    check_folder_empty()
    create_project_structure()
