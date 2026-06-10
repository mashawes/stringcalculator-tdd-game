""" String Calculator TDD Kata """
import re

def add(numbers):

    # Feature 1: empty string returns 0
    if numbers == "":
        return 0

    # Feature 2: treat newlines and commas as default delimiters
    delimiter = r",|\n"

    # Feature 3: support custom delimiter via //[delimiter]\n header
    if numbers.startswith("//"):
        header, numbers = numbers.split("\n", 1)
        delimiter = re.escape(header[2:])

    # Feature 4: split on delimiter — handles any number of values
    parts = re.split(delimiter + r"|,|\n", numbers)
    values = [int(n) for n in parts if n != ""]

    # Feature 5: reject negative numbers
    negatives = [v for v in values if v < 0]
    if negatives:
        raise ValueError(f"negatives not allowed: {', '.join(str(n) for n in negatives)}")

    # Feature 6: sum all parts
    return sum(values)
    if numbers.startswith("//"):
        header, numbers = numbers.split("\n", 1)
        raw = header[2:]
        delimiter = re.escape(raw)
