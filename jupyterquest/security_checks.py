import subprocess
import tempfile

def run_bandit(code_block):
    """
    Runs Bandit on a given code block to identify security vulnerabilities.
    Returns the Bandit output formatted as a Markdown string.
    """
    with tempfile.NamedTemporaryFile('w+', delete=False, suffix='.py') as tmp:
        tmp.write(code_block)
        tmp.flush()
        result = subprocess.run(['bandit', '-f', 'custom', '--quiet', tmp.name], capture_output=True, text=True)
    # Format result for Markdown (e.g., bullet points)
    output = result.stdout if result.stdout else "No security issues found."
    markdown_output = "- " + output.replace('\n', '\n- ') if output != "No security issues found." else output
    return markdown_output

def check_security_vulnerabilities(code_blocks):
    """
    Checks each code block for security vulnerabilities using Bandit.
    Returns a Markdown string with results for each code block.
    """
    results = [f"Code Block {i+1}:\n- {run_bandit(block)}" for i, block in enumerate(code_blocks)]
    return "\n".join(results)