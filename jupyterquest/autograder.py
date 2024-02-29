import os
import glob
from . import check_directory_structure
from . import assess_code_quality
from . import check_code_style
from . import analyze_commit_messages
from . import parse_ipynb  # Updated to reflect correct function name for parsing .ipynb files
from . import generate_markdown_report, save_markdown_report

def find_first_ipynb_file(repo_path):
    """Finds the first .ipynb file in the given directory."""
    ipynb_files = glob.glob(os.path.join(repo_path, '*.ipynb'))
    return ipynb_files[0] if ipynb_files else None

def main():
    repo_path = os.getenv('GITHUB_WORKSPACE', '.')

    # 1. Check Repository Structure
    required_directories = ['data', 'images']  # Assuming these directories are required
    allowed_files_patterns = ['README.md', '.gitignore', 'LICENSE', 'requirements.txt', '*.ipynb']  # Updated patterns
    repo_structure_results = check_directory_structure(
        repo_path, required_directories, allowed_files_patterns
    )
    print("Repository Structure Check Results:", repo_structure_results)

    # 2. Code Quality and Style Checks
    # Assuming you have a way to get code_blocks (list of strings) from .ipynb files
    first_ipynb_path = find_first_ipynb_file(repo_path)
    code_blocks = parse_ipynb(first_ipynb_path)['code_cells'] if first_ipynb_path else []
    code_quality_results = assess_code_quality(code_blocks)
    code_style_results = check_code_style(code_blocks)
    print("Code Quality Results:", code_quality_results)
    print("Code Style Results:", code_style_results)

    # 3. Commit Analysis
    commit_analysis_results = analyze_commit_messages(repo_path)
    print("Commit Analysis Results:", commit_analysis_results)

    # 4. Parse .ipynb File (if needed separately)
    # If additional information from the .ipynb file is needed, parse as required

    # Compile all results into a final Markdown report
    final_report = generate_markdown_report(
        code_quality_results,
        repo_structure_results,
        {
            "Code Style Results": code_style_results,
            "Commit Analysis Results": commit_analysis_results,
            # "Parsed .ipynb Content": parsed_content  # Include this if there's specific content to report
        }
    )

    # Save the report as a .md file
    report_file_path = os.path.join(repo_path, 'autograder_report.md')  # Ensure it saves in the correct directory
    save_markdown_report(final_report, report_file_path)

if __name__ == "__main__":
    main()