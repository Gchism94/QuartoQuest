import unittest
from quartoquest.generate_markdown_report import generate_markdown_report

class TestMarkdownReport(unittest.TestCase):
    def test_report_generation(self):
        # Mock data for quality reports
        sample_quality_reports = {
            "Code Block 1": {
                "Complexity": [("example_function", 2, "B")],
                "Structure": "Well-structured with clear logic."
            },
            "Code Block 2": {
                "Complexity": [("another_function", 3, "A")],
                "Structure": "Complex but manageable structure."
            }
            # Add more mock code blocks if needed
        }

        # Mock data for repository structure results
        sample_repo_structure_results = {
            "missing_directories": [],
            "unexpected_files": []
        }

        # Generate the report with the mock data
        report = generate_markdown_report(sample_quality_reports, sample_repo_structure_results)

        # Test for presence of key sections and content in the report
        self.assertIn("## Code Quality Checks", report)
        self.assertIn("Well-structured with clear logic.", report)
        self.assertIn("Complex but manageable structure.", report)
        self.assertIn("## Repository Structure Check", report)
        self.assertIn("missing_directories: []", report)
        self.assertIn("unexpected_files: []", report)

# Run the tests
if __name__ == '__main__':
    unittest.main()
