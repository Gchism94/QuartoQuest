import unittest
from jupyterquest.generate_markdown_report import generate_markdown_report

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

        # Assuming inclusion of additional data such as code style and commit analysis results
        additional_data = {
            "Code Style Results": "No issues found.",
            "Commit Analysis Results": "No commit message issues."
        }

        # Generate the report with the mock data
        report = generate_markdown_report(sample_quality_reports, sample_repo_structure_results, additional_data)

        # Test for presence of key sections and content in the report
        self.assertIn("## Code Quality Checks", report)
        self.assertIn("Well-structured with clear logic.", report)
        self.assertIn("Complex but manageable structure.", report)
        self.assertIn("## Repository Structure Check", report)
        self.assertIn("- **Missing Directories**: ", report)
        self.assertIn("- **Unexpected Files**: ", report)
        # Test for additional sections if applicable
        self.assertIn("## Code Style Results", report)
        self.assertIn("No issues found.", report)
        self.assertIn("## Commit Analysis Results", report)
        self.assertIn("No commit message issues.", report)

# Run the tests
if __name__ == '__main__':
    unittest.main()