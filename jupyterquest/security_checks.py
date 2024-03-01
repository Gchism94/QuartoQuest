import subprocess
import tempfile
import json

def run_bandit(code_block):
    """
    Runs Bandit on a given code block to identify security vulnerabilities.
    Uses a temporary file to save the code block for Bandit to analyze.
    Returns detailed Bandit output formatted as a Markdown string.
    """
    with tempfile.NamedTemporaryFile('w+', delete=True, suffix='.py') as tmp:
        tmp.write(code_block)
        tmp.flush()  # Ensure the written content is flushed to disk before running Bandit
        # Run Bandit with JSON format for detailed output
        result = subprocess.run(['bandit', '-f', 'json', '--quiet', tmp.name], capture_output=True, text=True)
    
    if result.stdout:
        # Parse JSON output for detailed reporting
        try:
            output_json = json.loads(result.stdout)
            if output_json.get('results'):  # Check if there are any issues found
                markdown_output = "### Security Issues Found\n"
                for issue in output_json['results']:
                    markdown_output += f"- **Test ID**: {issue['test_id']}, **Issue**: {issue['issue_text']}\n"
                    markdown_output += f"  - **Severity**: {issue['issue_severity']}, **Confidence**: {issue['issue_confidence']}\n"
                    markdown_output += f"  - **Remediation**: {issue.get('more_info', 'No specific remediation provided.')}\n"
                return markdown_output
            else:
                return "No security issues found."
        except json.JSONDecodeError:
            return "Error parsing Bandit output."
    elif result.stderr:
        # Handle potential errors from Bandit more explicitly
        return f"Error running Bandit: {result.stderr.strip()}"
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
        results.append(f"## Code Block {i+1}\n{bandit_result}\n")
    return "\n".join(results)