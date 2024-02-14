import pandas as pd

class FileOperation:
    def readFromFile(self, file_path: str):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                file_contents = file.read()
            return file_contents
        except Exception as e:
            print(f"An error occurred while reading the file '{file_path}': {str(e)}")
            return None

    def save_to_csv(self, data, file_name: str):
        try:
            if not isinstance(data, pd.DataFrame):
                data = pd.DataFrame(data)
            data.to_csv(file_name, index=False)
            print(f"Data saved to {file_name} successfully.")
        except Exception as e:
            print(f"An error occurred while saving to CSV: {str(e)}")

