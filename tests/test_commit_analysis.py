import unittest
from unittest.mock import patch, MagicMock
from git.exc import InvalidGitRepositoryError, NoSuchPathError
import os
from jupyterquest.commit_analysis import analyze_commit_messages

class TestCommitAnalysis(unittest.TestCase):

    @patch('jupyterquest.commit_analysis.Repo')
    def test_analyze_commit_messages_valid_repo_with_branches(self, mock_repo):
        # Setup mock branches and commits
        mock_branch1_commit1 = MagicMock(message='feat: Add new feature\nDetails.\n')
        mock_branch1_commit2 = MagicMock(message='fix: Fix issue\nDetails.\n')
        # Simulate a shared commit across branches
        mock_branch2_commit1 = mock_branch1_commit1
        mock_branch2_commit2 = MagicMock(message='Update readme\nMinor updates.\n')

        # Branch simulation
        mock_repo.return_value.branches = ['branch1', 'branch2']
        mock_repo.return_value.iter_commits.side_effect = [
            [mock_branch1_commit1, mock_branch1_commit2],  # branch1 commits
            [mock_branch2_commit1, mock_branch2_commit2]   # branch2 commits
        ]

        expected_result = {
            "total_commits": 3,
            "short_message_issues": 0,
            "non_informative_issues": 2,
            "non_conforming_messages": 1
        }
        
        result = analyze_commit_messages('mock_repo_path')
        self.assertEqual(result, expected_result)

    @patch('jupyterquest.commit_analysis.Repo')
    def test_analyze_commit_messages_invalid_repo(self, mock_repo):
        mock_repo.side_effect = InvalidGitRepositoryError
        result = analyze_commit_messages('/path/to/invalid/repo')
        self.assertIn("Error with the repository:", result)

    @patch('jupyterquest.commit_analysis.Repo')
    def test_analyze_commit_messages_no_commits(self, mock_repo):
        mock_repo.return_value.iter_commits.return_value = []
        result = analyze_commit_messages('/path/to/repo/with/no/commits')
        self.assertEqual(result, "No commits found in the repository.")

    @patch('os.getenv')
    @patch('jupyterquest.commit_analysis.Repo')
    def test_analyze_commit_messages_env_variable(self, mock_repo, mock_getenv):
        # Setup environment variable mock
        mock_getenv.return_value = '/mock/repo/path'
        
        # Prepare mock commits
        mock_commit = MagicMock(message='feat: Enhance feature\nDetailed explanation.\n')
        
        # Ensure the mock repo iterates over commits correctly
        mock_repo.return_value.iter_commits = MagicMock(return_value=[mock_commit])
        
        # Expected results based on the mock commits
        expected_result = {
            "total_commits": 1,
            "short_message_issues": 0,
            "non_informative_issues": 0,
            "non_conforming_messages": 0
        }
        
        result = analyze_commit_messages(os.getenv('GITHUB_WORKSPACE'))
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()