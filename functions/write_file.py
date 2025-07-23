import os

def write_file(working_directory, file_path, content):
    full_file_path = os.path.join(working_directory, file_path)
    abs_working_directory_path = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(full_file_path)

    if not abs_file_path.startswith(abs_working_directory_path):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(os.path.dirname(abs_file_path)):
        try:
            os.makedirs(os.path.dirname(abs_file_path))
        except Exception as e:
            return f'Error: Cannot create directory : {e}'
        
    if os.path.exists(abs_file_path) and os.path.isdir(abs_file_path):
        return f'Error: "{file_path}" is a directory, not a file'
    
    try:
        with open(full_file_path, "w") as file:
            file.write(content)
    except Exception as e:
        return f'Error: writing to the file {full_file_path} with exception : {e}'
    
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'