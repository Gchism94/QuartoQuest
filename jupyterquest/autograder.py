import os
import glob
import markdown
from markdown.extensions.tables import TableExtension
from .repo_structure_check import check_directory_structure
from .code_quality_check import assess_code_quality
from .code_style_check import check_code_style
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
    """Generates HTML content with CSS styling from Markdown content, enhanced with semantic HTML and a footer."""
    css_styles = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Merriweather:wght@700&display=swap');

    body {
        font-family: 'Roboto', sans-serif;
        line-height: 1.6;
        margin: 50px;
        color: #333;
        background-color: #fff;
    }
    header, section, footer {
        margin-bottom: 40px;
    }
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Merriweather', sans-serif;
        margin-top: 20px;
        margin-bottom: 10px;
        font-weight: 700;
    }
    p, ul, ol, table, pre {
        margin-bottom: 20px;
    }
    a {
        color: #3498db;
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
    }
    table {
        border-collapse: collapse;
        width: 100%;
    }
    th, td {
        border: 1px solid #dddddd;
        padding: 8px;
        text-align: left;
    }
    th {
        background-color: #f2f2f2;
    }
    pre, code {
        background-color: #efefef;
        border: 1px solid #ddd;
        padding: 10px;
        overflow: auto;
    }
    code {
        font-family: 'Open Sans', monospace;
        padding: 2px 4px;
        font-size: 90%;
        border-radius: 3px;
    }
    footer {
        font-size: 0.9em;
        color: #777;
    }
    </style>
    """
    # Semantic HTML structure
    html_structure = """
    <header>
        <h1>Autograder Report</h1>
    </header>
    <main>
        {content}
    </main>
    <footer>
        <p>Generated on: {date}</p>
    </footer>
    """.format(content=markdown.markdown(markdown_content, extensions=[TableExtension()]),
               date=os.path.getmtime("autograder_report.html"))

    # Combine CSS and HTML content
    styled_html = css_styles + html_structure

    return styled_html



def main():
    repo_path = os.getenv('GITHUB_WORKSPACE', '.')
    reports_dir = os.path.join(repo_path, "docs")  

    # 1. Check Repository Structure
    required_directories = ['data', 'images']
    allowed_files_patterns = ['README.md', '.gitignore', 'LICENSE', 'requirements.txt', '*.ipynb', '*.py', 'docs/*']
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

    final_report = generate_markdown_report(
        quality_reports=code_quality_results,
        repo_structure_results=repo_structure_results,
        notebook_stats=notebook_stats,
        commit_analysis_results=commit_analysis_results,
    )

    # Convert Markdown report to HTML
    final_report_html = generate_html_with_css(final_report)


    # Save the report as an .html file in the reports directory
    report_file_path = os.path.join(reports_dir, "autograder_report.html")
    save_html_report(final_report_html, report_file_path)
    print(f"Report saved to {report_file_path}")

if __name__ == '__main__':
    main()