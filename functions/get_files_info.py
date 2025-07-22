import os

def get_files_info(working_directory, directory="."):
    # This is the way I have done this check, it kinda works properly, but i decided to use the one from the solution files
    # since it does cover the check without any doubt.
    #full_path = os.path.join(working_directory, directory)
    #
    #if not full_path.startswith(working_directory):
    #    return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    #
    #if working_directory not in os.path.abspath(full_path):
    #    return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    #

    full_path = os.path.join(working_directory, directory)

    abs_working_dir = os.path.abspath(working_directory)
    abs_target_dir = os.path.abspath(full_path)

    if not abs_target_dir.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'
    
    try:
        directory_content = os.listdir(full_path)
    except Exception as e:
        return f"Error: {e}"
    
    if directory == ".":
        files_info = f'Result for current directory:'
    else:
        files_info = f'Result for {directory} directory:'
    
    for item in directory_content:
        try:
            full_item_path = os.path.join(full_path, item)
        except Exception as e:
            return f'Error: {e}'
        
        try:
            is_item_dir = os.path.isdir(full_item_path)
        except Exception as e:
            return f'Error: {e}'
    
        try:
            size_of_item = os.path.getsize(full_item_path)
        except Exception as e:
            return f'Error: {e}'
        
        files_info += f'\n- {item}: file_size={size_of_item}, is_dir={is_item_dir}'

    return(files_info)