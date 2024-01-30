from git import Repo
from git.exc import InvalidGitRepositoryError

def analyze_commit_messages(repo_path):
    try:
        repo = Repo(repo_path)
    except InvalidGitRepositoryError:
        return "Invalid Git repository."

    # Assuming 'main' is the branch to be analyzed, adjust as needed
    branch = 'main'
    commits = list(repo.iter_commits(branch))
    if not commits:
        return "No commits found in the branch."

    short_message_issues = 0
    non_informative_issues = 0

    for commit in commits:
        if len(commit.message.strip()) < 10:
            short_message_issues += 1
        # Implement additional checks as needed

    return {
        "total_commits": len(commits),
        "short_message_issues": short_message_issues,
        "non_informative_issues": non_informative_issues
    }

if __name__ == "__main__":
    repo_path = '/autograder'  # Adjust this path based on your Docker setup
    commit_analysis_result = analyze_commit_messages(repo_path)
    print(commit_analysis_result)