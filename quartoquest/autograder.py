import os
from . import repo_structure_check
# Import other necessary modules or scripts

def main():
    repo_path = os.getenv('GITHUB_WORKSPACE', '.')

    repo_structure_results = repo_structure_check.check_directory_structure(
        repo_path, ['data'], ['README.md', '.gitignore', 'LICENSE', 'requirements.txt']
    )
    print("Repository Structure Check Results:", repo_structure_results)

    final_report = compile_report(repo_structure_results)
    print(final_report)

    # Write the final report to a file
    with open('autograder_report.md', 'w') as file:
        file.write(final_report)

def compile_report(*args):
    report = "Autograder Final Report\n"
    for result in args:
        report += str(result) + "\n"
    return report

if __name__ == "__main__":
    main()