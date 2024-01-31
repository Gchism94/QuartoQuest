yaml_header = """
---
title: "Autograder Report"
author: "Autograder System"
date: "`r format(Sys.time(), '%d %B, %Y')`"
format:
  html:
    theme: lux
    toc: true
---
"""

def format_complexity_report(complexity_report):
    """
    Formats the complexity report into a markdown string.
    """
    report_md = "### Complexity Report\n"
    for item in complexity_report:
        report_md += f"- **Function/Method**: {item[0]}, **Complexity**: {item[1]}, **Rank**: {item[2]}\n"
    return report_md

def format_structure_report(structure_report):
    """
    Formats the structure report into a markdown string.
    """
    # This is an example and will vary based on your structure assessment
    return f"### Structure Report\n- {structure_report}\n"

def generate_quarto_report(quality_reports, repo_structure_results, other_reports=None):
    """
    Generates a comprehensive Quarto (.qmd) report from various checks.
    """
    report_qmd = yaml_header
    report_qmd += "# Introduction\n\nThis report presents the results of the autograding process...\n\n"

    # Add Repository Structure Check Results
    report_qmd += "## Repository Structure Check\n"
    report_qmd += "- **Missing Directories**: " + ", ".join(repo_structure_results['missing_directories']) + "\n"
    report_qmd += "- **Unexpected Files**: " + ", ".join(repo_structure_results['unexpected_files']) + "\n\n"

    # Add Code Quality Reports
    report_qmd += "## Code Quality Checks\n"
    for block_id, report in quality_reports.items():
        report_qmd += f"#### {block_id}\n"
        report_qmd += format_complexity_report(report['Complexity']) + "\n"
        report_qmd += format_structure_report(report['Structure']) + "\n"

    # Add other reports if any
    if other_reports:
        report_qmd += "## Other Checks\n"
        # Format other reports (placeholder)

    return report_qmd

def save_quarto_report(report_content, file_path):
    """Saves the given Quarto report content to a file."""
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(report_content)

# Example usage
if __name__ == "__main__":
    sample_quality_reports = {
        "Code Block 1": {
            "Complexity": [("example_function", 2, "B")],
            "Structure": "Good structure and organization."
        },
        # ... other code blocks
    }
    sample_repo_structure_results = {
        "missing_directories": ["data"],
        "unexpected_files": ["temp.txt"]
    }
    # Assuming other_reports is a dictionary of other check results
    quarto_report = generate_quarto_report(sample_quality_reports, sample_repo_structure_results)

    report_file_path = "/autograder/autograder_report.qmd"
    save_quarto_report(quarto_report, report_file_path)

