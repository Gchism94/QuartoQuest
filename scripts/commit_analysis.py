from git import Repo
from git.exc import InvalidGitRepositoryError

def analyze_commit_messages(repo_path):
    """
    Analyzes commit messages in the given repository.
    Returns a summary of the analysis.
    """
    try:
        repo = Repo(repo_path)
    except InvalidGitRepositoryError:
        return "Invalid Git repository."

    commits = list(repo.iter_commits('main'))  # assuming the default branch is 'main'
    if not commits:
        return "No commits found."

    short_message_issues = 0
    non_informative_issues = 0

    for commit in commits:
        # Example check for message length
        if len(commit.message.strip()) < 10:  
            short_message_issues += 1

        # Add more checks as needed, e.g., for non-informative messages

    return {
        "total_commits": len(commits),
        "short_message_issues": short_message_issues,
        "non_informative_issues": non_informative_issues
    }

# Example usage
if __name__ == "__main__":
    repo_path = '/path/to/repo'  # Replace with the actual path to the repository
    commit_analysis_result = analyze_commit_messages(repo_path)
    print(commit_analysis_result)
