import subprocess
import tempfile

def lint_code(code_block):
    """
    Lints a given code block using flake8.
    Utilizes a temporary file for the code block, ensuring cleanup after linting.
    Returns a string containing the linting results.
    """
    with tempfile.NamedTemporaryFile(mode='w+', encoding='utf-8', suffix='.py', delete=True) as temp_file:
        temp_file.write(code_block)
        temp_file.flush()  # Ensure data is written to disk
        result = subprocess.run(['flake8', temp_file.name], capture_output=True, text=True)

    # Process and return the linting output
    return result.stdout if result.stdout else result.stderr if result.stderr else "No issues found."

def check_code_style(code_blocks):
    """
    Checks the style of a list of code blocks using flake8.
    Returns a list of linting results for each block.
    """
    results = []
    for block in code_blocks:
        lint_result = lint_code(block)
        results.append(lint_result)
    return results

# Example usage
if __name__ == "__main__":
    sample_code_blocks = [
        "import math\n\nx=2\nprint(x )",  # Sample code block with style issues
        "import math\n\nx = 2\nprint(x)"  # Sample code block without style issues
    ]
    
    style_results = check_code_style(sample_code_blocks)
    for i, result in enumerate(style_results, start=1):
        print(f"Code Block {i} Linting Result:\n{result}\n")
