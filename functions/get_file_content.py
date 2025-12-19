import os
from config import MAX_FILE_SIZE
from google import genai
from google.genai import types

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
    

# The google-genai library that we're using to interact with the Gemini API offers a standard format to describe a function for LLM callers: types.FunctionDeclaration. We'll use this to build a "declaration" or "schema" for each of our functions.
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads and returns the content of a specified file within the working directory, up to a maximum size limit",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to read, relative to the working directory",
            ),
            "working_directory": types.Schema(
                type=types.Type.STRING,
                description="The working directory where files are located",
            ),
        },
        required=["working_directory", "file_path"],
    ),
)

