""" Edit the function below to implement the String Calculator TDD Kata """

import re

def add(numbers):
    if numbers == "":
        return 0

    delimiter = r",|\n"

    if numbers.startswith("//"):
        header, numbers = numbers.split("\n", 1)
        delimiter = re.escape(header[2:])

    parts = re.split(delimiter + r"|,|\n", numbers)
    return sum(int(n) for n in parts if n != "")
