import os, subprocess

def run_python_file(working_directory, file_path, args=[]):
    full_file_path = os.path.join(working_directory, file_path)
    abs_working_directory_path = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(full_file_path)

    if not abs_file_path.startswith(abs_working_directory_path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    
    if not abs_file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        command_list = ["python", file_path]
        if args:
            command_list += args
        completed_process = subprocess.run(
            command_list, 
            cwd=abs_working_directory_path, 
            capture_output=True, 
            timeout=30.0, 
            text=True)
        
        output = []
        if completed_process.stdout:
            output.append(f"STDOUT:\n{completed_process.stdout}")
        if completed_process.stderr:
            output.append(f"STDERR:\n{completed_process.stderr}")
        if completed_process.returncode != 0:
            print(f'Process exited with code {completed_process.returncode}')
        if output:
            return "\n".join(output)
        else:
            return f'No output produced'
    except Exception as e:
        return f"Error: Cannot execute the command due to : {e}"
    
    
    
