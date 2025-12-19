import os
import sys

# Add project root (one level up from this file) to sys.path
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from functions.run_python_file import run_python_file

def test():
    # should print the calculator's usage instructions
    result1 = run_python_file(".", "main.py", args=[])
    print("Result 1:")
    print(result1)

    # should run the calculator... which gives a kinda nasty rendered result)
    result2 = run_python_file(".", "main.py", args=["3", "+", "5"])
    print("Result 2:")
    print(result2)

    # should run the calculator's tests successfully
    result3 = run_python_file(".", "tests.py")
    print("Result 3:")
    print(result3)

    # this should return an error
    result4 = run_python_file(".", "../main.py")
    print("Result 4:")
    print(result4)

    # this should return an error
    result5 = run_python_file(".", "nonexistent.py")
    print("Result 5:")
    print(result5)  

    # this should return an error
    result6 = run_python_file(".", "lorem.txt")
    print("Result 6:")
    print(result6)


if __name__ == "__main__":
    test()