from calc import add


# Write your tests below.
# Use assert statements to check that calc returns the correct result.
# All test functions must start with test_ to be discovered by pytest or similar frameworks.
# We have included a single starter test.
# Add more test_* functions as you work through each new requirement.
# Example:

def test_example_string_returns_zero():
    assert add("") == 0  # uncomment to test
    assert add("1") == 1
    assert add("1,2") == 3
    assert add("1,2,3") == 6
    # assert add("1\n2,3") == 6
    # assert add("//;\n1;2") == 3
    # assert add("2,1001") == 2
    # assert add("//[***]\n1***2***3") == 6
    # assert add("//[*][%]\n1*2%3") == 6
    # assert add("//[***][##]\n1***2##3") == 6
