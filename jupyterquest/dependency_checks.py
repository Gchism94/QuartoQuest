import subprocess

def run_safety():
    """
    Runs Safety to check installed dependencies for known vulnerabilities.
    Returns the Safety output formatted as a Markdown string.
    """
    result = subprocess.run(['safety', 'check', '--full-report'], capture_output=True, text=True)
    output = result.stdout if result.stdout else "No dependency issues found."
    markdown_output = output.replace('\n', '\n- ')
    return markdown_output

def run_pip_audit():
    """
    Runs pip-audit to check Python environment for dependencies with known vulnerabilities.
    Returns the pip-audit output formatted as a Markdown string.
    """
    result = subprocess.run(['pip-audit'], capture_output=True, text=True)
    output = result.stdout if result.stdout else "No dependency issues found."
    markdown_output = output.replace('\n', '\n- ')
    return markdown_output

def check_dependencies():
    """
    Checks for known vulnerabilities in dependencies using both Safety and pip-audit.
    Returns a Markdown string with the results of both checks.
    """
    safety_results = run_safety()
    pip_audit_results = run_pip_audit()
    return f"## Safety Checks\n{safety_results}\n\n## pip-audit Checks\n{pip_audit_results}"