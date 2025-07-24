import os
from config import MAX_CHARS
from google.genai import types

def get_file_content(working_directory, file_path):
    full_file_path = os.path.join(working_directory, file_path)

    abs_working_directory_path = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(full_file_path)

    if not abs_file_path.startswith(abs_working_directory_path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(full_file_path, 'r') as file:
            content = file.read()
            if len(content) > MAX_CHARS:
                content = content[:MAX_CHARS]
                content += f'[...File "{full_file_path}" truncated at 10000 characters]'
    except Exception as e:
        return f'Error: Unable to read the file {e}'
    
    return content

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Return contents of the file, truncated at maximum chars defined in config.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path to the file that we are returning contents of.",
            ),
        },
    ),
)
    

    

    
