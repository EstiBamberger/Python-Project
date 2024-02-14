import importlib
import inspect
import os
import re


class Task8:

    # 1
    def check_and_create_file(file_path):
        if not os.path.exists(file_path):
            # Create the directory if it doesn't exist
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            # Create the file
            with open(file_path, 'w') as f:
                pass  # Do nothing, just create an empty file
        return file_path

    # 2
    def read_usernames(file_path):
        with open(file_path, 'r') as file:
            for line in file:
                yield line.strip()


    # 3
    def read_usernames_into_array(usernames_file_path):
        # Initialize an empty array
        sophisticated_array = []

        # Read usernames from the file and add them to the array
        with open(usernames_file_path, 'r') as file:
            usernames = file.readlines()

        # Calculate the number of users to exclude (10% of total users)
        num_users_to_exclude = int(len(usernames) * 0.1)

        # Add each username to the array, excluding the first 10% of users
        for i, username in enumerate(usernames):
            if i < num_users_to_exclude:
                # Exclude the first 10% of users
                sophisticated_array.append(None)  # or whatever placeholder for users with no access
            else:
                sophisticated_array.append(username.strip())  # Add username to the array

        return sophisticated_array

    # 4

    def read_usernames_into_array_even_rows(usernames_file_path):
        # Initialize an empty array
        sophisticated_array_even_rows = []

        # Read usernames from the file and add them to the array, skipping even rows
        with open(usernames_file_path, 'r') as file:
            usernames = file.readlines()

        # Calculate the number of users to exclude (10% of total users)
        num_users_to_exclude = int(len(usernames) * 0.1)

        # Add each username to the array, excluding the first 10% of users from even rows
        for i, username in enumerate(usernames):
            if i % 2 == 0:  # Check if the row index is even
                if i < num_users_to_exclude:
                    # Exclude the first 10% of users
                    sophisticated_array_even_rows.append(None)  # or whatever placeholder for users with no access
                else:
                    sophisticated_array_even_rows.append(username.strip())  # Add username to the array

        return sophisticated_array_even_rows

    # 5
    def read_emails_from_file(filename):
        with open(filename, 'r') as file:
            for line in file:
                email = line.strip()
                if re.match(r"[^@]+@[^@]+\.[^@]+", email):  # Check if the line is a valid email address
                    yield email
                else:
                    print(f"{email} is not valid")

    def validate_username(username):
        return username.isalpha()

    def read_users_from_file(filename):
        with open(filename, 'r') as file:
            for line in file:
                username = line.strip()
                if Task8.validate_username(username):  # Assuming you have a function to validate usernames
                    yield username
                else:
                    print(f"{username} is not valid")



    # 6
    def filter_gmail_addresses(email_addresses):
        gmail_addresses = [email for email in email_addresses if email.endswith('@gmail.com')]
        return gmail_addresses

    # 7
    def read_emails_and_users_from_files(emails_filename, users_filename):
        emails_dict = {}
        with open(emails_filename, 'r') as email_file:
            for line in email_file:
                email = line.strip()
                emails_dict[email] = None

        with open(users_filename, 'r') as users_file:
            for line in users_file:
                username = line.strip()
                for email in emails_dict.keys():
                    if username.lower() in email.lower():
                        emails_dict[email] = username
                        break

        return emails_dict
    # 8
    def check_username_variations(username, usernames_list):
        # Check if the username is in the list
        if username in usernames_list:
            print(f"Username '{username}' is in the list.")

        # Define conversion types
        conversions = {
            'Capitalize': lambda name: name.capitalize(),
            'To Lowercase': lambda name: name.upper(),
            'Reverse': lambda name: name[::-1],
            'Count Characters': lambda name: len(name)
        }

        # Convert the username to ASCII code
        ascii_code_username = []
        for char in username:
            ascii_code = ord(char)
            ascii_code_username.append(ascii_code)
            print(f"ASCII code of '{char}' in the username: {ascii_code}")
        # Print conversion types and perform conversions
        for conversion_type, conversion_func in conversions.items():
            converted_username = conversion_func(username)
            print(f"{conversion_type}: {converted_username}")

        # Convert the username back to string
        username_string = ''.join(chr(code) for code in ascii_code_username)
        print(f"Converted username back to string: {username_string}")

        # Count the number of times the letter 'A' appears in the username
        count_A = username.lower().count('a')
        print(f"Number of times the letter 'A' appears in the username: {count_A}")

    def capitalize_names_from_file(file_path):
        # Open the file and read names
        with open(file_path, 'r') as file:
            names = file.readlines()

        # Remove whitespace and capitalize each name
        capitalized_names = [name.strip().capitalize() for name in names]

        return capitalized_names

    def calculate_earnings(groups):
        total_earnings = 0

        for group in groups:
            x = group % 8
            y = group // 8
            total_earnings += (200 * y) + (50 * x)

        return total_earnings

