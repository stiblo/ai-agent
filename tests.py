from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file

print("TEST 1")
print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
print("END TEST 1")

print("TEST 2")
print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
print("END TEST 2")

print("TEST 3")
print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
print("END TEST 3")