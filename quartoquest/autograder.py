import os
import glob
from . import repo_structure_check
from . import code_quality_check
from . import code_style_check
from . import commit_analysis
from . import parse_qmd
from .generate_markdown_report import generate_markdown_report, save_markdown_report

def find_first_qmd_file(repo_path):
    """Finds the first .qmd file in the given directory."""
    qmd_files = glob.glob(os.path.join(repo_path, '*.qmd'))
    return qmd_files[0] if qmd_files else None

def main():
    repo_path = os.getenv('GITHUB_WORKSPACE', '.')

    # 1. Check Repository Structure
    repo_structure_results = repo_structure_check.check_directory_structure(
        repo_path, ['data'], ['README.md', '.gitignore', 'LICENSE', 'requirements.txt']
    )
    print("Repository Structure Check Results:", repo_structure_results)

    # 2. Code Quality and Style Checks
    # Assuming you have a way to get code_blocks (list of strings)
    code_blocks = []  # Replace with actual code blocks
    code_quality_results = code_quality_check.assess_code_quality(code_blocks)
    code_style_results = code_style_check.check_code_style(code_blocks)
    print("Code Quality Results:", code_quality_results)
    print("Code Style Results:", code_style_results)

    # 3. Commit Analysis
    commit_analysis_results = commit_analysis.analyze_commit_messages(repo_path)
    print("Commit Analysis Results:", commit_analysis_results)

    # 4. Parse QMD File
    qmd_file_path = find_first_qmd_file(repo_path)
    parsed_qmd = parse_qmd.parse_qmd(qmd_file_path) if qmd_file_path else None
    print("Parsed QMD Content:", parsed_qmd)

    # Compile all results into a final Markdown report
    final_report = generate_markdown_report(
        code_quality_results,
        repo_structure_results,
        {
            "Code Style Results": code_style_results,
            "Commit Analysis Results": commit_analysis_results,
            "Parsed QMD Content": parsed_qmd
        }
    )

    # Save the report as a .md file
    report_file_path = 'autograder_report.md'  # Updated file extension
    save_markdown_report(final_report, report_file_path)  # Updated function call

if __name__ == "__main__":
    main()
