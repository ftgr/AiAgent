# calculator/test_get_files_info.py
import os
import sys

# Add project root (one level up from this file) to sys.path
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from functions.get_files_info import get_files_info


def test():
    result = get_files_info(".", ".")
    print("Result for current directory:")
    print(result)
    print("")

    result = get_files_info(".", "pkg")
    print("Result for 'pkg' directory:")
    print(result)

    result = get_files_info(".", "/bin")
    print("Result for '/bin' directory:")
    print(result)

    result = get_files_info(".", "../")
    print("Result for '../' directory:")
    print(result)


if __name__ == "__main__":
    test()
