from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

print("Test 1 --- Start")
print(run_python_file("calculator","main.py"))
print("Test 1 --- End")

print("Test 2 --- Start")
print(run_python_file("calculator","main.py", ["3 + 5"]))
print("Test 2 --- End")

print("Test 3 --- Start")
print(run_python_file("calculator","tests.py"))
print("Test 3 --- End")

print("Test 4 --- Start")
print(run_python_file("calculator","../main.py"))
print("Test 4 --- End")

print("Test 5 --- Start")
print(run_python_file("calculator","nonexistent.py"))
print("Test 5 --- End")