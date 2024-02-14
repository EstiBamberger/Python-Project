import unittest
from unittest.mock import patch
from io import StringIO
import pandas as pd
from FileOperation import FileOperation


class FileOperationTest(unittest.TestCase):
    def setUp(self):
        self.test_file_path = "test_file.txt"
        self.test_csv_data = {
            'A': [1, 2, 3],
            'B': ['a', 'b', 'c']
        }
        self.test_df = pd.DataFrame(self.test_csv_data)

    def tearDown(self):
        import os
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

    def test_readFromFile_success(self):
        # Create a test file with some content
        with open(self.test_file_path, 'w', encoding='utf-8') as file:
            file.write("Test file content")

        file_operation = FileOperation()
        file_contents = file_operation.readFromFile(self.test_file_path)

        self.assertEqual(file_contents, "Test file content")

    def test_readFromFile_file_not_found(self):
        file_operation = FileOperation()
        file_contents = file_operation.readFromFile("non_existent_file.txt")

        self.assertIsNone(file_contents)

    @patch('builtins.print')
    def test_readFromFile_exception_handling(self, mock_print):
        file_operation = FileOperation()
        file_contents = file_operation.readFromFile("invalid_file.txt")

        self.assertIsNone(file_contents)
        mock_print.assert_called()

    def test_save_to_csv_success(self):
        file_operation = FileOperation()
        file_operation.save_to_csv(self.test_df, "test_output.csv")

        # Check if the CSV file has been created and contains the correct data
        df_read = pd.read_csv("test_output.csv")
        self.assertTrue(df_read.equals(self.test_df))

    @patch('builtins.print')
    def test_save_to_csv_exception_handling(self, mock_print):
        # Test saving with invalid data
        file_operation = FileOperation()
        invalid_data = {'A': [1, 2, 3], 'B': [4, 5]}  # Invalid data with unequal lengths
        file_operation.save_to_csv(invalid_data, "invalid_output.csv")

        # Check if an error message has been printed
        mock_print.assert_called()

if __name__ == '__main__':
    unittest.main()






