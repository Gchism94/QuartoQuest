import unittest
import tempfile
import os
from quartoquest.parse_qmd import parse_qmd

class TestParseQmd(unittest.TestCase):
    def test_extraction(self):
        # Create a temporary file with test content
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(b"# Test Markdown\n```python\nprint(\"Hello, World!\")\n```\nSome text content.")
            tmp_path = tmp.name

        try:
            result = parse_qmd(tmp_path)
            self.assertIn('python\nprint("Hello, World!")\n', result['code_blocks'])
            # Additional assertions
        finally:
            # Clean up the temporary file
            os.remove(tmp_path)

# Run the tests
if __name__ == '__main__':
    unittest.main()

