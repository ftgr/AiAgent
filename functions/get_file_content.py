import os
from config import MAX_FILE_SIZE


def get_file_content(working_directory, file_path):
    # If the file_path is outside the working_directory, return the error string below. To validate the path, you can use essentially the same logic that you wrote for get_files_info.
    try:
        abs_working_dir = os.path.abspath(working_directory)

        target_file = os.path.normpath(os.path.join(abs_working_dir, file_path))


        if os.path.commonpath([abs_working_dir, target_file]) != abs_working_dir:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        with open(target_file, 'r') as file:
            content = file.read(MAX_FILE_SIZE)  # Read up to 10,000 characters
            if file.read(1):  # Check if there's more content beyond the limit
                content += f'[...File "{file_path}" truncated at {MAX_FILE_SIZE} characters]'
        
        return content
    
    except Exception as e:
        return f"Error: {e}"