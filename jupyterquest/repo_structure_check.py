import os

def check_directory_structure(repo_path, required_directories, allowed_files):
    """
    Checks if the repository has the required directory structure.
    Args:
    - repo_path: Path to the repository.
    - required_directories: List of directories that must exist.
    - allowed_files: List of allowed files in the root directory.
    
    Returns:
    - A dictionary with the results of the directory and file checks.
    """
    results = {
        'missing_directories': [],
        'unexpected_files': []
    }

    # Check for required directories
    for directory in required_directories:
        if not os.path.isdir(os.path.join(repo_path, directory)):
            results['missing_directories'].append(directory)

    # Check for unexpected files in root
    for file in os.listdir(repo_path):
        if os.path.isfile(os.path.join(repo_path, file)) and file not in allowed_files:
            results['unexpected_files'].append(file)

    return results

# Example usage
if __name__ == "__main__":
    # Use the GITHUB_WORKSPACE environment variable if available, otherwise default to the current directory
    repo_path = os.getenv('GITHUB_WORKSPACE', '.')

    required_directories = ['data']  # Modify as needed
    allowed_files = ['README.md', '.gitignore', 'LICENSE', 'requirements.txt', '*.ipynb', "data/*", "images/*"]  # Modify as needed

    structure_check_results = check_directory_structure(repo_path, required_directories, allowed_files)
    print(structure_check_results)