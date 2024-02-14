from FileOperation import FileOperation

usernames_file_path = "UsersName.txt"
useremail_file_path = "UsersEmail.txt"

file_op = FileOperation()

# Reading from file
file_contents = file_op.readFromFile("YafeNof.csv")
if file_contents is not None:
    print("File contents:")
    print(file_contents)

# Saving to CSV
data = {'Column1': [1, 2, 3], 'Column2': ['A', 'B', 'C']}
file_op.save_to_csv(data, "example.csv")


