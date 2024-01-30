import re
import sys
import os

def extract_code_blocks(qmd_content):
    """
    Extracts code blocks from the qmd content.
    Returns a list of code blocks.
    """
    code_blocks = re.findall(r'```(.*?)```', qmd_content, re.DOTALL)
    return code_blocks

def extract_markdown_text(qmd_content):
    """
    Extracts markdown text, excluding code blocks.
    Returns the markdown text as a string.
    """
    markdown_text = re.sub(r'```.*?```', '', qmd_content, flags=re.DOTALL)
    return markdown_text.strip()

def parse_qmd(file_path):
    """
    Parses the .qmd file and extracts code blocks and markdown text.
    Returns a dictionary with extracted content.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None

    return {
        'code_blocks': extract_code_blocks(content),
        'markdown_text': extract_markdown_text(content)
    }

if __name__ == "__main__":
    # Dynamically determine the .qmd file path or take it from command line arguments
    file_path = sys.argv[1] if len(sys.argv) > 1 else '/autograder/example.qmd'
    
    # Ensure the file exists before proceeding
    if not os.path.exists(file_path):
        print(f"The specified file does not exist: {file_path}")
        sys.exit(1)

    parsed_content = parse_qmd(file_path)
    if parsed_content:
        print("Code Blocks:", parsed_content['code_blocks'])
        print("Markdown Text:", parsed_content['markdown_text'])
