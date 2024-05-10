import unittest
from file_operations.file_reader import read_file
from file_operations.file_writer import write_file

class TestFileOperations(unittest.TestCase):
    def test_read_write_file(self):
        content = "Hello, World!"
        file_path = "test.txt"
        
        write_file(file_path, content)
        read_content = read_file(file_path)
        
        self.assertEqual(read_content, content)

if __name__ == '__main__':
    unittest.main()