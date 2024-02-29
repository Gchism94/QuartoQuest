import json
import sys
import os

def extract_code_cells(nb_content):
    """
    Extracts code cells from the Jupyter notebook content.
    Returns a list of strings, where each string represents the source code of a code cell.
    """
    code_cells = [''.join(cell['source']) for cell in nb_content['cells'] if cell['cell_type'] == 'code']
    return code_cells

def extract_markdown_cells(nb_content):
    """
    Extracts markdown cells from the Jupyter notebook content.
    Returns a list of strings, where each string represents the content of a markdown cell.
    """
    markdown_cells = [''.join(cell['source']) for cell in nb_content['cells'] if cell['cell_type'] == 'markdown']
    return markdown_cells

def parse_ipynb(file_path):
    """
    Parses the .ipynb file and extracts code cells and markdown cells.
    Returns a dictionary with extracted content.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            nb_content = json.load(file)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None

    return {
        'code_cells': extract_code_cells(nb_content),
        'markdown_cells': extract_markdown_cells(nb_content)
    }

if __name__ == "__main__":
    # Dynamically determine the .ipynb file path or take it from command line arguments
    file_path = sys.argv[1] if len(sys.argv) > 1 else '/autograder/example.ipynb'
    
    # Ensure the file exists before proceeding
    if not os.path.exists(file_path):
        print(f"The specified file does not exist: {file_path}")
        sys.exit(1)

    parsed_content = parse_ipynb(file_path)
    if parsed_content:
        print("Code Cells:", parsed_content['code_cells'])
        print("Markdown Cells:", parsed_content['markdown_cells'])