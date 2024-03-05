import os
import fnmatch

def check_directory_structure(repo_path, required_directories, allowed_files_patterns):
    """
    Checks if the repository has the required directory structure and allowed files.
    
    Args:
        repo_path (str): Path to the repository to be checked.
        required_directories (list): A list of directories that must exist in the repo.
        allowed_files_patterns (list): A list of allowed file patterns in the root of the repo.
    
    Returns:
        dict: A dictionary with keys 'missing_directories' and 'unexpected_files'. Each key maps to a list.
    """
    results = {
        'missing_directories': [],
        'unexpected_files': []
    }

    # Check for required directories
    for directory in required_directories:
        directory_path = os.path.join(repo_path, directory)
        if not os.path.isdir(directory_path):
            results['missing_directories'].append(directory)

    # Check for unexpected files in the root directory
    root_files = os.listdir(repo_path)
    for file_name in root_files:
        file_path = os.path.join(repo_path, file_name)
        if os.path.isfile(file_path):
            # Check if the file matches any of the allowed patterns
            if not any(fnmatch.fnmatch(file_name, pattern) for pattern in allowed_files_patterns):
                results['unexpected_files'].append(file_name)

    return results

# Example usage
if __name__ == "__main__":
    repo_path = os.getenv('GITHUB_WORKSPACE', '.')
    required_directories = ['data', 'docs']
    allowed_files_patterns = ['README.md', '.gitignore', 'LICENSE', 'requirements.txt', '*.py', '*.ipynb', 'docs/*']
    
    structure_check_results = check_directory_structure(repo_path, required_directories, allowed_files_patterns)
    print("Repository Structure Check Results:", structure_check_results)
