import unittest
from generate_markdown_report import generate_markdown_report

class TestMarkdownReport(unittest.TestCase):
    def test_report_generation(self):
        sample_data = {
            # Sample data structured as expected by generate_markdown_report
        }
        report = generate_markdown_report(sample_data)
        # Test for presence of key sections in the report
        self.assertIn("## Code Quality Checks", report)

# Run the tests
if __name__ == '__main__':
    unittest.main()
