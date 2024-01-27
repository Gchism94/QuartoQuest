import unittest
from ..quartoquest.parse_qmd import parse_qmd

class TestParseQmd(unittest.TestCase):
    def test_extraction(self):
        test_qmd_content = """
        # Test Markdown
        ```python
        print("Hello, World!")
        ```
        Some text content.
        """
        result = parse_qmd(test_qmd_content)
        self.assertIn("print(\"Hello, World!\")", result['code_blocks'])
        self.assertIn("Some text content", result['markdown_text'])

# Run the tests
if __name__ == '__main__':
    unittest.main()
