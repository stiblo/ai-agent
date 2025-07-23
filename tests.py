from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

test_cases_files_info = [
    ("calculator","."),
    ("calculator", "pkg"),
    ("calculator", "/bin"),
    ("calculator", "../")

]

test_cases_file_content = [
    ("calculator", "main.py"),
    ("calculator", "pkg/calculator.py"),
    ("calculator", "/bin/cat"),
    ("calculator", "pkg/does_not_exist.py")
]

for test in test_cases_file_content:
    print(get_file_content(test[0], test[1]))