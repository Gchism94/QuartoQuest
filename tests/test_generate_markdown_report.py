import unittest
from jupyterquest.generate_markdown_report import generate_markdown_report

class TestMarkdownReport(unittest.TestCase):
    def test_report_generation(self):
        # Prepare mock data
        sample_quality_reports = {
            "Code Block 1": {
                "Complexity": [("example_function", 2, "B")],
                "Structure": "Well-structured with clear logic."
            },
            "Code Block 2": {
                "Complexity": [("another_function", 3, "A")],
                "Structure": "Complex but manageable structure."
            }
        }
        sample_repo_structure_results = {"missing_directories": [], "unexpected_files": []}
        notebook_stats = {"total_code_cells": 5, "total_markdown_cells": 3}  # Updated to include markdown cells
        other_reports = {
            "Code Style Results": "No issues found.",
            "Commit Analysis Results": "No commit message issues.",
            "Security Vulnerability Scans": "No security vulnerabilities found.",
            "Dependency Analysis": "All dependencies are secure."
        }
        improvement_plan = [
            "Review and address all code style issues.",
            "Reduce complexity in high-complexity functions.",
            "Ensure all dependencies are up-to-date and secure."
        ]

        # Generate report
        report = generate_markdown_report(
            sample_quality_reports,
            sample_repo_structure_results,
            notebook_stats,
            other_reports,
            improvement_plan  # Now passing the improvement plan
        )

        # Assertions to check the presence of new sections and content
        self.assertIn("## Summary", report)
        self.assertIn("This report outlines the findings", report)
        self.assertIn("## Improvement Plan", report)
        self.assertIn("Review and address all code style issues.", report)
        self.assertIn("## Additional Resources", report)
        self.assertIn("[Python Official Documentation](https://docs.python.org/3/)", report)
        
        # Existing checks
        self.assertIn("## Code Quality Checks", report)
        self.assertIn("Well-structured with clear logic.", report)
        self.assertIn("## Repository Structure Check", report)
        self.assertIn("- **Missing Directories**: ", report)
        
        # Checks for other reports
        self.assertIn("## Code Style Results", report)
        self.assertIn("No issues found.", report)
        self.assertIn("## Security Vulnerability Scans", report)
        self.assertIn("No security vulnerabilities found.", report)
        self.assertIn("## Dependency Analysis", report)
        self.assertIn("All dependencies are secure.", report)
        
        # Check for notebook stats
        self.assertIn("- **Total Code Cells**: 5\n", report)
        self.assertIn("- **Total Markdown Cells**: 3\n", report)

if __name__ == '__main__':
    unittest.main()