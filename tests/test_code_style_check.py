import unittest
from quartoquest.code_style_check import check_code_style

class TestCodeStyleCheck(unittest.TestCase):
    def test_linting(self):
        code_with_style_issues = "import math\nx=2\nprint(x)"  # Example of code with style issues
        results = check_code_style(code_with_style_issues)
        self.assertNotEqual(results, "", "Expected style issues, but none were found")

if __name__ == '__main__':
    unittest.main()
