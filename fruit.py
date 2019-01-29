fruits = ["apple", "pear", "blueberry"]
fruit = fruits.pop(0)
print (fruit, fruits)


#numbers = ["o","l","l","h"]
def reverse_string(s):
    """Returns the reversal of the given string."""
    result = ""
    for char in s:
        result = char + result
    return result

print (reverse_string("hello"))
