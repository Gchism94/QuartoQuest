import unittest
import json
from unittest.mock import patch, MagicMock
from jupyterquest.security_checks import run_bandit, check_security_vulnerabilities

class TestSecurityChecks(unittest.TestCase):

    @patch('subprocess.run')
    def test_run_bandit_no_issues(self, mock_run):
        # Simulate Bandit finding no security issues
        mock_run.return_value = MagicMock(stdout='{"results": []}', stderr="")
        result = run_bandit("safe_code = True")
        self.assertEqual(result, "No security issues found.")

    @patch('subprocess.run')
    def test_run_bandit_with_issues(self, mock_run):
        # Simulate Bandit finding security issues
        mock_bandit_output = {
            "results": [
                {
                    "test_id": "B101",
                    "issue_text": "Use of assert detected.",
                    "issue_severity": "LOW",
                    "issue_confidence": "HIGH",
                    "more_info": "http://example.com/b101"
                }
            ]
        }
        mock_run.return_value = MagicMock(stdout=json.dumps(mock_bandit_output), stderr="")
        result = run_bandit("assert user.is_admin")
        expected_output = (
            "### Security Issues Found\n"
            "- **Test ID**: B101, **Issue**: Use of assert detected.\n"
            "  - **Severity**: LOW, **Confidence**: HIGH\n"
            "  - **Remediation**: http://example.com/b101\n"
        )
        self.assertEqual(result, expected_output)

    @patch('jupyterquest.security_checks.run_bandit')
    def test_check_security_vulnerabilities_multiple_blocks(self, mock_run_bandit):
        # Simulate multiple code blocks with and without issues
        mock_run_bandit.side_effect = [
            "No security issues found.",
            "### Security Issues Found\n- **Test ID**: B102, **Issue**: Use of exec detected.\n  - **Severity**: HIGH, **Confidence**: MEDIUM\n  - **Remediation**: http://example.com/b102\n"
        ]
        code_blocks = ["safe_code = True", "exec('unsafe_code')"]
        result = check_security_vulnerabilities(code_blocks)
        expected_output = (
            "## Code Block 1\nNo security issues found.\n\n"
            "## Code Block 2\n### Security Issues Found\n- **Test ID**: B102, **Issue**: Use of exec detected.\n"
            "  - **Severity**: HIGH, **Confidence**: MEDIUM\n"
            "  - **Remediation**: http://example.com/b102\n\n"
            "Safety checks did not find any issues."
        )
        self.assertEqual(result.strip(), expected_output.strip())


if __name__ == '__main__':
    unittest.main()