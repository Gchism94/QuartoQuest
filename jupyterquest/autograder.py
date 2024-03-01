import os
import glob
import markdown
from markdown.extensions.tables import TableExtension
from .repo_structure_check import check_directory_structure
from .code_quality_check import assess_code_quality
from .code_style_check import check_code_style
from .security_checks import check_security_vulnerabilities
from .dependency_checks import check_dependencies
from .commit_analysis import analyze_commit_messages
from .parse_ipynb import parse_ipynb
from .generate_markdown_report import generate_markdown_report

def find_first_ipynb_file(repo_path):
    """Finds the first .ipynb file in the given directory."""
    ipynb_files = glob.glob(os.path.join(repo_path, '*.ipynb'))
    return ipynb_files[0] if ipynb_files else None

def save_html_report(html_content, file_path):
    """Saves the HTML content to a file."""
    os.makedirs(os.path.dirname(file_path), exist_ok=True)  # Ensure the directory exists
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

def generate_html_with_css(markdown_content):
    """Generates HTML content with CSS styling from Markdown content."""
    css_styles = """
    <style>
    body {
        font-family: Segoe UI, sans-serif;
        line-height: 1.6;
        margin: 20px;
    }
    h1, h2, h3 {
        color: #333;
    }
    table {
        width: 100%;
        border-collapse: collapse;
    }
    table, th, td {
        border: 1px solid #dddddd;
        padding: 8px;
        text-align: left;
    }
    th {
        background-color: #f2f2f2;
    }
    pre {
        background-color: #f4f4f4;
        border: 1px solid #ddd;
        padding: 10px;
        overflow: auto;
    }
    .critical {
        color: red;
    }
    </style>
    """

    # Convert Markdown to HTML
    html_content = markdown.markdown(markdown_content, extensions=[TableExtension()])

    # Combine CSS and HTML content
    styled_html = css_styles + html_content

    return styled_html

def main():
    repo_path = os.getenv('GITHUB_WORKSPACE', '.')

    # 1. Check Repository Structure
    required_directories = ['data', 'images']
    allowed_files_patterns = ['README.md', '.gitignore', 'LICENSE', 'requirements.txt', '*.ipynb', '*.py', 'reports/*']
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

    # 4. Security Checks and Dependency Analysis
    security_report = check_security_vulnerabilities(code_blocks)  # Pass the code blocks for analysis
    dependency_report = check_dependencies()

    # Prepare other reports with security and dependency reports
    other_reports = {
        "Security Vulnerability Scans": security_report,
        "Dependency Analysis": dependency_report,
        "Commit Analysis Results": "\n".join([f"- {message}" for message in commit_analysis_results])
    }

    # Compile all results into a final Markdown report
    notebook_stats = {
        'total_code_cells': len(code_blocks),
        'total_markdown_cells': len(markdown_cells)
    }

    final_report = generate_markdown_report(
        quality_reports=code_quality_results,
        repo_structure_results=repo_structure_results,
        notebook_stats=notebook_stats,
        other_reports=other_reports
    )

    # Convert Markdown report to HTML
    final_report_html = generate_html_with_css(final_report)


    # Save the report as an .html file in the reports directory
    report_file_path = os.path.join(repo_path, "reports", "autograder_report.html")
    save_html_report(final_report_html, report_file_path)
    print(f"Report saved to {report_file_path}")

if __name__ == '__main__':
    main()