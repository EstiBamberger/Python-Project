from Task8 import Task8

usernames_file_path = "UsersName.txt"
useremail_file_path = "UsersEmail.txt"

# Task 8 ex 1
checked_file_path = Task8.check_and_create_file(usernames_file_path)
print(f"Checked file path: {checked_file_path}")

# Task 8 ex 2
usernames_generator = Task8.read_usernames(usernames_file_path)

# Print each username
for username in usernames_generator:
   print(username)

# Task 8 ex 3
sophisticated_array = Task8.read_usernames_into_array(usernames_file_path)
print(sophisticated_array)

# Task 8 ex 4
sophisticated_array_even_rows = Task8.read_usernames_into_array_even_rows(usernames_file_path)
print(sophisticated_array_even_rows)

# Task 8 ex 5
filename = "UsersEmail.txt"
emails_generator = Task8.read_emails_from_file(filename)
for email in emails_generator:
    print(email)
filename = "UsersName.txt"
users_generator =Task8.read_users_from_file(filename)
for user in users_generator:
    print(user)

# Task 8 ex 6
gmail_addresses = Task8.filter_gmail_addresses(Task8.read_emails_from_file(useremail_file_path))
print("Gmail Addresses:", gmail_addresses)

# Task 8 ex 7
email_variable_results = Task8.read_emails_and_users_from_files(useremail_file_path, usernames_file_path)
print("Results:", email_variable_results)

# Task 8 ex 8
name = input("Enter your name: ")
usersNames =Task8.read_users_from_file(usernames_file_path)
Task8.check_username_variations(name, usersNames)
# Task 8 ex 9
capitalized_names = Task8.capitalize_names_from_file(usernames_file_path)
print(capitalized_names)
# Task 8 ex 10
total_earnings =Task8.calculate_earnings([9 ,5 ,19 ,43 ,4 ,88 ,76 ,20, 15])
print("Total earnings:", total_earnings)

