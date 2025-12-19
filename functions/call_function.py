from google import genai
from google.genai import types
import os
import sys

from .get_file_content import schema_get_file_content
from .get_files_info import schema_get_files_info
from .run_python_file import schema_run_python_file
from .write_files import schema_write_file


available_functions = types.Tool(
    function_declarations=[schema_get_file_content, schema_get_files_info, schema_write_file, schema_run_python_file]
)