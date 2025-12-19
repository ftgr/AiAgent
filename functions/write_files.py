import os
from google import genai
from google.genai import types


def write_file(working_directory, file_path, content):
    # If the file_path is outside the working_directory, return an error string like the one below
    try:
        abs_working_dir = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(abs_working_dir, file_path))

        if os.path.commonpath([abs_working_dir, target_file]) != abs_working_dir:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        # If the file_path points to an existing directory (this is what os.path.isdir() checks for), return an error string:
        if os.path.isdir(target_file):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        
        # Ensure the directory exists
        # Make sure that all parent directories of the file_path exist. You can use os.makedirs() with the exist_ok=True argument to create any missing directories. If the necessary directory structure already exists, this will do nothing – which is what we want.
        os.makedirs(os.path.dirname(target_file), exist_ok=True)

        # Open the file at file_path in write mode ("w") and overwrite its contents with the content argument.
        with open(target_file, 'w') as file:
            file.write(content)
        
        return f'Success: File "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error writing file: {e}"
    

# The google-genai library that we're using to interact with the Gemini API offers a standard format to describe a function for LLM callers: types.FunctionDeclaration. We'll use this to build a "declaration" or "schema" for each of our functions.
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a specified file within the working directory, creating any necessary directories",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to write to, relative to the working directory",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to write into the file",
            ),
            "working_directory": types.Schema(
                type=types.Type.STRING,
                description="The working directory where files are located",
            ),
        },
        required=["file_path", "content", "working_directory"],
    ),
)