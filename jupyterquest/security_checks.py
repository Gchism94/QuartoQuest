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
        result = subprocess.run(['bandit', '-f', 'json', '--quiet', tmp.name], capture_output=True, text=True)
    
    if result.stdout:
        try:
            output_json = json.loads(result.stdout)
            if output_json.get('results'):
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
        return f"Error running Bandit: {result.stderr.strip()}"
    else:
        return "No security issues found."

def run_safety_checks():
    """
    Runs safety checks on the project dependencies and returns formatted output.
    """
    try:
        result = subprocess.run(['safety', 'check', '--json', '--full-report'], capture_output=True, text=True)
        if result.returncode == 0 and result.stdout:
            issues = json.loads(result.stdout)
            if issues:
                markdown_output = "### Safety Check Issues Found\n"
                for issue in issues:
                    markdown_output += f"- **Package**: {issue['name']} ({issue['spec']})\n"
                    markdown_output += f"  **Issue**: {issue['advisory']}\n"
                    markdown_output += f"  **Severity**: {issue.get('severity', 'N/A')}, **Vulnerability ID**: {issue.get('vulnerability_id', 'N/A')}\n\n"
                return markdown_output
            else:
                return "No safety issues found."
        else:
            return "Safety checks did not find any issues."
    except json.JSONDecodeError:
        return "Error parsing safety output."
    except Exception as e:
        return f"Error running safety checks: {str(e)}"

def check_security_vulnerabilities(code_blocks):
    """
    Checks each code block for security vulnerabilities using Bandit and runs safety checks.
    Iterates through the code blocks, running Bandit on each, and aggregates the results.
    Then, runs safety checks to analyze project dependencies for vulnerabilities.
    Returns a Markdown string with results for each code block and the safety check summary.
    """
    bandit_results = []
    for i, block in enumerate(code_blocks):
        bandit_result = run_bandit(block)
        bandit_results.append(f"## Code Block {i+1}\n{bandit_result}\n")
    
    safety_results = run_safety_checks()
    
    return "\n".join(bandit_results) + "\n" + safety_results