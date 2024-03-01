import subprocess
import tempfile

def run_bandit(code_block):
    """
    Runs Bandit on a given code block to identify security vulnerabilities.
    Uses a temporary file to save the code block for Bandit to analyze.
    Returns the Bandit output formatted as a Markdown string.
    """
    with tempfile.NamedTemporaryFile('w+', delete=True, suffix='.py') as tmp:
        tmp.write(code_block)
        tmp.flush()  # Ensure the written content is flushed to disk before running Bandit
        # Adjust Bandit command to use a format that works well with markdown if necessary
        result = subprocess.run(['bandit', '-f', 'txt', '--quiet', tmp.name], capture_output=True, text=True)
    
    # Always apply Markdown formatting to the output, regardless of the content
    if result.stdout:
        output_lines = result.stdout.strip().split('\n')
        markdown_output = '\n- '.join(output_lines)
        return "- " + markdown_output
    else:
        return "No security issues found."

def check_security_vulnerabilities(code_blocks):
    """
    Checks each code block for security vulnerabilities using Bandit.
    Iterates through the code blocks, running Bandit on each, and aggregates the results.
    Returns a Markdown string with results for each code block.
    """
    results = []
    for i, block in enumerate(code_blocks):
        bandit_result = run_bandit(block)
        results.append(f"Code Block {i+1}:\n{bandit_result}")
    return "\n\n".join(results)
