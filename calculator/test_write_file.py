import os
import sys

# Add project root (one level up from this file) to sys.path
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from functions.write_files import write_file

def test():
    result1 = write_file(".", "lorem.txt", "wait, this isn't lorem ipsum")
    print(result1)

    result2 = write_file(".", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(result2)

    result3 = write_file(".", "/tmp/temp.txt", "this should not be allowed")
    print(result3)

if __name__ == "__main__":
    test()