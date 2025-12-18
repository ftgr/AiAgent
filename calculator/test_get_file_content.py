# calculator/test_get_files_info.py
import os
import sys

# Add project root (one level up from this file) to sys.path
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from functions.get_file_content import get_file_content


def test():
    result = get_file_content(".", "lorem.txt")
    #print("Result for current directory:")
    print(len(result), result[-51:])  # Print length and last 100 characters
    print("")

    result2 = get_file_content(".", "main.py")
    print(result2)
    result3 = get_file_content(".", "pkg/calculator.py")
    print(result3)
    result4 = get_file_content(".", "/bin/cat") #(this should return an error string)
    print(result4)
    result5 = get_file_content(".", "pkg/does_not_exist.py")
    print(result5)


if __name__ == "__main__":
    test()
