import subprocess
import tempfile
import json

def run_bandit(code_block):
    """
    Runs Bandit on a single code block.
    """
    with tempfile.NamedTemporaryFile('w+', delete=False, suffix='.py') as tmp:
        tmp.write(code_block)
        tmp.flush()

    command = ['bandit', '-f', 'json', '--quiet', tmp.name]
    result = subprocess.run(command, capture_output=True, text=True)

    try:
        # Delete the temporary file after use
        os.unlink(tmp.name)
    except OSError as e:
        print(f"Error deleting temporary file: {e}")

    if result.stderr:
        return f"Error running Bandit: {result.stderr}"

    try:
        output_json = json.loads(result.stdout)
        if output_json.get('results'):
            markdown_output = "### Security Issues Found\n"
            for issue in output_json['results']:
                markdown_output += f"- **Test ID**: {issue['test_id']}, **Issue**: {issue['issue_text']}\n"
                markdown_output += f"  - **Severity**: {issue['issue_severity']}, **Confidence**: {issue['issue_confidence']}\n"
                markdown_output += f"  - **Remediation**: {issue.get('more_info', 'No specific remediation provided.')}\n"
            return markdown_output
    except json.JSONDecodeError:
        return "Error parsing Bandit output."

    return "No security issues found."

def run_safety_checks():
    """
    Runs safety checks on the project dependencies.
    """
    command = ['safety', 'check', '--json', '--full-report']
    result = subprocess.run(command, capture_output=True, text=True)

    if result.stderr:
        return f"Error running Safety: {result.stderr}"

    try:
        issues = json.loads(result.stdout)
        if issues:
            markdown_output = "### Safety Check Issues Found\n"
            for issue in issues:
                markdown_output += f"- **Package**: {issue['name']} ({issue['spec']})\n"
                markdown_output += f"  **Issue**: {issue['advisory']}\n"
                markdown_output += f"  **Severity**: {issue.get('severity', 'N/A')}, **Vulnerability ID**: {issue.get('vulnerability_id', 'N/A')}\n"
            return markdown_output
    except json.JSONDecodeError:
        return "Error parsing Safety output."

    return "No safety issues found."

def check_security_vulnerabilities(code_blocks):
    """
    Aggregates security checks from Bandit and Safety.
    """
    bandit_results = [run_bandit(block) for block in code_blocks]
    safety_results = run_safety_checks()

    full_report = "\n".join([f"## Code Block {i+1}\n{result}\n" for i, result in enumerate(bandit_results)])
    full_report += "\n" + safety_results

    return full_report