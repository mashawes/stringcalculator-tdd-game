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
    values = [int(n) for n in parts if n != ""]

    negatives = [v for v in values if v < 0]
    if negatives:
        raise ValueError(f"negatives not allowed: {', '.join(str(n) for n in negatives)}")

    return sum(values)