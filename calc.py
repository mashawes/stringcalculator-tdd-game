""" String Calculator TDD Kata """

def add(numbers):

    # Feature 1: empty string returns 0
    if numbers == "":
        return 0
    # Feature 2: treat newlines as delimiters (normalise before splitting)
    numbers = numbers.replace("\n", ",")
