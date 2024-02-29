import unittest
import tempfile
import os
import json
from jupyterquest.parse_ipynb import parse_ipynb  # Ensure this is the correct import

class TestParseIpynb(unittest.TestCase):
    def test_extraction(self):
        # Create a temporary file with minimal .ipynb content
        ipynb_content = {
            "cells": [
                {
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": [
                        "# Test Markdown"
                    ]
                },
                {
                    "cell_type": "code",
                    "execution_count": None,
                    "metadata": {},
                    "outputs": [],
                    "source": [
                        "print(\"Hello, World!\")"
                    ]
                }
            ],
            "metadata": {},
            "nbformat": 4,
            "nbformat_minor": 2
        }

        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.ipynb') as tmp:
            json.dump(ipynb_content, tmp)
            tmp_path = tmp.name

        try:
            # Assuming parse_ipynb returns a dictionary with 'code_cells' and 'markdown_cells' keys
            result = parse_ipynb(tmp_path)
            self.assertIn('print("Hello, World!")', result['code_cells'][0], "Code cell content not extracted correctly.")
            self.assertIn('# Test Markdown', result['markdown_cells'][0], "Markdown cell content not extracted correctly.")
        finally:
            # Clean up the temporary file
            os.remove(tmp_path)

# Run the tests
if __name__ == '__main__':
    unittest.main()


