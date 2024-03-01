import unittest
from unittest.mock import patch, MagicMock
from git.exc import InvalidGitRepositoryError
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

        # Simulate iter_commits for each branch
        mock_repo.return_value.branches = MagicMock()
        mock_repo.return_value.iter_commits.side_effect = lambda branch: {
            'branch1': [mock_branch1_commit1, mock_branch1_commit2],
            'branch2': [mock_branch2_commit1, mock_branch2_commit2],
        }[branch]

        expected_result = {
            "total_commits": 3,  # Three unique commits across branches
            "short_message_issues": 0,
            "non_informative_issues": 1,  # Assuming 'Update readme' is non-informative
            "non_conforming_messages": 1  # Assuming 'Update readme' is non-conforming
        }
        
        result = analyze_commit_messages('mock_repo_path')
        self.assertEqual(result, expected_result)

    @patch('jupyterquest.commit_analysis.Repo')
    def test_analyze_commit_messages_invalid_repo(self, mock_repo):
        mock_repo.side_effect = InvalidGitRepositoryError
        result = analyze_commit_messages('/path/to/invalid/repo')
        self.assertTrue("Error with the repository:" in result)

    @patch('jupyterquest.commit_analysis.Repo')
    def test_analyze_commit_messages_no_commits(self, mock_repo):
        mock_repo.return_value.iter_commits.return_value = []
        expected_result = {
            "total_commits": 0,
            "short_message_issues": 0,
            "non_informative_issues": 0,
            "non_conforming_messages": 0
        }
        result = analyze_commit_messages('/path/to/repo/with/no/commits')
        self.assertEqual(result, expected_result)

    @patch('os.getenv', return_value='/mock/repo/path')
    @patch('jupyterquest.commit_analysis.Repo')
    def test_analyze_commit_messages_env_variable(self, mock_repo, mock_getenv):
        # Setup mock commits
        mock_commit = MagicMock()
        mock_commit.message = 'feat: Enhance feature\nDetailed explanation.\n'
        mock_repo.return_value.iter_commits.return_value = [mock_commit]

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