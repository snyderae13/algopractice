#Write an algorithm that takes in a string and sorts the words in the string in alphabetical order. The comparison should be case-insensitive.


test_string = "I love software programming"

sorted_strings = sorted(test_string.split(), key =str.lower)
print(sorted_strings)