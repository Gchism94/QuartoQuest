import unittest
from unittest.mock import patch, MagicMock
from jupyterquest import dependency_checks  # Adjust the import path according to your package structure

class TestDependencyChecks(unittest.TestCase):

    @patch('subprocess.run')
    def test_run_safety_no_issues(self, mock_run):
        # Simulate Safety returning no issues
        mock_run.return_value = MagicMock(stdout="No dependency issues found.", stderr="")
        result = dependency_checks.run_safety()
        self.assertIn("No dependency issues found.", result)

    @patch('subprocess.run')
    def test_run_safety_with_issues(self, mock_run):
        # Simulate Safety finding issues
        mock_run.return_value = MagicMock(stdout="1: issue found", stderr="")
        result = dependency_checks.run_safety()
        self.assertIn("- 1: issue found", result)

    @patch('subprocess.run')
    def test_run_pip_audit_no_issues(self, mock_run):
        # Simulate pip-audit returning no issues
        mock_run.return_value = MagicMock(stdout="No dependency issues found.", stderr="")
        result = dependency_checks.run_pip_audit()
        self.assertIn("No dependency issues found.", result)

    @patch('subprocess.run')
    def test_run_pip_audit_with_issues(self, mock_run):
        # Simulate pip-audit finding issues
        mock_run.return_value = MagicMock(stdout="1: issue found", stderr="")
        result = dependency_checks.run_pip_audit()
        self.assertIn("- 1: issue found", result)

    @patch('jupyterquest.dependency_checks.run_safety')
    @patch('jupyterquest.dependency_checks.run_pip_audit')
    def test_check_dependencies(self, mock_run_pip_audit, mock_run_safety):
        # Simulate both checks
        mock_run_safety.return_value = "## Safety Checks\n- No issues found."
        mock_run_pip_audit.return_value = "## pip-audit Checks\n- No issues found."
        result = dependency_checks.check_dependencies()
        self.assertIn("## Safety Checks\n- No issues found.", result)
        self.assertIn("## pip-audit Checks\n- No issues found.", result)

if __name__ == '__main__':
    unittest.main()
 