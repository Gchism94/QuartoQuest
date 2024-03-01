from git import Repo
from git.exc import InvalidGitRepositoryError, NoSuchPathError
import re

def analyze_commit_messages(repo_path):
    """
    Analyzes commit messages in a given repository for adherence to defined standards.

    Parameters:
    - repo_path (str): Path to the Git repository.

    Returns:
    - dict: Summary of analysis including counts of total commits, short messages,
            non-informative messages, and non-conforming messages.
    """
    try:
        repo = Repo(repo_path)
    except (InvalidGitRepositoryError, NoSuchPathError) as e:
        return f"Error with the repository: {str(e)}"

    branch = 'main'
    try:
        commits = list(repo.iter_commits(branch))
    except ValueError:
        return f"No such branch: '{branch}'."

    if not commits:
        return "No commits found in the branch."

    short_message_issues = 0
    non_informative_issues = 0
    non_conforming_messages = 0

    # Define non-informative keywords based on common practices.
    non_informative_keywords = ['fix', 'update', 'minor', 'misc', 'changes']

    # Regular expression for structured commit messages, e.g., "TYPE: Description".
    structured_message_pattern = re.compile(r"^(feat|fix|docs|style|refactor|perf|test|chore):\s.+")

    for commit in commits:
        first_line = commit.message.strip().split('\n', 1)[0]
        if len(first_line) < 10:
            short_message_issues += 1
        if any(keyword in first_line.lower() for keyword in non_informative_keywords):
            non_informative_issues += 1
        if not structured_message_pattern.match(first_line):
            non_conforming_messages += 1

    return {
        "total_commits": len(commits),
        "short_message_issues": short_message_issues,
        "non_informative_issues": non_informative_issues,
        "non_conforming_messages": non_conforming_messages
    }

if __name__ == "__main__":
    repo_path = '/path/to/your/repo'  # Adjust as necessary.
    commit_analysis_result = analyze_commit_messages(repo_path)
    print(commit_analysis_result)