import unittest
from unittest.mock import patch, MagicMock
from jupyterquest import commit_analysis  # Adjust the import path according to your package structure

class TestCommitAnalysis(unittest.TestCase):

    @patch('jupyterquest.commit_analysis.Repo')
    def test_analyze_commit_messages_valid_repo(self, mock_repo):
        # Setup mock
        mock_repo.return_value.iter_commits.return_value = [
            MagicMock(message='feat: Add new feature\nDetailed explanation of the feature.'),
            MagicMock(message='fix: Fix issue\nDetails about the fix.'),
            MagicMock(message='Update readme\nThis is a minor update.')  # This should be counted as non-informative and non-conforming
        ]
        
        expected_result = {
            "total_commits": 3,
            "short_message_issues": 0,  # Assuming all first lines are above the minimum length
            "non_informative_issues": 1,  # "Update readme" is considered non-informative
            "non_conforming_messages": 1  # "Update readme" does not conform to the structured pattern
        }
        
        result = commit_analysis.analyze_commit_messages('/path/to/valid/repo')
        self.assertEqual(result, expected_result)

    @patch('jupyterquest.commit_analysis.Repo')
    def test_analyze_commit_messages_invalid_repo(self, mock_repo):
        # Setup mock to raise an exception for an invalid repository
        mock_repo.side_effect = commit_analysis.InvalidGitRepositoryError
        
        result = commit_analysis.analyze_commit_messages('/path/to/invalid/repo')
        self.assertTrue("Error with the repository:" in result)

    @patch('jupyterquest.commit_analysis.Repo')
    def test_analyze_commit_messages_no_commits(self, mock_repo):
        # Setup mock for a repository with no commits
        mock_repo.return_value.iter_commits.return_value = []
        
        result = commit_analysis.analyze_commit_messages('/path/to/repo/with/no/commits')
        self.assertEqual(result, "No commits found in the branch.")

if __name__ == '__main__':
    unittest.main()