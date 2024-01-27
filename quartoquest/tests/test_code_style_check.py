import unittest
from quartoquest import check_code_style

class TestCodeStyleCheck(unittest.TestCase):
    def test_linting(self):
        code_blocks = ["import math\nx=2\nprint(x)"]  # Incorrect style
        results = check_code_style(code_blocks)
        self.assertNotEqual(results[0], "")  # Expecting non-empty result due to style issues

# Run the tests
if __name__ == '__main__':
    unittest.main()
