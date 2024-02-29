from git import Repo
from git.exc import InvalidGitRepositoryError, NoSuchPathError

def analyze_commit_messages(repo_path):
    try:
        repo = Repo(repo_path)
    except (InvalidGitRepositoryError, NoSuchPathError) as e:
        return f"Error with the repository: {str(e)}"

    # Assuming 'main' is the branch to be analyzed, adjust as needed
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

    # Define a list of non-informative keywords
    non_informative_keywords = ['fix', 'update', 'minor', 'misc', 'changes']

    # Define a regex pattern for a structured commit message, e.g., "TYPE: Description"
    import re
    structured_message_pattern = re.compile(r"^(feat|fix|docs|style|refactor|perf|test|chore):\s.+")

    for commit in commits:
        message = commit.message.strip()
        # Check for short messages
        if len(message) < 10:
            short_message_issues += 1
        # Check for non-informative messages
        if any(keyword in message.lower() for keyword in non_informative_keywords):
            non_informative_issues += 1
        # Check for structured commit message conformity
        if not structured_message_pattern.match(message):
            non_conforming_messages += 1

    return {
        "total_commits": len(commits),
        "short_message_issues": short_message_issues,
        "non_informative_issues": non_informative_issues,
        "non_conforming_messages": non_conforming_messages
    }

if __name__ == "__main__":
    repo_path = '/path/to/your/repo'  # Adjust this path as necessary
    commit_analysis_result = analyze_commit_messages(repo_path)
    print(commit_analysis_result)
