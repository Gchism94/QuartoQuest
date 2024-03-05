import unittest
import tempfile
import os
from jupyterquest.repo_structure_check import check_directory_structure

class TestRepoStructureCheck(unittest.TestCase):
    def setUp(self):
        # Setup a temporary directory for the test
        self.tmp_dir = tempfile.TemporaryDirectory()

    def tearDown(self):
        # Clean up after the test
        self.tmp_dir.cleanup()

    def test_structure_check(self):
        # Setup: Creating required directory and allowed/unexpected files
        os.mkdir(os.path.join(self.tmp_dir.name, 'data'))
        with open(os.path.join(self.tmp_dir.name, 'README.md'), 'w') as f:
            f.write('Sample README content')
        with open(os.path.join(self.tmp_dir.name, 'unexpected_file.txt'), 'w') as f:
            f.write('This file should not be here.')
        
        # Setup: Creating a Python script to test '*.py' pattern
        with open(os.path.join(self.tmp_dir.name, 'script.py'), 'w') as f:
            f.write('# Python script content')

        # Defining required directories and allowed file patterns
        required_directories = ['data']
        allowed_files_patterns = ['README.md', '*.md', '*.py', 'data/*']

        # Checking directory structure
        result = check_directory_structure(self.tmp_dir.name, required_directories, allowed_files_patterns)

        # Assertions
        self.assertNotIn('data', result['missing_directories'], "Required 'data' directory is missing.")
        self.assertNotIn('README.md', result['unexpected_files'], "'README.md' is unexpectedly flagged.")
        self.assertNotIn('script.py', result['unexpected_files'], "'script.py' is unexpectedly flagged.")
        self.assertIn('unexpected_file.txt', result['unexpected_files'], "'unexpected_file.txt' should be flagged as unexpected.")

if __name__ == '__main__':
    unittest.main()