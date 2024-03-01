import unittest
from unittest.mock import patch, MagicMock
from jupyterquest.autograder import main
import os

class TestAutograder(unittest.TestCase):

    @patch('jupyterquest.autograder.os.getenv', return_value='.')
    @patch('jupyterquest.autograder.glob.glob', return_value=['/path/to/notebook.ipynb'])
    @patch('jupyterquest.autograder.check_directory_structure', return_value={'missing_directories': [], 'unexpected_files': []})
    @patch('jupyterquest.autograder.parse_ipynb', return_value={'code_cells': ['print("Hello, World!")'], 'markdown_cells': ['# Title']})
    @patch('jupyterquest.autograder.assess_code_quality', return_value={'Code Block 1': {'Complexity': 'Low', 'Structure': 'Good'}})
    @patch('jupyterquest.autograder.check_code_style', return_value=['No issues found.'])
    @patch('jupyterquest.autograder.analyze_commit_messages', return_value={'total_commits': 1, 'short_message_issues': 0, 'non_informative_issues': 0, 'non_conforming_messages': 1})
    @patch('jupyterquest.autograder.check_security_vulnerabilities', return_value='No security vulnerabilities found.')
    @patch('jupyterquest.autograder.check_dependencies', return_value='All dependencies are secure.')
    @patch('jupyterquest.autograder.generate_html_with_css')
    @patch('builtins.open', new_callable=unittest.mock.mock_open)  # Mock the built-in open function
    def test_main_integration(self, mock_open, mock_generate_html, mock_check_deps, mock_run_security, mock_analyze_commits, mock_check_style, mock_assess_quality, mock_parse, mock_check_structure, mock_glob, mock_getenv):
        # Setup mocks
        mock_generate_html.return_value = '<html>Mocked HTML Content</html>'

        # Call the main function
        main()

        # Verify that the correct path was used to save the HTML report
        report_path = os.path.join('.', "reports", "autograder_report.html")
        mock_open.assert_called_with(report_path, 'w', encoding='utf-8')
        
        # Verify the HTML content generation call
        mock_generate_html.assert_called()

        # Optionally, verify that the write function was called with the expected HTML content
        # mock_open.return_value.write.assert_called_once_with('<html>Mocked HTML Content</html>')

if __name__ == '__main__':
    unittest.main()