from git import Repo
from git.exc import InvalidGitRepositoryError, NoSuchPathError
import re
import os

def analyze_commit_messages(repo_path):
    try:
        repo = Repo(repo_path)
    except (InvalidGitRepositoryError, NoSuchPathError) as e:
        return f"Error with the repository: {str(e)}"

    # Initialize a set to hold unique commits
    unique_commits = set()

    # Iterate through all branches to collect commits
    for branch in repo.branches:
        for commit in repo.iter_commits(branch):
            unique_commits.add(commit)

    if not unique_commits:
        return "No commits found in the repository."

    # Continue with analysis as before
    short_message_issues = 0
    non_informative_issues = 0
    non_conforming_messages = 0

    non_informative_keywords = ['fix', 'update', 'minor', 'misc', 'changes']
    structured_message_pattern = re.compile(r"^(feat|fix|docs|style|refactor|perf|test|chore):\s.+")

    for commit in unique_commits:
        first_line = commit.message.strip().split('\n', 1)[0]
        if len(first_line) < 10:
            short_message_issues += 1
        if any(keyword in first_line.lower() for keyword in non_informative_keywords):
            non_informative_issues += 1
        if not structured_message_pattern.match(first_line):
            non_conforming_messages += 1

    return {
        "total_commits": len(unique_commits),
        "short_message_issues": short_message_issues,
        "non_informative_issues": non_informative_issues,
        "non_conforming_messages": non_conforming_messages
    }

if __name__ == "__main__":
    repo_path = os.getenv('GITHUB_WORKSPACE')
    commit_analysis_result = analyze_commit_messages(repo_path)
    print(commit_analysis_result)
