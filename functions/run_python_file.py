import os
import subprocess
import sys
from google import genai
from google.genai import types

def run_python_file(working_directory, file_path, args=None):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(abs_working_dir, file_path))

        # Ensure target_file is inside working directory
        if os.path.commonpath([abs_working_dir, target_file]) != abs_working_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        # Ensure file exists and is a regular file
        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        # Ensure it is a .py file
        if not target_file.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        # Build command: interpreter + script + args
        command = [sys.executable, target_file]
        if args:
            command.extend(args)

        # Run subprocess and capture output
        result = subprocess.run(
            command,
            cwd=abs_working_dir,
            capture_output=True,
            text=True,
            timeout=30,
        )

        # Build output string
        output_lines = []

        if result.returncode != 0:
            output_lines.append(f"Process exited with code {result.returncode}")

        if result.stdout:
            output_lines.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            output_lines.append(f"STDERR:\n{result.stderr}")

        if not output_lines:
            output_lines.append("No output produced")

        return "\n".join(line.rstrip("\n") for line in output_lines) + "\n"

    except Exception as e:
        return f"Error: executing Python file: {e}"

# The google-genai library that we're using to interact with the Gemini API offers a standard format to describe a function for LLM callers: types.FunctionDeclaration. We'll use this to build a "declaration" or "schema" for each of our functions.
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a specified Python file within the working directory and returns its output",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to execute, relative to the working directory",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                ),
                description="Optional list of command-line arguments to pass to the Python file",
            ),
        },
        required=["file_path"],
    ),
)