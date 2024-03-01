from git import Repo
from git.exc import InvalidGitRepositoryError, NoSuchPathError
import re
import os

def analyze_commit_messages(repo_path):
    try:
        repo = Repo(repo_path)
    except (InvalidGitRepositoryError, NoSuchPathError) as e:
        return f"Error with the repository: {str(e)}"

    # Use a set to hold unique commit hashes to avoid processing duplicates
    processed_commits = set()
    total_commits, short_message_issues, non_informative_issues, non_conforming_messages = 0, 0, 0, 0

    non_informative_keywords = ['fix', 'update', 'minor', 'misc', 'changes']
    structured_message_pattern = re.compile(r"^(feat|fix|docs|style|refactor|perf|test|chore):\s.+")
    exclude_phrase = "Add autograder report"  # Phrase to exclude

    # Include commits from all refs (branches, tags, etc.)
    for ref in repo.references:
        for commit in repo.iter_commits(ref):
            if commit.hexsha not in processed_commits:
                first_line = commit.message.strip().split('\n', 1)[0]
                
                # Skip commits with the excluded phrase
                if exclude_phrase in commit.message:
                    continue

                processed_commits.add(commit.hexsha)
                total_commits += 1

                if len(first_line) < 10:
                    short_message_issues += 1
                if any(keyword in first_line.lower() for keyword in non_informative_keywords):
                    non_informative_issues += 1
                if not structured_message_pattern.match(first_line):
                    non_conforming_messages += 1

    return {
        "total_commits": total_commits,
        "short_message_issues": short_message_issues,
        "non_informative_issues": non_informative_issues,
        "non_conforming_messages": non_conforming_messages
    }

if __name__ == "__main__":
    repo_path = os.getenv('GITHUB_WORKSPACE', '.')
    commit_analysis_result = analyze_commit_messages(repo_path)
    print(commit_analysis_result)