import subprocess

def lint_code(code_block):
    """
    Lints a given code block using flake8.
    Returns a string containing the linting results.
    """
    # Write the code block to a temporary file
    with open('temp_code.py', 'w', encoding='utf-8') as temp_file:
        temp_file.write(code_block)

    # Run flake8 on the temporary file
    result = subprocess.run(['flake8', 'temp_code.py'], capture_output=True, text=True)

    # Return the linting output
    return result.stdout if result.returncode == 0 else result.stderr

def check_code_style(code_blocks):
    """
    Checks the style of a list of code blocks.
    Returns a list of linting results for each block.
    """
    results = []
    for block in code_blocks:
        lint_result = lint_code(block)
        results.append(lint_result)
    return results

# Example usage
if __name__ == "__main__":
    # Sample code blocks - replace with actual extracted code blocks
    sample_code_blocks = [
        "import math\n\nx=2\nprint(x )",  # Sample code block with style issues
        "import math\n\nx = 2\nprint(x)"  # Sample code block without style issues
    ]
    
    style_results = check_code_style(sample_code_blocks)
    for i, result in enumerate(style_results, start=1):
        print(f"Code Block {i} Linting Result:\n{result}\n")
