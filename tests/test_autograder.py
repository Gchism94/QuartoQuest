import unittest
from unittest.mock import patch, MagicMock
from jupyterquest.autograder import main
import markdown

class TestAutograder(unittest.TestCase):

    @patch('jupyterquest.autograder.os.getenv')
    @patch('jupyterquest.autograder.glob.glob')
    @patch('jupyterquest.autograder.check_directory_structure')
    @patch('jupyterquest.autograder.parse_ipynb')
    @patch('jupyterquest.autograder.assess_code_quality')
    @patch('jupyterquest.autograder.check_code_style')
    @patch('jupyterquest.autograder.analyze_commit_messages')
    @patch('jupyterquest.autograder.check_security_vulnerabilities')
    @patch('jupyterquest.autograder.check_dependencies')
    @patch('builtins.open', new_callable=unittest.mock.mock_open)  # Mock the built-in open function
    def test_main_integration(self, mock_open, mock_check_deps, mock_run_security, mock_analyze_commits, mock_check_style, mock_assess_quality, mock_parse, mock_check_structure, mock_glob, mock_getenv):
        # Setup mocks
        mock_getenv.return_value = '.'
        mock_glob.return_value = ['/path/to/notebook.ipynb']
        mock_check_structure.return_value = {'missing_directories': [], 'unexpected_files': []}
        mock_parse.return_value = {'code_cells': ['print("Hello, World!")'], 'markdown_cells': ['# Title']}
        mock_assess_quality.return_value = {'Code Block 1': {'Complexity': 'Low', 'Structure': 'Good'}}
        mock_check_style.return_value = ['No issues found.']
        mock_analyze_commits.return_value = 'No commit message issues.'
        mock_run_security.return_value = 'No security vulnerabilities found.'
        mock_check_deps.return_value = 'All dependencies are secure.'

        # Call the main function
        main()

        # Verify that the open function was called to write the HTML report
        mock_open.assert_called_with('./reports/autograder_report.html', 'w', encoding='utf-8')
        
        # Optionally, verify that the write function was called with the expected HTML content
        # This assumes that you want to check the HTML content as well.
        # html_content = markdown.markdown(mock_generate_markdown_report.return_value)
        # mock_open.return_value.write.assert_called_once_with(html_content)

if __name__ == '__main__':
    unittest.main()
