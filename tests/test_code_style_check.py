import unittest
from jupyterquest.code_style_check import check_code_style

class TestCodeStyleCheck(unittest.TestCase):
    def test_linting_with_issues(self):
        # Prepare a list of code blocks, including one with style issues
        code_blocks_with_style_issues = [
            "import math\nx=2\nprint(x)"  # Example of code with style issues
        ]
        # Check style for each block
        results = check_code_style(code_blocks_with_style_issues)

        # Since results is expected to be a list of linting results for each block
        self.assertTrue(len(results) > 0, "Expected at least one linting result")
        self.assertNotEqual(results[0].strip(), "", "Expected style issues, but none were found in the first code block")

    def test_linting_without_issues(self):
        # Prepare a list of code blocks without style issues
        code_blocks_without_style_issues = [
            "x = 2\nprint(x)\n"  # Code without unused import or other style issues
        ]
        # Check style for each block
        results = check_code_style(code_blocks_without_style_issues)

        # Test if the linting result correctly indicates no issues
        self.assertTrue(len(results) > 0, "Expected at least one linting result")
        # Assuming that no issues result in a specific message or an empty string, adjust as per your implementation
        self.assertEqual(results[0].strip(), "No issues found.", "Expected no style issues, but some were found in the first code block")
        
if __name__ == '__main__':
    unittest.main()