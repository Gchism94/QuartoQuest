import re

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
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    return {
        'code_blocks': extract_code_blocks(content),
        'markdown_text': extract_markdown_text(content)
    }

# Example usage
if __name__ == "__main__":
    file_path = 'example.qmd'  # Replace with the path to your .qmd file
    parsed_content = parse_qmd(file_path)
    print("Code Blocks:", parsed_content['code_blocks'])
    print("Markdown Text:", parsed_content['markdown_text'])
