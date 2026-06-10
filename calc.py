""" String Calculator TDD Kata """

def add(numbers):

    # Feature 1: empty string returns 0
    if numbers == "":
        return 0
    # Feature 2: treat newlines as delimiters (normalise before splitting)
    numbers = numbers.replace("\n", ",")
    # Feature 3: split on comma — handles 1, 2, or any number of values
    parts = numbers.split(",")
    # Feature 4: sum all parts
    return sum(int(n) for n in parts)
