import unittest
import tempfile
import os
from quartoquest.repo_structure_check import check_directory_structure

class TestRepoStructureCheck(unittest.TestCase):
    def test_structure_check(self):
        # Create a temporary directory
        with tempfile.TemporaryDirectory() as tmp_dir:
            # Create mock files and directories as needed
            os.mkdir(os.path.join(tmp_dir, 'data'))
            with open(os.path.join(tmp_dir, 'README.md'), 'w') as f:
                f.write('Sample README content')

            # Perform the test
            # Assuming 'data' should be present and 'README.md' should be there
            result = check_directory_structure(tmp_dir, ['data'], ['README.md'])

            # If 'data' is correctly created, it should not be in missing_directories
            self.assertNotIn('data', result['missing_directories'])

            # If 'README.md' is correctly placed, it should not be in unexpected_files
            self.assertNotIn('README.md', result['unexpected_files'])

# Run the tests
if __name__ == '__main__':
    unittest.main()

