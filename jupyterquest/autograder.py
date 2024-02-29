import os
import glob
from .repo_structure_check import check_directory_structure
from .code_quality_check import assess_code_quality
from .code_style_check import check_code_style
from .commit_analysis import analyze_commit_messages
from .parse_ipynb import parse_ipynb
from .generate_markdown_report import generate_markdown_report, save_markdown_report

def find_first_ipynb_file(repo_path):
    """Finds the first .ipynb file in the given directory."""
    ipynb_files = glob.glob(os.path.join(repo_path, '*.ipynb'))
    return ipynb_files[0] if ipynb_files else None

def main():
    repo_path = os.getenv('GITHUB_WORKSPACE', '.')

    # 1. Check Repository Structure
    required_directories = ['data', 'images']
    allowed_files_patterns = ['README.md', '.gitignore', 'LICENSE', 'requirements.txt', '*.ipynb', 'hw-0*.ipynb', '*.py', 'check_allowed_files.py',
                              'hw-01.ipynb', 'hw-02.ipynb', 'hw-03.ipynb', 'hw-04.ipynb', 'hw-05.ipynb', 'hw-06.ipynb']
    repo_structure_results = check_directory_structure(
        repo_path, required_directories, allowed_files_patterns
    )
    print("Repository Structure Check Results:", repo_structure_results)

    # 2. Code Quality and Style Checks
    first_ipynb_path = find_first_ipynb_file(repo_path)
    if first_ipynb_path:
        parsed_notebook = parse_ipynb(first_ipynb_path)
        code_blocks = parsed_notebook['code_cells']
        markdown_cells = parsed_notebook['markdown_cells']
    else:
        code_blocks = []
        markdown_cells = []

    code_quality_results = assess_code_quality(code_blocks)
    code_style_results = check_code_style(code_blocks)
    print("Code Quality Results:", code_quality_results)
    print("Code Style Results:", code_style_results)

    # 3. Commit Analysis
    commit_analysis_results = analyze_commit_messages(repo_path)
    print("Commit Analysis Results:", commit_analysis_results)

    # Compile all results into a final Markdown report
    notebook_stats = {
        'total_code_cells': len(code_blocks),
        'total_markdown_cells': len(markdown_cells)
    }

    # Prepare other_reports if needed, or set to None
    other_reports = None  # Adjust as needed based on your specific checks

    final_report = generate_markdown_report(
        quality_reports=code_quality_results,
        repo_structure_results=repo_structure_results,
        notebook_stats=notebook_stats,
        other_reports=other_reports  # Can be None or a dictionary of other reports
    )

    # Save the report as a .md file
    report_file_path = os.path.join(repo_path, 'autograder_report.md')
    save_markdown_report(final_report, report_file_path)

if __name__ == "__main__":
    main()