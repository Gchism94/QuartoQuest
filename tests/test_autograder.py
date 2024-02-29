import unittest
from unittest.mock import patch, MagicMock
from jupyterquest.autograder import main

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
    @patch('jupyterquest.autograder.save_markdown_report')
    def test_main_integration(self, mock_save, mock_check_deps, mock_run_security, mock_analyze_commits, mock_check_style, mock_assess_quality, mock_parse, mock_check_structure, mock_glob, mock_getenv):
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
        mock_save.return_value = None  # Assuming saving the report does not return a value

        # Call the main function
        main()

        # Verify that save_markdown_report was called with expected arguments
        mock_save.assert_called()
        # This line checks that save_markdown_report was called, but you might want to be more specific about the arguments.
        # For example, you can inspect the call arguments to ensure the generated Markdown content meets expectations.
        # This would involve checking the `call_args` of `mock_save` and performing assertions on the content.

if __name__ == '__main__':
    unittest.main()
 