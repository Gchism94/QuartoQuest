import os

def generate_markdown_report(quality_reports, repo_structure_results, notebook_stats=None, commit_analysis_results=None, other_reports=None, improvement_plan=None):
    """
    Generates a comprehensive Markdown report from various checks.

    :param quality_reports: Dictionary of code quality reports.
    :param repo_structure_results: Dictionary of repository structure results.
    :param notebook_stats: Dictionary of notebook statistics.
    :param commit_analysis_results: Dictionary of commit analysis results.
    :param improvement_plan: List of improvement actions.
    :return: Markdown formatted report as a string.
    """
    report_md = "# Code Review Report\n\n## Summary\nThis report outlines the findings from the automated code review process.\n\n"

    # Include notebook stats if provided
    if notebook_stats:
        report_md += f"- **Total Code Cells**: {notebook_stats.get('total_code_cells', 'N/A')}\n"
        report_md += f"- **Total Markdown Cells**: {notebook_stats.get('total_markdown_cells', 'N/A')}\n\n"

    # Repository Structure Check Results
    report_md += "## Repository Structure Check\n\n"
    report_md += "- **Missing Directories**: " + ", ".join(repo_structure_results.get('missing_directories', [])) + "\n"
    report_md += "- **Unexpected Files**: " + ", ".join(repo_structure_results.get('unexpected_files', [])) + "\n\n"

    # Code Quality Reports
    report_md += "## Code Quality Checks\n\n"
    for block_id, report in quality_reports.items():
        report_md += f"### Code Block {block_id}\n"
        report_md += f"- **Complexity**: {report.get('Complexity', 'N/A')}\n"
        report_md += f"- **Structure**: {report.get('Structure', 'N/A')}\n\n"


    # Commit Analysis Results
    if commit_analysis_results:
        report_md += "## Commit Analysis Results\n\n"
        for key, value in commit_analysis_results.items():
            report_md += f"- **{key.replace('_', ' ').title()}**: {value}\n"
        report_md += "\n"


    # Improvement Plan
    if improvement_plan:
        report_md += "## Improvement Plan\n\n"
        for step in improvement_plan:
            report_md += f"- {step}\n"
        report_md += "\n"

    # Additional Resources
    report_md += "## Additional Resources\n\n"
    report_md += "- [Python Official Documentation](https://docs.python.org/3/)\n"
    report_md += "- [Effective Python: 90 Specific Ways to Write Better Python](https://effectivepython.com/)\n"
    report_md += "- [Stack Overflow](https://stackoverflow.com/) for community support\n\n"

    return report_md

def save_markdown_report(report_content, file_path):
    """Saves the given Markdown report content to a file."""
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(report_content)

# Example usage
if __name__ == "__main__":
    # Mock data for demonstration purposes
    sample_quality_reports = {
        "Code Cell 1": {"Complexity": "Low", "Structure": "Good"},
    }

    sample_repo_structure_results = {"missing_directories": [], "unexpected_files": []}

    sample_notebook_stats = {"total_code_cells": 10, "total_markdown_cells": 5}

    sample_commit_analysis_results = {
        "total_commits": 42,
        "short_message_issues": 5,
        "non_informative_issues": 3,
        "non_conforming_messages": 2
    }

    improvement_plan = [
        "Review and address all code style issues.",
        "Reduce complexity in high-complexity functions.",
    ]

    # Generate the report
    markdown_report = generate_markdown_report(
        sample_quality_reports,
        sample_repo_structure_results,
        sample_notebook_stats,
        sample_commit_analysis_results,
        other_reports,
        improvement_plan
    )