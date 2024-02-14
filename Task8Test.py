import unittest
from unittest.mock import patch

from Task8 import Task8
import os
import re

class TestTask8(unittest.TestCase):
    def setUp(self):
        self.test_file_path = "test_data/test_file.txt"
        self.test_usernames_file_path = "test_data/test_usernames.txt"
        self.test_emails_file_path = "test_data/test_emails.txt"

    def tearDown(self):
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

    def test_check_and_create_file(self):
        # Test file creation
        file_path = Task8.check_and_create_file(self.test_file_path)
        self.assertTrue(os.path.exists(file_path))

    def test_read_usernames(self):
        # Test reading usernames from file
        expected_usernames = ["user1", "user2", "user3"]
        with open(self.test_usernames_file_path, 'w') as file:
            file.write('\n'.join(expected_usernames))

        usernames = list(Task8.read_usernames(self.test_usernames_file_path))
        self.assertEqual(usernames, expected_usernames)

    def test_read_usernames_into_array(self):
        # Test reading usernames into array
        expected_array = ["user2", "user3"]
        sophisticated_array = Task8.read_usernames_into_array("empty_file.csv")

        # Convert generator to list to inspect its contents
        actual_array = list(sophisticated_array)

        # Check if the expected and actual arrays match
        self.assertEqual(actual_array, expected_array)

    @patch("builtins.open", unittest.mock.mock_open(read_data="user0\nuser1\nuser2\nuser3\n"))
    def test_read_usernames_into_array_even_rows(self):
        # Test reading usernames into array from even rows
        expected_array_even_rows = ["user0", "user2"]
        sophisticated_array_even_rows = Task8.read_usernames_into_array_even_rows("dummy_file_path")

        # Convert generator to list to inspect its contents
        actual_array_even_rows = list(sophisticated_array_even_rows)

        # Check if the expected and actual arrays match
        self.assertEqual(actual_array_even_rows, expected_array_even_rows)

    def test_read_emails_from_file(self):
        # Test reading emails from file
        valid_emails = ["test@example.com", "invalid_email", "another@test.com"]
        with open(self.test_emails_file_path, 'w') as file:
            file.write('\n'.join(valid_emails))

        emails = list(Task8.read_emails_from_file(self.test_emails_file_path))
        self.assertEqual(emails, ["test@example.com", "another@test.com"])

    def test_validate_username(self):
        # Test validating usernames
        valid_username = "username"
        invalid_username = "user@name"
        self.assertTrue(Task8.validate_username(valid_username))
        self.assertFalse(Task8.validate_username(invalid_username))

    def test_read_users_from_file(self):
        # Test reading users from file
        valid_users = ["userA", "userB", "invaliduser"]
        with open(self.test_usernames_file_path, 'w') as file:
            file.write('\n'.join(valid_users))

        users = list(Task8.read_users_from_file(self.test_usernames_file_path))
        self.assertEqual(users, valid_users)

    def test_filter_gmail_addresses(self):
        # Test filtering Gmail addresses
        email_addresses = ["test@example.com", "user@gmail.com", "another@test.com"]
        filtered_emails = Task8.filter_gmail_addresses(email_addresses)
        self.assertEqual(filtered_emails, ["user@gmail.com"])

    def test_read_emails_and_users_from_files(self):
        # Test reading emails and users from files
        emails_filename = "test_data/test_emails.txt"
        users_filename = "test_data/test_usernames.txt"
        expected_dict = {'another@test.com': None, 'invalid_email': None, 'test@example.com': None}
        emails_dict = Task8.read_emails_and_users_from_files(emails_filename, users_filename)
        self.assertEqual(emails_dict, expected_dict)

    def test_check_username_variations(self):
        # Test checking username variations
        username = "username"
        usernames_list = ["username", "user1", "user2"]
        Task8.check_username_variations(username, usernames_list)
        # Check console output manually

    def test_capitalize_names_from_file(self):
        # Test capitalizing names from file
        test_names = ["john", "doe", "jane"]
        with open(self.test_file_path, 'w') as file:
            file.write('\n'.join(test_names))

        capitalized_names = Task8.capitalize_names_from_file(self.test_file_path)
        self.assertEqual(capitalized_names, ["John", "Doe", "Jane"])

    def test_calculate_earnings(self):
        # Test calculating earnings
        groups = [2, 8, 14]
        total_earnings = Task8.calculate_earnings(groups)
        self.assertEqual(total_earnings, 800)

if __name__ == '__main__':
    unittest.main()
