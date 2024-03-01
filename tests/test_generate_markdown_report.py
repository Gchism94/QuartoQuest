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
        notebook_stats = {"total_code_cells": 5, "total_markdown_cells": 3}
        other_reports = {
            "Code Style Results": "No issues found.",
            "Security Vulnerability Scans": "No security vulnerabilities found.",
            "Dependency Analysis": "All dependencies are secure."
        }
        commit_analysis_results = {
            "total_commits": 10,
            "short_message_issues": 1,
            "non_informative_issues": 2,
            "non_conforming_messages": 0
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
            improvement_plan,
            commit_analysis_results  # Including commit analysis results in the test
        )

        # Verify the inclusion and correct formatting of the new sections and content
        self.assertIn("## Summary", report)
        self.assertIn("## Improvement Plan", report)
        self.assertIn("Review and address all code style issues.", report)
        self.assertIn("## Additional Resources", report)
        self.assertIn("## Code Quality Checks", report)
        self.assertIn("Well-structured with clear logic.", report)
        self.assertIn("## Repository Structure Check", report)
        self.assertIn("- **Missing Directories**: ", report)
        self.assertIn("## Code Style Results", report)
        self.assertIn("No issues found.", report)
        self.assertIn("## Security Vulnerability Scans", report)
        self.assertIn("No security vulnerabilities found.", report)
        self.assertIn("## Dependency Analysis", report)
        self.assertIn("All dependencies are secure.", report)
        self.assertIn("- **Total Code Cells**: 5\n", report)
        self.assertIn("- **Total Markdown Cells**: 3\n", report)
        self.assertIn("## Commit Analysis Results", report)
        self.assertIn("- **Total Commits**: 10", report)
        self.assertIn("- **Short Message Issues**: 1", report)
        self.assertIn("- **Non Informative Issues**: 2", report)
        self.assertIn("- **Non Conforming Messages**: 0", report)

if __name__ == '__main__':
    unittest.main()