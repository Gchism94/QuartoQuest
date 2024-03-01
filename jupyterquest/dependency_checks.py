import re
import subprocess

def clean_ansi_sequences(text):
    """
    Removes ANSI escape sequences from a string to clean up the output.
    """
    ansi_escape_pattern = re.compile(r'\x1B[@-_][0-?]*[ -/]*[@-~]')
    return ansi_escape_pattern.sub('', text)

def format_dependency_check_output(output):
    """
    Formats the dependency check output by cleaning ANSI sequences and adjusting Markdown formatting.
    """
    clean_output = clean_ansi_sequences(output)
    # Replace '\n' with Markdown list format, if not empty or default message
    if clean_output and "No dependency issues found." not in clean_output:
        return "- " + clean_output.replace('\n', '\n- ')
    return clean_output

def run_safety():
    """
    Runs Safety to check installed dependencies for known vulnerabilities.
    Returns the Safety output formatted as a Markdown string.
    """
    result = subprocess.run(['safety', 'check', '--full-report'], capture_output=True, text=True)
    output = result.stdout if result.stdout.strip() else "No dependency issues found."
    return format_dependency_check_output(output)

def run_pip_audit():
    """
    Runs pip-audit to check Python environment for dependencies with known vulnerabilities.
    Returns the pip-audit output formatted as a Markdown string.
    """
    result = subprocess.run(['pip-audit'], capture_output=True, text=True)
    output = result.stdout if result.stdout.strip() else "No dependency issues found."
    return format_dependency_check_output(output)

def check_dependencies():
    """
    Checks for known vulnerabilities in dependencies using both Safety and pip-audit.
    Returns a Markdown string with the results of both checks.
    """
    safety_results = run_safety()
    pip_audit_results = run_pip_audit()
    # Formatting the final combined report
    combined_report = f"## Safety Checks\n{safety_results}\n\n## pip-audit Checks\n{pip_audit_results}"
    return combined_report