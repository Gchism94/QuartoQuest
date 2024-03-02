import unittest
from unittest.mock import patch, MagicMock
from git.exc import InvalidGitRepositoryError, NoSuchPathError
import os
from jupyterquest.commit_analysis import analyze_commit_messages

class TestCommitAnalysis(unittest.TestCase):

    @patch('jupyterquest.commit_analysis.Repo')
    def test_analyze_commit_messages_valid_repo_with_branches_and_exclusions(self, mock_repo):
        # Setup mock commits with authors and commit messages
        mock_commit1 = MagicMock(message='feat: Add new feature\nDetails.\n', hexsha='123', author=MagicMock(name='SomeUser'))
        mock_commit2 = MagicMock(message='fix: Fix issue\nDetails.\n', hexsha='456', author=MagicMock(name='Gchism94'))
        mock_commit3 = MagicMock(message='Update readme\nMinor updates.\n', hexsha='789', author=MagicMock(name='SomeUser'))  # Considered non-informative and non-conforming
        mock_commit4 = MagicMock(message='Add autograder report', hexsha='abc', author=MagicMock(name='actions-user'))  # Excluded based on message

        # Simulate iter_commits returning these commits
        mock_repo.return_value.references = ['master']
        mock_repo.return_value.iter_commits = MagicMock(return_value=[mock_commit1, mock_commit2, mock_commit3, mock_commit4])

        expected_result = {
            "total_commits": 3,  # Excluding commits by Gchism94 and 'Add autograder report'
            "short_message_issues": 0,
            "non_informative_issues": 2,  # 'Update readme' is considered non-informative
            "non_conforming_messages": 1  # 'Update readme' is considered non-conforming
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
        mock_repo.return_value.iter_commits = MagicMock(return_value=[])

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
        mock_commit = MagicMock(message='feat: Enhance feature\nDetailed explanation.\n', hexsha='def', author=MagicMock(name='SomeUser'))
        # Simulate iter_commits returning these commits
        mock_repo.return_value.iter_commits = MagicMock(return_value=[mock_commit])

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