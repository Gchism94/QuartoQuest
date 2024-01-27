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

def generate_markdown_report(quality_reports, repo_structure_results, other_reports=None):
    """
    Generates a comprehensive markdown report from various checks.
    """
    report_md = "# Autograder Report\n\n"

    # Add Repository Structure Check Results
    report_md += "## Repository Structure Check\n"
    report_md += "- **Missing Directories**: " + ", ".join(repo_structure_results['missing_directories']) + "\n"
    report_md += "- **Unexpected Files**: " + ", ".join(repo_structure_results['unexpected_files']) + "\n\n"

    # Add Code Quality Reports
    report_md += "## Code Quality Checks\n"
    for block_id, report in quality_reports.items():
        report_md += f"#### {block_id}\n"
        report_md += format_complexity_report(report['Complexity']) + "\n"
        report_md += format_structure_report(report['Structure']) + "\n"

    # Add other reports if any
    if other_reports:
        report_md += "## Other Checks\n"
        # Format other reports (placeholder)

    return report_md

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
    markdown_report = generate_markdown_report(sample_quality_reports, sample_repo_structure_results)
    print(markdown_report)
