import unittest
import tempfile
import os
from jupyterquest.repo_structure_check import check_directory_structure

class TestRepoStructureCheck(unittest.TestCase):
    def test_structure_check(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            # Setup: Creating required directory and allowed file
            os.mkdir(os.path.join(tmp_dir, 'data'))
            with open(os.path.join(tmp_dir, 'README.md'), 'w') as f:
                f.write('Sample README content')

            # Setup: Creating a file that should be flagged as unexpected
            with open(os.path.join(tmp_dir, 'unexpected_file.txt'), 'w') as f:
                f.write('This file should not be here.')

            # Test: Checking directory structure
            required_directories = ['data']
            allowed_files_patterns = ['*.md', '.gitignore']  # Adjusted to use patterns
            result = check_directory_structure(tmp_dir, required_directories, allowed_files_patterns)

            # Assertions
            self.assertNotIn('data', result['missing_directories'], "Required 'data' directory is missing.")
            self.assertNotIn('README.md', result['unexpected_files'], "'README.md' is unexpectedly flagged.")
            self.assertIn('unexpected_file.txt', result['unexpected_files'], "'unexpected_file.txt' should be flagged as unexpected.")

# Run the tests
if __name__ == '__main__':
    unittest.main()
