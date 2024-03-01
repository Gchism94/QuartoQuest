import unittest
from unittest.mock import patch, MagicMock
# Ensure the import path is correct for your project structure
from jupyterquest.commit_analysis import analyze_commit_messages

class TestCommitAnalysis(unittest.TestCase):

    @patch('jupyterquest.commit_analysis.Repo')
    def test_analyze_commit_messages_valid_repo(self, mock_repo):
        # Setup mock commits with a variety of commit message types
        mock_repo.return_value.iter_commits.return_value = [
            MagicMock(message='feat: Add new feature\nMore details about feature.\n'),
            MagicMock(message='fix: Fix issue\nDetails about the fix.\n'),
            MagicMock(message='Update readme\nMinor updates.\n')
        ]
        
        # Adjust expectations based on the refined logic in commit_analysis.py
        expected_result = {
            "total_commits": 3,
            "short_message_issues": 0,
            "non_informative_issues": 1,  # "Update readme" considered non-informative
            "non_conforming_messages": 1  # "Update readme" considered non-conforming
        }
        
        result = analyze_commit_messages('/path/to/valid/repo')
        self.assertEqual(result, expected_result)

    @patch('jupyterquest.commit_analysis.Repo')
    def test_analyze_commit_messages_invalid_repo(self, mock_repo):
        # Mock to simulate an invalid repository path
        mock_repo.side_effect = commit_analysis.InvalidGitRepositoryError
        
        result = analyze_commit_messages('/path/to/invalid/repo')
        self.assertIn("Error with the repository:", result)

    @patch('jupyterquest.commit_analysis.Repo')
    def test_analyze_commit_messages_no_commits(self, mock_repo):
        # Mock to simulate a repository with no commits
        mock_repo.return_value.iter_commits.return_value = []
        
        result = analyze_commit_messages('/path/to/repo/with/no/commits')
        self.assertEqual(result, "No commits found in the branch.")

if __name__ == '__main__':
    unittest.main()
